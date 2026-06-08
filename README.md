# Employee Attrition Analytics & Prediction Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-blue)
![Gradio](https://img.shields.io/badge/Gradio-Web%20Application-green)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Deployed-yellow)

---

# Overview

Employee attrition is a major challenge for organizations due to the costs associated with recruitment, onboarding, training, and productivity loss.

This project develops an end-to-end Machine Learning solution to predict employee attrition using HR analytics data. The objective is to identify employees at risk of leaving the organization and provide actionable insights to support employee retention strategies.

The project covers the complete Machine Learning lifecycle including:

* Data Preprocessing
* Feature Engineering
* Model Training
* Cross Validation
* Hyperparameter Tuning
* Threshold Optimization
* MLflow Experiment Tracking
* Gradio Application Development
* Hugging Face Deployment

---

# Live Demo

### Hugging Face Application

🔗 https://asifkhandokar-employee-attrition-prediction.hf.space

### GitHub Repository

🔗 https://github.com/Asif-Khandokar/employee-attrition-prediction

---

# Problem Statement

Predict whether an employee is likely to leave the organization using demographic, compensation, satisfaction, and employment-related features.

### Target Variable

**Attrition**

* Yes = Employee left the company
* No = Employee stayed in the company

### Machine Learning Task

**Binary Classification**

---

# Dataset

Dataset Used:

**IBM HR Analytics Employee Attrition Dataset**

The dataset contains employee information including:

* Age
* Monthly Income
* Job Satisfaction
* Environment Satisfaction
* Overtime
* Business Travel
* Job Role
* Marital Status
* Years At Company
* Total Working Years

and other HR-related features.

---

# Project Architecture

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Cross Validation
   ↓
Hyperparameter Tuning
   ↓
Threshold Optimization
   ↓
MLflow Tracking
   ↓
Model Serialization
   ↓
Gradio Web Application
   ↓
Hugging Face Deployment
```

# Data Preprocessing

The following preprocessing steps were performed:

* Missing Value Analysis
* One-Hot Encoding
* Feature Scaling using StandardScaler
* Train-Test Split
* Feature Selection

### Why StandardScaler?

Features such as Monthly Income and Age exist on different scales. Standardization ensures all features contribute fairly during model training.

### Why One-Hot Encoding?

Machine Learning models cannot process categorical text directly. One-Hot Encoding converts categories into numerical binary representations.

---

# Models Evaluated

The following Machine Learning algorithms were evaluated:

### Logistic Regression

* Interpretable
* Fast training
* Probability outputs
* Easy deployment

### Random Forest

* Ensemble learning
* Handles non-linear relationships

### XGBoost

* Gradient boosting algorithm
* Strong predictive performance

---

# Model Selection

The final selected model was:

## Logistic Regression

Although Random Forest and XGBoost achieved competitive performance, Logistic Regression was selected because:

* Highest Recall after threshold tuning
* Strong interpretability
* Probability-based predictions
* Easier deployment and maintenance

Since the business objective was identifying employees likely to leave, Recall was prioritized over Accuracy.

---

# Cross Validation

To evaluate model robustness, 5-Fold Cross Validation was performed.

Benefits:

* Reduces overfitting risk
* Provides more reliable performance estimates
* Evaluates model stability across multiple data splits

---

# Hyperparameter Tuning

GridSearchCV was used to optimize model performance.

Parameters were systematically tested and evaluated using Cross Validation.

Best Parameter:

```text
C = 10
```

---

# Threshold Optimization

The default Logistic Regression classification threshold is:

```text
0.5
```

However, the primary business objective was maximizing employee-risk detection.

The threshold was optimized to:

```text
0.2
```

Result:

| Threshold | Recall |
| --------- | ------ |
| 0.5       | 0.34   |
| 0.2       | 0.64   |

This nearly doubled the model's ability to identify employees likely to leave.

---

# Final Model Performance

| Model                                 | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------------------------------- | -------- | --------- | ------ | -------- | ------- |
| Logistic Regression (Threshold = 0.2) | 0.81     | 0.43      | 0.64   | 0.51     | 0.81    |

### Business Interpretation

The model successfully identifies approximately 64% of employees who are likely to leave the organization, enabling proactive retention strategies.

---

# Key Business Insights

Analysis revealed several important attrition drivers:

### Factors Increasing Attrition Risk

* Overtime
* Frequent Business Travel
* Sales Representative Roles
* Laboratory Technician Roles
* Longer Time Since Last Promotion

### Factors Reducing Attrition Risk

* Higher Job Satisfaction
* Higher Environment Satisfaction
* Longer Total Working Experience
* Stronger Manager Relationships

These findings can support HR decision-making and employee retention programs.

---

# MLflow Experiment Tracking

MLflow was integrated for experiment management.

Tracked Components:

* Parameters
* Metrics
* Model Runs
* Experiment History

Benefits:

* Reproducibility
* Performance comparison
* Model management

---

# Web Application

An interactive Gradio web application was developed to allow users to:

* Enter employee information
* Predict attrition risk
* View attrition probability
* Receive risk-based recommendations

---

# Deployment

The application was deployed using:

### Hugging Face Spaces

Deployment Files:

```text
app.py
attrition_model.pkl
requirements.txt
```

The deployed application provides real-time employee attrition predictions through a public web interface.

---

# Repository Structure

```text
employee-attrition-prediction/
│
├── app.py
├── attrition_model.pkl
├── requirements.txt
├── Employee_Attrition_Analytics_&_Prediction_Platform.ipynb
├── README.md
└── screenshots/
```

---

# Future Enhancements

Potential future improvements include:

* SHAP Explainability
* SMOTE for Class Imbalance Handling
* Docker Containerization
* CI/CD Pipeline Integration
* Real-Time Monitoring Dashboard
* Model Drift Detection

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* MLflow
* Joblib
* Gradio
* Hugging Face Spaces
* GitHub

---

# Author

## Asif Khandokar

GitHub:
https://github.com/Asif-Khandokar

Hugging Face:
https://huggingface.co/AsifKhandokar

---

### If you found this project interesting, feel free to explore the repository, try the live demo, or connect with me on GitHub.
