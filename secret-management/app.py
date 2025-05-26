import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.subheader("🔐 Secrets and Environment Variable Check")

# Safe check before accessing secrets
if "db_username" in os.environ:
    st.write("✅ db_username found in .env:", os.environ["db_username"])
    match = os.getenv("db_username") == st.secrets["db_username"]
    st.success(f"✅ Match: {match}")
else:
    st.error("❌ Key 'db_username' not found in st.secrets. Please check secrets.toml.")
