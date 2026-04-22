import streamlit as st
import requests

st.title("calculator using API")

a = st.number_input("ENTER A")
b = st.number_input("ENTER B")

if st.button("add"):
    res = requests.get(f"http://127.0.0.1:8000/add?a={a}&b={b}")
    st.write(res.json())
if st.button("mul"):
    res = requests.get(f"http://127.0.0.1:8000/mul?a={a}&b={b}")
    st.write(res.json())
if st.button("sub"):
    res = requests.get(f"http://127.0.0.1:8000/sub?a={a}&b={b}")
    st.write(res.json())
if st.button("div"):
    res = requests.get(f"http://127.0.0.1:8000/div?a={a}&b={b}")
    st.write(res.json())