import streamlit as st



# Access API key
openai_key = st.secrets["api_keys"]["openai"] #like nested dictionary
# first we access the section api_keys and then the key openai
weather_key = st.secrets["api_keys"]["weather"]
# same as above

# Access database credentials
db_user = st.secrets["database"]["user"]
db_password = st.secrets["database"]["password"]
db_host = st.secrets["database"]["host"]


st.write("OpenAI Key:", openai_key)
st.write("Database User:", db_user)
st.write("Database Password:", db_password)
st.write("Database Host:", db_host)
st.write("weather api key:", weather_key)


