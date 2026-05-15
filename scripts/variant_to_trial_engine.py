
import json
import pandas as pd
import os

BASE = os.path.dirname(os.path.dirname(__file__))

DATA_PATH = os.path.join(BASE, "data")
RESULTS_PATH = os.path.join(BASE, "results")

# Load datasets
master = pd.read_csv(os.path.join(DATA_PATH, "precision_oncology_master_matrix.csv"))

with open(os.path.join(RESULTS_PATH, "civic_molecular_profiles.json")) as f:
    civic = json.load(f)

with open(os.path.join(RESULTS_PATH, "matched_trials_report.json")) as f:
    trials = json.load(f)

print("Loaded datasets successfully")
print("Master shape:", master.shape)
print("CIViC records:", len(civic))
print("Trials records:", len(trials))


def generate_report(gene, variant):
    report = {
        "Gene": gene,
        "Variant": variant,
        "CIViC_Evidence": [],
        "Clinical_Trials": []
    }

    # CIViC match
    for item in civic:
        if gene.lower() in item.get("Name", "").lower():
            report["CIViC_Evidence"].append(item)

    # Trial match
    for t in trials:
        if gene.lower() in str(t).lower():
            report["Clinical_Trials"].append(t)

    return report


if __name__ == "__main__":
    print(generate_report("KRAS", "G12C"))
