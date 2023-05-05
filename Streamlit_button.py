import streamlit as st

st.header('Streamlit Button')

if st.button('say hello'):
    st.write('hello')
else:
    st.write('Why goodbye is here')