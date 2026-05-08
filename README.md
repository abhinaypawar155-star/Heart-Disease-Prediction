# Heart Disease Risk Prediction using Machine Learning
📌 Project Overview

This project aims to predict the likelihood of heart disease using Machine Learning algorithms based on clinical and medical attributes of patients.

# The project includes:
Data preprocessing
Exploratory Data Analysis (EDA)
Feature scaling
Model training & evaluation
Model comparison
Streamlit deployment
📂 Dataset Information

# The dataset contains medical attributes such as:
Age
Sex
Chest Pain Type
Blood Pressure
Cholesterol
Heart Rate
Exercise Induced Angina
Oldpeak
Number of Major Vessels
Thalassemia

# Target Variable
1 → Heart Disease Present
0 → No Heart Disease

# 🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
XGBoost
Streamlit
Pickle
# 📊 Exploratory Data Analysis (EDA)

# Performed:

Distribution plots
Boxplots
Correlation heatmap
Target variable analysis
Key Insights
Cholesterol and oldpeak contain outliers
Chest pain type and maximum heart rate strongly influence prediction
Dataset is relatively balanced
⚙️ Data Preprocessing

# Steps performed:

Checked missing values
Train-test split
Feature scaling using StandardScaler
🤖 Machine Learning Models Used
Logistic Regression
Random Forest Classifier
XGBoost Classifier
K-Nearest Neighbors (KNN)
📈 Model Performance
Model	Accuracy
Logistic Regression	81.32%
Random Forest	83.52%
XGBoost	81.32%
KNN	86.81%
Best Performing Model

✅ K-Nearest Neighbors (KNN)

🔍 Evaluation Metrics

Models were evaluated using:

Accuracy Score
Precision
Recall
F1-Score
Confusion Matrix
Cross Validation
💾 Model Saving

The final trained model and scaler were saved using pickle.

pickle.dump(model, open('best_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))
🌐 Streamlit Deployment

A simple Streamlit web application was created where users can:

Enter patient details
Predict heart disease risk in real time
Run the App
streamlit run app.py
🚀 Project Workflow
Data Collection
Data Cleaning
Exploratory Data Analysis
Feature Scaling
Model Training
Model Evaluation
Model Comparison
Model Saving
Streamlit Deployment
📌 Conclusion

This project demonstrates how Machine Learning can be used in healthcare for early prediction of heart disease. Multiple models were compared, and KNN achieved the best performance with an accuracy of approximately 86.8%.
