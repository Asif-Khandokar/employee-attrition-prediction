# Employee Attrition Analytics & Prediction Platform

## Overview

This project predicts employee attrition using Machine Learning and HR Analytics techniques. The goal is to identify employees at risk of leaving the organization and provide actionable insights for retention strategies.

The project covers the complete Machine Learning lifecycle including data preprocessing, model training, evaluation, experiment tracking, web application development, and deployment.

---

## Features

* Employee Attrition Prediction
* Data Preprocessing & Feature Engineering
* Logistic Regression Model
* Cross Validation
* Hyperparameter Tuning (GridSearchCV)
* Threshold Optimization
* MLflow Experiment Tracking
* Gradio Web Application
* Hugging Face Deployment

---

## Dataset

Dataset: IBM HR Analytics Employee Attrition Dataset

Target Variable:

* Attrition (Yes/No)

Problem Type:

* Binary Classification

---

## Machine Learning Workflow

### Data Preprocessing

* Missing Value Check
* Label Encoding
* One-Hot Encoding
* Feature Scaling
* Train-Test Split

### Models Evaluated

* Logistic Regression
* Random Forest
* XGBoost

### Model Selection

The final selected model was Logistic Regression with threshold tuning because it achieved the highest Recall, which is critical for identifying employees likely to leave.

---

## Final Model Performance

| Model                                 | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------------------------------- | -------- | --------- | ------ | -------- | ------- |
| Logistic Regression (Threshold = 0.2) | 0.81     | 0.43      | 0.64   | 0.51     | 0.81    |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* MLflow
* Gradio
* Hugging Face Spaces
* Joblib

---

## Deployment

### Hugging Face Space

Live Application:

https://asifkhandokar-employee-attrition-prediction.hf.space

---

## Repository Structure

```text
employee-attrition-prediction/
│
├── app.py
├── attrition_model.pkl
├── requirements.txt
├── Employee_Attrition_Analytics_&_Prediction_Platform.ipynb
└── README.md
```

---

## Author

**Asif Khandokar**

GitHub:
https://github.com/Asif-Khandokar

Hugging Face:
https://huggingface.co/AsifKhandokar
