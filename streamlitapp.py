import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="🧬 Genomic Inheritance & Disease Risk Dashboard",
    page_icon="🧫",
    layout="wide"
)

# ---- SIDEBAR NAVIGATION ----
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📥 Data Input", "🔮 Predictions", "📊 Visuals", "📄 Reports", "⚙️ Settings"]
)

# ---- Function to show small image below sidebar navigation ----
def sidebar_image():
    img_path = "dna_icon.png"  # Ensure this image is in the same folder as this file
    if os.path.exists(img_path):
        st.sidebar.image(img_path, caption="Genomic Dashboard", width=120)
    else:
        st.sidebar.info("🖼️ Add dna_icon.png in this folder.")

# ---- HOME PAGE ----
if page == "🏠 Home":
    st.title("🧬 Genomic Inheritance & Disease Risk Prediction System")

    # ✅ Small image directly below the title
    img_path = "dna_icon.png"
    if os.path.exists(img_path):
        st.image(img_path, caption="Genomic Insight Visualization", width=200)
    else:
        st.info("🖼️ Please place an image named **dna_icon.png** in the same folder.")

    # Intro text
    st.markdown("""
    ### Welcome to the Genomic Inheritance Analysis Dashboard

    This platform helps researchers and clinicians:
    - 🧬 Analyze **genetic inheritance patterns**
    - 📈 Predict **disease risk levels**
    - 🧠 Visualize **gene expression data**
    - 🧾 Generate **summary and detailed reports**
    
    ---

    ### 🧠 How This Project Works
    1. **Data Collection:** Input or upload genetic data (gene names, expression levels, etc.)  
    2. **Analysis & Prediction:** The model compares gene expression between individuals and estimates risk levels.  
    3. **Visualization:** Displays expression charts and disease risk distributions for better interpretation.  
    4. **Report Generation:** Summarizes results into easy-to-read reports for medical or research purposes.

    ---
    ---
    """)

# ---- DATA INPUT PAGE ----
elif page == "📥 Data Input":
    sidebar_image()
    st.title("📥 Input or Upload Genetic Data")
    st.markdown("Provide data for gene expression either manually, through a file, or use sample data.")

    method = st.radio("Choose Input Method:", ["🧾 Upload CSV", "🧬 Manual Entry", "📊 Use Sample Data"])

    if method == "🧾 Upload CSV":
        uploaded = st.file_uploader("Upload a gene expression CSV file", type=["csv"])
        if uploaded is not None:
            df = pd.read_csv(uploaded)
            st.dataframe(df)
            st.success("✅ File uploaded successfully!")

    elif method == "🧬 Manual Entry":
        st.subheader("Enter Gene Data")
        gene = st.text_input("Gene Name")
        patient_id = st.text_input("Patient ID")
        expression = st.number_input("Expression Level", min_value=0.0, format="%.2f")
        risk = st.selectbox("Disease Risk", ["Low", "Medium", "High"])
        if st.button("Submit"):
            st.success(f"Data saved for {gene} ({patient_id}) - Risk: {risk}")

    elif method == "📊 Use Sample Data":
        if os.path.exists("gene_data.csv"):
            df = pd.read_csv("gene_data.csv")
            st.dataframe(df)
            st.success("✅ Loaded sample gene data successfully.")
        else:
            st.warning("⚠️ No sample data file (gene_data.csv) found.")

# ---- PREDICTIONS PAGE ----
elif page == "🔮 Predictions":
    sidebar_image()
    st.title("🔮 Prediction Results")
    if os.path.exists("inheritance_predictions.csv"):
        df = pd.read_csv("inheritance_predictions.csv")
        st.dataframe(df)
        st.success("✅ Predictions loaded from file.")
    else:
        st.warning("⚠️ No predictions found. Run the analysis first.")

# ---- VISUALS PAGE ----
elif page == "📊 Visuals":
    sidebar_image()
    st.title("📊 Gene Expression Visualizations")
    if os.path.exists("inheritance_predictions.csv"):
        df = pd.read_csv("inheritance_predictions.csv")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Gene Expression Comparison")
            fig, ax = plt.subplots()
            ax.bar(df["Gene"], df["Expression_A"], label="Person A", color="teal", alpha=0.7)
            ax.bar(df["Gene"], df["Expression_B"], label="Person B", color="orange", alpha=0.7)
            ax.set_xlabel("Genes")
            ax.set_ylabel("Expression Level")
            ax.legend()
            st.pyplot(fig)

        with col2:
            st.subheader("Disease Risk Distribution")
            risk_counts = df["Risk_Status"].value_counts()
            fig2, ax2 = plt.subplots()
            ax2.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%', startangle=90)
            st.pyplot(fig2)
    else:
        st.warning("⚠️ Please run the model first to generate visualization data.")

# ---- REPORTS PAGE ----
elif page == "📄 Reports":
    sidebar_image()
    st.title("📄 Reports & Summaries")
    if os.path.exists("summary_report.txt"):
        with open("summary_report.txt") as f:
            report_text = f.read()
        st.text_area("Summary Report", report_text, height=300)
        st.download_button("Download Report", report_text, file_name="summary_report.txt")
    else:
        st.warning("⚠️ No report found. Run full analysis first.")

# ---- SETTINGS PAGE ----
elif page == "⚙️ Settings":
    sidebar_image()
    st.title("⚙️ Dashboard Settings")
    st.markdown("""
    Customize display options, theme colors, and refresh intervals here.  
    (This section can be expanded with user preferences or saved settings.)
    """)
    theme = st.selectbox("Choose Theme", ["Light", "Dark", "Auto"])
    st.success(f"Theme set to: {theme}")
