import streamlit as st
import numpy as np

with st.chat_message('user'):
    st.write('Hi everyone 👋')
    st.line_chart(np.random.randn(30, 3))

with st.chat_message('assistant'):
    st.write('Hi there! How can I help')

user_input = st.chat_input('Type your message...')
if user_input:
    st.write(f'You said: {user_input}')