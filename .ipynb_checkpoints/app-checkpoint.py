import streamlit as st

st.title("Student Score Predictor")
name=st.text_input(
    "Enter name"
)
hours=st.slider(
    "Studey Hours",
    0,12
)

if st.button("predict"):
    score=hours*10

    st.success(
        f"{name}'s Predicted Score :{score}"
    )
    if score>70:
        st.balloons()