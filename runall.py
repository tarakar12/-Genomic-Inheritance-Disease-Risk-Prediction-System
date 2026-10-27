# runall.py
import time
import samplemain
import main as main_module
import predictmodel
from visualize import show_visualizations
import report
import subprocess

def run_all():
    print("🚀 Starting Genomic Inheritance Demo\n")

    # Step 1: load data
    df, disease_db = main_module.main()

    # Step 2: predict
    df_pred = predictmodel.compute_predictions(df, disease_db)

    # Step 3: show charts (terminal)
    show_visualizations(df_pred, show_in_terminal=True)

    # Step 4: generate report
    report.generate_report(df_pred)

    print("\n🎉 All steps complete. Opening dashboard soon...")
    time.sleep(2)

    # Step 5: open Streamlit dashboard (after closing all charts)
    subprocess.Popen(["streamlit", "run", "streamlitapp.py"])

if __name__ == "__main__":
    run_all()
