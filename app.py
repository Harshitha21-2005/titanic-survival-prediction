import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# Load cleaned data
df = pd.read_csv('data/cleaned_titanic.csv')

X = df.drop('Survived', axis=1)
y = df['Survived']

# Train final model (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
st.title("🚢 Titanic Survival Prediction")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 1, 80, 30)
sibsp = st.number_input("Siblings/Spouses", 0, 5, 0)
parch = st.number_input("Parents/Children", 0, 5, 0)
fare = st.slider("Fare", 0, 500, 50)
embarked = st.selectbox("Embarked", ["S", "C", "Q"])
title = st.selectbox("Title", ["Mr", "Miss", "Mrs", "Master", "Rare"])
sex = 0 if sex == "Male" else 1
embarked = {"S": 0, "C": 1, "Q": 2}[embarked]
title = {"Mr":1, "Miss":2, "Mrs":3, "Master":4, "Rare":5}[title]
family_size = sibsp + parch + 1
input_data = [[
    pclass, sex, age, sibsp, parch, fare, embarked, family_size, title
]]

if st.button("Predict Survival"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("Passenger Survived")
    else:
        st.error("Passenger Did Not Survive")
        
# FILTERING 

st.subheader("🔍 Filter Passenger Predictions")

filter_class = st.selectbox("Filter by Class", ["All", 1, 2, 3])
filter_gender = st.selectbox("Filter by Gender", ["All", "Male", "Female"])

filtered_df = df.copy()

if filter_class != "All":
    filtered_df = filtered_df[filtered_df['Pclass'] == filter_class]

if filter_gender != "All":
    filtered_df = filtered_df[
        filtered_df['Sex'] == (0 if filter_gender == "Male" else 1)
    ]

st.dataframe(filtered_df.head(20))
