Overview
This project aims to predict whether a customer is likely to churn based on their demographic and service usage data. The goal is to identify high-risk customers and help businesses improve retention strategies.

Dataset
Thae dataset contains customer related information such as 
- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Internet Service
- Payment Method

Exploratory Data Analysis
EDA revelaed key insights about the relation of churn rate with different parameters like Tenure and Monthly Charges

Models used
- Logistic Regression
- Random Forest Classifier
- K Neighbors Classifier

Model Evaluation
Used Evaluation Metric Recall
Logistic Regression performed best with recall of 0.69

Turned it into a Flask-based web application which takes user inputs and display the results

Tech Stack
- Python
- Numpy/Pandas
- Scikit-Learn
- Flask
- HTML/CSS
