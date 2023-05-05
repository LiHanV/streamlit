import streamlit as st
import pandas as pd

st.header('st.write')
st.header('Display text')
st.write('Hello,*World!* :sunglasses:')

st.header('Display numbers')

st.write(1234)

st.header('Display DataFrame')

df = pd.DataFrame({
    'First column':[1, 2, 3, 4],
    'Second column':[10, 20, 30, 40]
})
st.write('Below is a DataFrame', df, 'Above is a DataFrame')


