import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Data Analytics Dashboard", page_icon="📊", layout="wide")

st.title("📊 Smart Data Analytics Dashboard")
st.write("Upload your CSV or Excel file below to generate an instant exploratory data analysis report.")

# 1. File Upload
uploaded_file = st.file_uploader("Choose a file (CSV or Excel):", type=["csv", "xlsx"])

if uploaded_file is not None:
    # 2. Read File Based on Extension
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        st.success("File uploaded successfully!")
        
        # 3. Key Metrics Overview
        col1, col2 = st.columns(2)
        col1.metric("Total Rows", df.shape[0])
        col2.metric("Total Columns", df.shape[1])
        
        st.divider()
        
        # 4. Data Preview
        st.subheader("📋 Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)
        
        # 5. Descriptive Statistics
        st.subheader("📈 Summary Statistics")
        st.dataframe(df.describe(), use_container_width=True)
        
        st.divider()
        
        # 6. Interactive Visualization
        st.subheader("📊 Data Visualization")
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        
        if len(numeric_columns) > 0:
            selected_col = st.selectbox("Select a numerical column to plot:", numeric_columns)
            st.bar_chart(df[selected_col])
        else:
            st.info("No numerical columns found in the uploaded dataset for plotting.")
            
    except Exception as e:
        st.error(f"Error processing the file: {e}")
else:
    st.info("Please upload a CSV or Excel file to get started.")