import streamlit as st
import pandas as pd
import time

st.title("📄 CSV Uploader with Status")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    with st.status("Reading file...", expanded=True) as status:
        time.sleep(1)
        df = pd.read_csv(uploaded_file)
        st.write("✅ File read successfully!")

        st.write("🔍 Cleaning data...")
        time.sleep(1)
        # Simulate cleaning
        df.dropna(inplace=True) # save this in same data frame not new
        st.write("✅ Missing values removed") # NaN values remove

        st.write("🧪 Doing analysis...")
        time.sleep(1)
        mean_values = df.mean(numeric_only=True)

        status.update(label="🎉 Processing Complete!", state="complete")

    st.subheader("📊 Cleaned Data")
    st.dataframe(df)

    st.subheader("📈 Mean of Numeric Columns")
    st.write(mean_values)
