# samplemain.py
import pandas as pd
import numpy as np
from Bio.Seq import Seq

def generate_samples(seed: int = 42):
    np.random.seed(seed)

    genes = ["BRCA1", "TP53", "EGFR", "MYC", "APOE"]
    n = len(genes)
    expr_A = np.round(np.random.uniform(5, 20, n), 1)
    expr_B = np.round(expr_A + np.random.uniform(-3, 3, n), 1)

    mut_A = np.random.choice(["Yes", "No"], size=n, p=[0.3, 0.7])
    mut_B = []
    for i in range(n):
        if mut_A[i] == "Yes":
            mut_B.append(np.random.choice(["Yes", "No"], p=[0.6, 0.4]))
        else:
            mut_B.append(np.random.choice(["Yes", "No"], p=[0.2, 0.8]))
    mut_B = np.array(mut_B)

    df = pd.DataFrame({
        "Gene": genes,
        "Expression_A": expr_A,
        "Expression_B": expr_B,
        "Mutation_A": mut_A,
        "Mutation_B": mut_B
    })

    disease_db = {
        "BRCA1": "Breast / Ovarian Cancer",
        "TP53": "Li-Fraumeni Syndrome",
        "EGFR": "Non-small cell lung cancer",
        "MYC": "Various cancers (oncogene)",
        "APOE": "Alzheimer's Disease"
    }

    dna_seq = Seq("ATGCGTAGCTAGTACGATCGN")
    print("\n🧬 DNA:", dna_seq)
    print("RNA :", dna_seq.transcribe())
    print("Protein:", dna_seq.translate())

    print("\n✅ Sample data generated successfully!")
    return df, disease_db

if __name__ == "__main__":
    df_sample, db = generate_samples()
    print(df_sample)
