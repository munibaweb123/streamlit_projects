# https://docs.streamlit.io/library/api-reference/layout/st.columns

import streamlit as st

col1, col2, col3, col4 = st.columns(4)

# col1.header("aaaaa")
# in streamlit with helps group UI elements inside a layout component like a container, column, expander or even empty placeholders
with col1: # with is used for context management, 
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

with col4:
   st.header('A butterfly')
   st.image('https://th.bing.com/th/id/OIP.vmvIjBTRK0zsDQ1QF1jiXwHaLH?w=133&h=180&c=7&r=0&o=5&pid=1.7')