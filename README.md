# Snakemake Workflow: Data Simulation, Processing, and Visualization

This repository contains a **Snakemake workflow** that simulates a dataset, processes it, generates summary statistics, and creates a visualization.


## **1. Setting Up the Environment**

### **Using a Python Virtual Environment (Recommended)**
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## **2. Running the Workflow**
To execute the Snakemake workflow, simply run:
```bash
snakemake --cores 1
```
For parallel execution:
```bash
snakemake --cores 4
```

## **3. Generating the DAG (Workflow Visualization)**
To visualize the workflow, generate a **DAG (Directed Acyclic Graph)**:
```bash
snakemake --dag | dot -Tpng > dag.png
```
Open `dag.png` to see the workflow structure.

## **4. Expected Output Files**
- `data/raw_data.csv` → Randomly generated dataset.
- `data/processed_data.csv` → Processed dataset with additional columns.
- `data/report.txt` → Summary statistics of the dataset.
- `figures/plot.png` → Visualization of the dataset.

## **5. Cleaning Up Generated Files**
To remove all output files and rerun the workflow from scratch:
```bash
snakemake --cleanup
```
Or manually delete the `data/` directory contents.

## **6. Troubleshooting**
- If `snakemake` is not found, ensure your virtual environment or Conda environment is activated.
- If `dot` is not found when generating the DAG, install `Graphviz`:
  ```bash
  sudo apt install graphviz  # Ubuntu/Debian
  brew install graphviz      # macOS (Homebrew)
  conda install -c conda-forge graphviz  # Conda
  ```

## **7. License**
This project is released under the MIT License.

## **8. Author**
Developed by Ben Lambert.

