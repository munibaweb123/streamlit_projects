import streamlit as st
import time

with st.status("Processing...", expanded=True) as status:
    st.write("Step 1: Starting...")
    time.sleep(1)
    st.write("Step 2: Doing work...")
    time.sleep(1)
    st.write("Step 3: Finishing...")
    time.sleep(1)
    status.update(label="✅ Done!", state="complete")
