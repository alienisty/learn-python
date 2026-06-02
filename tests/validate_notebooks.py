import os
import glob
import json

def validate():
    print("Starting structural notebook verification...")
    errors = 0
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Dynamically find all notebooks in the project root
    notebooks = sorted([os.path.basename(p) for p in glob.glob(os.path.join(project_root, "*.ipynb"))])
    print(f"Found {len(notebooks)} notebook(s) to structurally validate.")
    
    for nb in notebooks:
        path = os.path.join(project_root, nb)
        if not os.path.exists(path):
            print(f"[FAIL] File missing: {nb}")
            errors += 1
            continue

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Check basic Jupyter structure
            if "cells" not in data:
                print(f"[FAIL] {nb}: Missing 'cells' list")
                errors += 1
                continue
            
            if "nbformat" not in data or data["nbformat"] < 4:
                print(f"[FAIL] {nb}: Incorrect or missing 'nbformat' version ({data.get('nbformat')})")
                errors += 1
                continue

            # Verify that every cell has required fields
            cell_errors = False
            for idx, cell in enumerate(data["cells"]):
                if "cell_type" not in cell:
                    print(f"[FAIL] {nb}: Cell {idx} is missing 'cell_type'")
                    cell_errors = True
                if "source" not in cell:
                    print(f"[FAIL] {nb}: Cell {idx} is missing 'source'")
                    cell_errors = True
            
            if cell_errors:
                errors += 1
                continue

            print(f"[OK] {nb} is structurally valid.")

        except json.JSONDecodeError as e:
            print(f"[ERROR] {nb}: Failed to parse JSON: {e}")
            errors += 1
        except Exception as e:
            print(f"[ERROR] {nb}: Unexpected error: {e}")
            errors += 1

    if errors == 0:
        print(f"\n[SUCCESS] All {len(notebooks)} notebooks/appendices are structurally valid nbformat v4 files.")
        return True
    else:
        print(f"\n[FAIL] Validation failed with {errors} error(s).")
        return False

if __name__ == "__main__":
    validate()
