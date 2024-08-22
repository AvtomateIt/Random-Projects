import streamlit as st
import numpy as np

st.write("""
         # How much does Jayzelle :red[love] Kuya Ryn?
         """)

if 'lives' not in st.session_state:
    st.session_state.lives = 10

lives = st.session_state.lives

st.write(f"Lives remaining: {lives}")

love = st.slider("Choose a number.", 0, 100, 50)

if 'random_int' not in st.session_state:
    st.session_state.random_int = np.random.randint(0, 100)

if 'btn_lbl' not in st.session_state:
    st.session_state.btn_lbl = "Check Answer"

button_label = st.session_state.btn_lbl
correct = st.session_state.random_int

@st.dialog("You got a highscore!")
def highscore_name(lives):
    name = st.text_input("Name")
    message = st.text_input("Short Message")
    if st.button("Submit"):
        st.session_state.top = {"Name": name, "Lives": lives, "Message": message}
        st.rerun()

if lives != 0:
    st.session_state.btn_lbl = "Check Answer"
    if st.button(label = f"{button_label}"):
        if love == correct:
            st.balloons()
            st.success("Correct Answer! You won the game!", icon='💁🏻‍♀️')

            if "top" not in st.session_state:
                highscore_name(lives)
            else:
                if lives > st.session_state.top['Lives']:
                    highscore_name(lives)

            st.session_state.btn_lbl = "Start a new game!"
            st.session_state.lives = 10
            st.session_state.random_int = np.random.randint(0,100)
        if love < correct:
            st.info("Higher!", icon="⬆️")
            st.session_state.lives -= 1
        if love > correct:
            st.info("Lower!", icon="⬇️")
            st.session_state.lives -= 1
else:
    st.error(f"Game over! The correct answer is {correct}!", icon="🤦🏻‍♀️")
    if st.button(label = "Restart game?"):
        st.session_state.lives = 10
        st.session_state.random_int = np.random.randint(0,100)

if "top" in st.session_state:
    st.write("""
    ### :rainbow[Top Scorer]
    """)
    st.write(f"{st.session_state.top['Name']}, lives remaining: {st.session_state.top['Lives']}, message: {st.session_state.top['Message']}")