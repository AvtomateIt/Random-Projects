import streamlit as st
import numpy as np

st.write("""
         # How much does Jayzelle :red[love] Kuya Ryn?
         """)

if 'lives' not in st.session_state:
    st.session_state.lives = 10

lives = st.session_state.lives

love = st.slider(f"Lives remaining: {lives}", 0, 100)

if 'random_int' not in st.session_state:
    st.session_state.random_int = np.random.randint(0, 100)

if 'btn_lbl' not in st.session_state:
    st.session_state.btn_lbl = "Check Answer"

button_label = st.session_state.btn_lbl
correct = st.session_state.random_int

if lives != 0:
    st.session_state.btn_lbl = "Check Answer"
    if st.button(label = f"{button_label}"):
        if love == correct:
            st.balloons()
            st.success("Correct Answer! You won the game!", icon='💁🏻‍♀️')
            st.session_state.btn_lbl = "Start a new game!"
            st.session_state.lives = 10
            st.session_state.random_int = np.random.randint(0,100)
        if love < correct:
            st.error("Higher!", icon="⬆️")
            st.session_state.lives -= 1
        if love > correct:
            st.error("Lower!", icon="⬇️")
            st.session_state.lives -= 1
else:
    st.error(f"Game over! The correct answer is {correct}!", icon="🤦🏻‍♀️")
    if st.button(label = "Restart game?"):
        st.session_state.lives = 10
        st.session_state.random_int = np.random.randint(0,100)