import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import streamlit as st
import numpy as np
import urllib
from PIL import Image

urllib.request.urlretrieve("https://www.niddk.nih.gov/-/media/Images/Health-Information/Diabetes/diabetes-monitor-fruits-vegetables-small_597x347.png", "car_sample1.png")
img = Image.open("car_sample1.png").convert('RGB')
img = img.resize((700,400))
st.image(img)

url = "https://raw.githubusercontent.com/joeyaj1302/datasets/master/diabetes.csv"
data = pd.read_csv(url, error_bad_lines=False)

st.title("Diabetes Predicton by machine learning")

st.header("Choose the parameters like age , BMI, Glucose , etc")

# Storing the default mean values in a dictionary:

#defining the inputs and outputs
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
reg = LogisticRegression()
reg.fit(x,y)
#taking input data from users

Pregnancies= 0
SkinThickness = 20
DiabetesPedigreeFunction = 0.47
Age = st.slider("select your age from the slider :",  25, 100)
BloodPressure = st.slider("Select your diastolic blood pressure from the slider :" ,60, 122)
BMI = st.slider("Select your BMI from the slider :" ,20, 50)
Insulin = st.slider("Select your insulin level from the slider :" ,30, 800)
Glucose = st.slider("Select your Blood glucose level from the slider :" ,80, 200)
if st.checkbox("Do you want to input other related data like pregnancy,skin thickness and DiabetesPedigreeFunction ?"):
    Pregnancies = st.sidebar.selectbox("Select the number of Pregnancies you had from the drop down box :",[1,2,3,4,5,6])
    SkinThickness = st.sidebar.slider("Select your skin thickness in mm :",1.5,9.9)*10
    DiabetesPedigreeFunction = st.sidebar.slider("Select your tested DiabetesPedigreeFunction :",0.07,2.42)

x1 = np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

#st.write(x1)

#st.write(Age,BMI,Insulin,BloodPressure,Glucose)

preds = reg.predict(x1)

if preds == 1:
    st.header("You are more prone to diabetes")
else:
    st.header("You are probably safe from diabetes")


