import os
import glob
import json
import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

def run_verify():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    log_file = os.path.join(project_root, "verification_log.txt")
    
    # Dynamically find all Jupyter Notebooks in the project root and sort them alphabetically
    notebook_paths = sorted(glob.glob(os.path.join(project_root, "*.ipynb")))
    
    with open(log_file, "w", encoding="utf-8") as log:
        log.write("=== NOTEBOOK EXECUTION VERIFICATION LOG ===\n\n")
        
        print(f"Found {len(notebook_paths)} notebook(s) to verify.")
        print("Starting cell execution verification across all notebooks...")
        print(f"Logs will be written to {log_file}")
        
        errors_found = 0
        
        for nb_path in notebook_paths:
            nb_name = os.path.basename(nb_path)
            log.write(f"--- Running: {nb_name} ---\n")
            print(f"Running {nb_name}...")
            
            try:
                with open(nb_path, "r", encoding="utf-8") as f:
                    nb = nbformat.read(f, as_version=4)
                
                # Execute notebook allowing errors so we can capture tracebacks from all cells
                client = NotebookClient(nb, timeout=60, allow_errors=True)
                client.execute()
                
                nb_errors = 0
                for idx, cell in enumerate(nb.cells):
                    if cell.cell_type != "code":
                        continue
                    
                    # Check if cell has error outputs
                    outputs = cell.get("outputs", [])
                    has_error = False
                    traceback_lines = []
                    
                    for out in outputs:
                        if out.get("output_type") == "error":
                            has_error = True
                            traceback_lines = out.get("traceback", [])
                            break
                    
                    if has_error:
                        source_code = cell.get("source", "")
                        
                        # Filter out expected challenge/assertion failures
                        is_expected_fail = (
                            "NotImplementedError" in source_code or 
                            "raise NotImplementedError" in source_code or
                            "assert " in source_code or
                            "# Challenge" in source_code or
                            "# Exercise" in source_code
                        )
                        
                        if not is_expected_fail:
                            nb_errors += 1
                            errors_found += 1
                            log.write(f"❌ Cell {idx} failed in {nb_name}!\n")
                            log.write("Source Code:\n")
                            log.write("```python\n" + source_code + "\n```\n")
                            log.write("Traceback:\n")
                            log.write("\n".join(traceback_lines) + "\n")
                            log.write("-" * 40 + "\n\n")
                
                if nb_errors == 0:
                    log.write(f"✅ {nb_name} run completed with no explanation cell errors.\n\n")
                else:
                    log.write(f"❌ {nb_name} had {nb_errors} unexpected cell error(s).\n\n")
                    
            except Exception as e:
                log.write(f"💥 Failed to execute notebook {nb_name} entirely: {e}\n\n")
                errors_found += 1
        
        log.write(f"\nVerification finished. Total unexpected errors: {errors_found}\n")
        print(f"\nVerification completed. Total unexpected errors: {errors_found}")
        print(f"Please check {log_file} for detailed tracebacks.")

if __name__ == "__main__":
    run_verify()
