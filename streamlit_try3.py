import streamlit as st

st.write("""
         # How much does Jayzelle love Kuya Ryn?
         """)

love = st.slider("", 0, 100)

if st.button("Check Answer"):
    if love == 100:
        st.balloons()
        st.success("Correct Answer!")
    else:
        st.error("Wrong Answer. Try Again!")