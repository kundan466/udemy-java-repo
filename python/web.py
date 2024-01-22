import streamlit as st
st.title("My todo app")
st.subheader("This is my todo app")
st.write("ThIS app  is to increase your productivity")

todos=["Do the laundry","Return the books to library","Fix the fllor"]

for i in todos:
    st.checkbox(i)

st.text_input(label=" ",placeholder="Add a new todo")