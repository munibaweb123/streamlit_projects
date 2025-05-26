import streamlit as st

prompt = st.chat_input('Say something')
uploaded_file = st.file_uploader("Or upload an image", type=["jpg", "jpeg", "png"])


if 'data' not in st.session_state:
    st.session_state.data = []

if prompt:
    st.session_state["data"].append(prompt)

    for text in st.session_state.data:
        st.write(f'User has sent the following prompt: {text}')
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

st.write(st.session_state.data)