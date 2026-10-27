# report.py
import pandas as pd
import os

def generate_report(df_pred=None):
    if df_pred is None:
        if not os.path.exists("inheritance_predictions.csv"):
            print("❌ No predictions found.")
            return
        df_pred = pd.read_csv("inheritance_predictions.csv")

    merged = df_pred.copy()
    merged["Expression_Avg"] = ((merged["Expression_A"] + merged["Expression_B"]) / 2).round(2)
    merged.to_csv("final_gene_inheritance_report.csv", index=False)

    with open("summary_report.txt", "w", encoding="utf-8") as f:
        for _, r in merged.iterrows():
            f.write(f"{r['Gene']}: {r['Disease']} | {r['Risk_Status']} | {r['Probability']}\n")

    print("✅ Reports generated successfully.")
    return merged

if __name__ == "__main__":
    generate_report()
