# Bottom-Up Python Tutorial

Welcome to the bottom-up Python tutorial series! This curriculum is designed as a series of runnable Jupyter Notebooks, strictly mapped to the [official Python Language Reference](https://docs.python.org/3/reference/index.html).

"Bottom-up" means we start from the absolute fundamental building blocks of the language (lexical structure, basic data models) and progressively build up to complex abstractions (classes, modules, decorators).

## Getting Started

Follow these steps to set up your environment and start learning.

### 1. Create a Virtual Environment and Install Dependencies

We recommend using [`uv`](https://github.com/astral-sh/uv) to manage your Python environment. You'll need `jupyter` and `ipykernel` to run these notebooks.

Open your terminal or command prompt in this directory and run:

```bash
uv venv
```

Then install the dependencies directly using uv:

```bash
uv pip install -r requirements.txt
```

### 2. Start Jupyter Notebook or JupyterLab

You can launch the server in one of two modes depending on your navigation preference:

#### Option A: JupyterLab (Recommended for same-window navigation)
If you want to navigate all notebooks and the Table of Contents within the **same browser window/tab** using an IDE-style tabbed workspace, run:
```bash
uv run jupyter lab TOC.ipynb
```
All module navigation links you click will open as editor tabs inside the same browser window.

#### Option B: Jupyter Notebook
If you prefer the classic, document-centric view where clicking any notebook link opens the document in a **new browser tab/window**, run:
```bash
uv run jupyter notebook TOC.ipynb
```

If the browser does not open automatically:
1. Look at the terminal output for the server URL (usually starting with `http://localhost:8888/...`)
2. Copy the URL in its entirety.
3. Paste the URL into your web browser's address bar and press Enter.


### 3. Open a Notebook

Click on any `.ipynb` file (e.g., `01_lexical_structure.ipynb`) to open it. 
You can run individual code cells by selecting them and pressing `Shift + Enter`.

## Curriculum Outline

The curriculum is structured into 19 modules and 3 appendices. For a detailed roadmap of all topics and coding challenges, please refer to the dedicated [TOC.ipynb](TOC.ipynb) file.

1. **Notebook 01**: Lexical Structure & Basic Execution
2. **Notebook 02**: The Python Data Model (Fundamentals)
3. **Notebook 03**: Expressions and Operations
4. **Notebook 04**: Simple Statements
5. **Notebook 05**: Compound Statements (Control Flow)
6. **Notebook 06**: Built-in Data Structures
7. **Notebook 07**: Functions and Scoping
8. **Notebook 08**: Exception Handling
9. **Notebook 09**: Classes and Object-Oriented Programming
10. **Notebook 10**: Advanced Data Model (Magic Methods)
11. **Notebook 11**: Type Hinting & Static Analysis
12. **Notebook 12**: Iterators and Generators
13. **Notebook 13**: Context Managers and Decorators
14. **Notebook 14**: Metaprogramming & Custom Descriptors
15. **Notebook 15**: Concurrency & Asynchronous Programming
16. **Notebook 16**: Modules and Packages
17. **Notebook 17**: Modern Packaging, Dependencies & Build Systems
18. **Notebook 18**: Testing, Mocking & Code Quality
19. **Notebook 19**: Memory Management, Weak References & Garbage Collection

### Appendices
* **Appendix A**: Database Connectivity & PEP 249
* **Appendix B**: Regular Expressions (The `re` Module)
* **Appendix C**: Serialization & Serialization Formats

## Verification

To check that all notebook files are structurally sound, you can run the provided validation script:

```bash
uv run python tests/validate_notebooks.py
```

Happy learning!
