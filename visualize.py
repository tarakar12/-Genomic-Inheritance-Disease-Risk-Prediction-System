# visualize.py
import matplotlib.pyplot as plt
import pandas as pd
import os

def show_visualizations(df_pred=None, show_in_terminal=False):
    """
    Visualizes genomic inheritance data.
    If show_in_terminal=True → opens matplotlib windows sequentially.
    If False → returns figures for Streamlit use.
    """
    if df_pred is None:
        if os.path.exists("inheritance_predictions.csv"):
            df_pred = pd.read_csv("inheritance_predictions.csv")
            print("✅ Loaded inheritance_predictions.csv")
        else:
            print("❌ No prediction data found. Run main pipeline first.")
            return

    # --- Prepare plots ---
    x = df_pred["Gene"]

    # 1️⃣ Bar Chart: Expression Levels
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.bar(x, df_pred["Expression_A"], width=0.4, label="Person A", color="#4CAF50", align="center")
    ax1.bar(x, df_pred["Expression_B"], width=0.4, label="Person B", color="#2196F3", align="edge")
    ax1.set_ylabel("Expression Level")
    ax1.set_xlabel("Gene")
    ax1.set_title("Gene Expression: Person A vs Person B")
    ax1.legend()
    plt.tight_layout()

    # 2️⃣ Pie Chart: Risk Distribution
    counts = df_pred["Risk_Status"].value_counts()
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    ax2.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["#E57373", "#FFD54F", "#81C784"]
    )
    ax2.set_title("Risk Distribution")

    # 3️⃣ Line Chart: Probability per Gene
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    ax3.plot(x, df_pred["Probability"], marker='o', color="#FF9800", linewidth=2)
    for i, v in enumerate(df_pred["Probability"]):
        ax3.text(i, v + 0.02, f"{v:.2f}", ha="center", fontsize=9)
    ax3.set_ylim(0, 1.05)
    ax3.set_xlabel("Gene")
    ax3.set_ylabel("Inheritance Probability")
    ax3.set_title("Inheritance Probability per Gene")
    ax3.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    # --- Display or Return ---
    if show_in_terminal:
        print("\n📊 Showing all charts in terminal...")
        for i, fig in enumerate([fig1, fig2, fig3], start=1):
            plt.figure(fig.number)
            plt.show(block=True)   # waits until you close each manually
            print(f"✅ Closed chart {i}")
        print("✅ All charts closed successfully.\n")
    else:
        return [fig1, fig2, fig3]


# Standalone test
if __name__ == "__main__":
    show_visualizations(show_in_terminal=True)
