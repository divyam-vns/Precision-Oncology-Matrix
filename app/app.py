
import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="Precision Oncology Matrix", layout="wide")

st.title("🧬 Precision Oncology Dashboard")

BASE = os.path.dirname(__file__)
ROOT = os.path.dirname(BASE)

DATA_PATH = os.path.join(ROOT, "data")
RESULTS_PATH = os.path.join(ROOT, "results")

# Load data
@st.cache_data
def load_data():
    with open(os.path.join(RESULTS_PATH, "civic_molecular_profiles.json")) as f:
        civic = json.load(f)

    with open(os.path.join(RESULTS_PATH, "matched_trials_report.json")) as f:
        trials = json.load(f)

    master = pd.read_csv(os.path.join(DATA_PATH, "precision_oncology_master_matrix.csv"))

    return civic, trials, master

civic, trials, master = load_data()

st.sidebar.header("Input Mutation")
gene = st.sidebar.text_input("Gene", "KRAS")
variant = st.sidebar.text_input("Variant", "G12C")

if st.sidebar.button("Run Analysis"):

    st.subheader("🔬 Clinical Interpretation")

    st.write("### CIViC Evidence Matches")
    civic_hits = [c for c in civic if gene.lower() in str(c.get("Name","")).lower()]
    st.write(civic_hits)

    st.write("### Clinical Trial Matches")
    trial_hits = [t for t in trials if gene.lower() in str(t).lower()]
    st.write(trial_hits)

    st.success("Analysis Complete")

else:
    st.info("Enter a gene and click Run Analysis")

st.write("---")
st.caption("Built for Precision Oncology Portfolio Project")
