# Titanic Survival Prediction 

## Project Description
The RMS Titanic sank in 1912, resulting in the loss of many lives.  
In this project, I built a Machine Learning model to predict whether a passenger survived or not based on their personal and travel details such as age, gender, class, fare, and family size.

This project helped me understand how Machine Learning can be applied to real-world data for prediction tasks.

## Objective
The main objective of this project is:
- To train a Machine Learning model that predicts passenger survival
- To analyze passenger data using Exploratory Data Analysis (EDA)
- To build a simple web application for real-time prediction using Streamlit

##  Dataset Used
- Dataset Name: Titanic Dataset
- Source: Kaggle
- Total Records: 891 passengers
- Target Variable: `Survived`
  - 0 → Did Not Survive  
  - 1 → Survived  

##  Technologies and Tools Used
- Python
- Pandas and NumPy for data processing
- Matplotlib and Seaborn for data visualization
- Scikit-learn for Machine Learning
- Streamlit for web application

## Project Workflow

### 1. Data Cleaning
- I handled missing values in the Age and Embarked columns.
- I removed the Cabin column due to a large number of missing values.
- I converted categorical data into numerical format.

### 2. Feature Engineering
- I created a new feature called `FamilySize`.
- I extracted passenger titles such as Mr, Mrs, Miss from the Name column.
- These features helped improve the model’s prediction accuracy.

### 3. Exploratory Data Analysis (EDA)
- I analyzed survival trends based on gender, class, and age.
- I observed that female passengers and first-class passengers had higher survival rates.
- Visualizations were created to understand data patterns.

### 4. Model Training
- I trained two Machine Learning models:
  - Logistic Regression
  - Random Forest Classifier
- Random Forest gave better accuracy, so I selected it as the final model.

### 5. Model Evaluation
- I evaluated the models using accuracy score and confusion matrix.
- Random Forest achieved higher accuracy compared to Logistic Regression.

### 6. Streamlit Web Application
- I developed a Streamlit application where users can enter passenger details.
- The app predicts whether the passenger survived or not.
- This makes the project interactive and user-friendly.

## Machine Learning Models Used
- Logistic Regression
- Random Forest Classifier (Final Model)

## How to Run the Project
### Step 1: Install required libraries
### Step 2: Run the Streamlit application
    -streamlit run app.py

## Project Structure
titanic-survival-prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── train.csv
│   └── cleaned_titanic.csv
├── notebooks/
    ├── EDA.ipynb
    └── Model_Building.ipynb
