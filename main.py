# main.py
import pandas as pd
import numpy as np
from samplemain import generate_samples

def input_manual_genes():
    print("\nIf you want to use sample data, just press Enter when asked for number of genes.")
    n_str = input("Enter number of genes to input (or press Enter for sample): ").strip()
    if n_str == "":
        return None
    try:
        n = int(n_str)
    except:
        print("Invalid number — using sample data.")
        return None

    rows = []
    for i in range(n):
        print(f"\nGene #{i+1}:")
        gene = input("  Gene name (e.g. BRCA1): ").strip() or f"Gene_{i+1}"
        exprA = input("  Expression for Person A (numeric): ").strip()
        exprB = input("  Expression for Person B (numeric): ").strip()
        mutA = input("  Mutation A? (Yes/No): ").strip().capitalize()
        mutB = input("  Mutation B? (Yes/No): ").strip().capitalize()

        try:
            exprA = float(exprA)
        except:
            exprA = np.round(np.random.uniform(5, 20), 1)
        try:
            exprB = float(exprB)
        except:
            exprB = np.round(exprA + np.random.uniform(-3, 3), 1)

        rows.append({
            "Gene": gene,
            "Expression_A": exprA,
            "Expression_B": exprB,
            "Mutation_A": mutA if mutA in ["Yes", "No"] else "No",
            "Mutation_B": mutB if mutB in ["Yes", "No"] else "No"
        })

    df = pd.DataFrame(rows)
    print("\n✅ Manual input data captured:")
    print(df)
    return df

def main():
    df_manual = input_manual_genes()
    if df_manual is None:
        df, disease_db = generate_samples()
    else:
        df = df_manual
        disease_db = {
            "BRCA1": "Breast / Ovarian Cancer",
            "TP53": "Li-Fraumeni Syndrome",
            "EGFR": "Non-small cell lung cancer",
            "MYC": "Various cancers (oncogene)",
            "APOE": "Alzheimer's Disease"
        }
    return df, disease_db

if __name__ == "__main__":
    df_main, db = main()
