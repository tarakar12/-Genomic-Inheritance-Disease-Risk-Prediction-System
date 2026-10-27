# predictmodel.py
import pandas as pd

def compute_predictions(df, disease_db):
    df2 = df.copy()
    probs, risks = [], []

    for _, r in df2.iterrows():
        mutA, mutB = r["Mutation_A"] == "Yes", r["Mutation_B"] == "Yes"
        exprA, exprB = float(r["Expression_A"]), float(r["Expression_B"])

        expr_diff = abs(exprA - exprB)
        expr_sim = max(0.0, 1 - expr_diff / 100)

        if mutA and mutB: base = 0.85
        elif mutA: base = 0.65
        elif mutB: base = 0.45
        else: base = 0.15

        prob = round(min(0.99, base * 0.7 + expr_sim * 0.3), 3)
        if prob >= 0.8: risk = "High Risk"
        elif prob >= 0.55: risk = "Medium Risk"
        elif prob >= 0.3: risk = "Low Risk"
        else: risk = "Very Low Risk"

        probs.append(prob)
        risks.append(risk)

    df2["Disease"] = df2["Gene"].map(disease_db).fillna("-")
    df2["Probability"] = probs
    df2["Risk_Status"] = risks

    df2 = df2.sort_values(by="Probability", ascending=False).reset_index(drop=True)
    print("\n🤖 Predictions complete:")
    print(df2[["Gene","Disease","Mutation_A","Mutation_B","Probability","Risk_Status"]])

    df2.to_csv("inheritance_predictions.csv", index=False)
    print("✅ Predictions saved to 'inheritance_predictions.csv'")
    return df2

if __name__ == "__main__":
    from samplemain import generate_samples
    df_sample, db = generate_samples()
    compute_predictions(df_sample, db)
