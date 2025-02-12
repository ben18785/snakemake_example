rule all:
    input:
        "data/report.csv",
        "figures/plot.png"

rule download:
    output:
        "data/raw_data.csv"
    shell:
        "python scripts/download_data.py"

rule process:
    input:
        "data/raw_data.csv"
    output:
        "data/processed_data.csv"
    shell:
        "python scripts/process_data.py"

rule report:
    input:
        "data/processed_data.csv"
    output:
        "data/report.csv"
    shell:
        "python scripts/report.py"

rule plot:
    input:
        "data/processed_data.csv"
    output:
        "figures/plot.png"
    shell:
        "python scripts/plot_data.py"