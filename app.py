import streamlit as st
import pickle

st.set_page_config(
    page_title="student Score Predictor",
    page_icon="🎓",
    layout="centered"
)
model=pickle.load(open("model.pkl","rb"))

st.title("👨‍🎓 Student Score Predictor")
st.write("Predict student marks using Machine Learning🎓🤖")
name=st.text_input(
    "Enter name"
)
Hours=st.number_input(
    "Enter study hours📚"
)

if st.button("predict score"):
    prediction=model.predict([[Hours]])
    
    st.success(
        f"{name}'s Predicted Score :{prediction[0]}"
    )
    if prediction[0]>80:
        st.balloons()
        st.write("Excellent Performance!✨")
    elif prediction[0]>50:
        st.write("Good job!👍")
    else:
        st.write("Need More Practice!📖")


        #st.markdown("""
#     <style>
#             .main{
#             background-color:#0E1117:
#             }
#             h1{
#                 color:#00FFD1;
#                 text-align:center;
#             }
#             .stButton>button{
#             background-color:#00FFD1:
#             color:black;
#             border-radius:10px;
#             height:3em;
#             width:100%;
#             font-size:18px;
#             }
#             </style>
# """,unsafe_allow_html=True)
