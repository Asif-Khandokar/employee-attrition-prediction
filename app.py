import gradio as gr
import pandas as pd
import joblib

# Load model
model = joblib.load("attrition_model.pkl")


def predict_attrition(
    age,
    monthly_income,
    total_working_years,
    years_at_company,
    years_since_last_promotion,
    years_with_curr_manager,
    env_satisfaction,
    job_satisfaction,
    job_involvement,
    business_travel,
    department,
    education_field,
    gender,
    job_role,
    marital_status,
    overtime
):

    # Default values (medians from training data)
    data = {
        'Age': 36,
        'DailyRate': 802,
        'DistanceFromHome': 7,
        'Education': 3,
        'EnvironmentSatisfaction': 3,
        'HourlyRate': 66,
        'JobInvolvement': 3,
        'JobLevel': 2,
        'JobSatisfaction': 3,
        'MonthlyIncome': 4919,
        'MonthlyRate': 14235.5,
        'NumCompaniesWorked': 2,
        'PercentSalaryHike': 14,
        'PerformanceRating': 3,
        'RelationshipSatisfaction': 3,
        'StockOptionLevel': 1,
        'TotalWorkingYears': 10,
        'TrainingTimesLastYear': 3,
        'WorkLifeBalance': 3,
        'YearsAtCompany': 5,
        'YearsInCurrentRole': 3,
        'YearsSinceLastPromotion': 1,
        'YearsWithCurrManager': 3,

        'BusinessTravel_Travel_Frequently': 0,
        'BusinessTravel_Travel_Rarely': 0,

        'Department_Research & Development': 0,
        'Department_Sales': 0,

        'EducationField_Life Sciences': 0,
        'EducationField_Marketing': 0,
        'EducationField_Medical': 0,
        'EducationField_Other': 0,
        'EducationField_Technical Degree': 0,

        'Gender_Male': 0,

        'JobRole_Human Resources': 0,
        'JobRole_Laboratory Technician': 0,
        'JobRole_Manager': 0,
        'JobRole_Manufacturing Director': 0,
        'JobRole_Research Director': 0,
        'JobRole_Research Scientist': 0,
        'JobRole_Sales Executive': 0,
        'JobRole_Sales Representative': 0,

        'MaritalStatus_Married': 0,
        'MaritalStatus_Single': 0,

        'OverTime_Yes': 0
    }

    # User inputs
    data['Age'] = age
    data['MonthlyIncome'] = monthly_income
    data['TotalWorkingYears'] = total_working_years
    data['YearsAtCompany'] = years_at_company
    data['YearsSinceLastPromotion'] = years_since_last_promotion
    data['YearsWithCurrManager'] = years_with_curr_manager

    data['EnvironmentSatisfaction'] = env_satisfaction
    data['JobSatisfaction'] = job_satisfaction
    data['JobInvolvement'] = job_involvement

    # One-hot encoding
    if business_travel == "Travel_Frequently":
        data['BusinessTravel_Travel_Frequently'] = 1
    elif business_travel == "Travel_Rarely":
        data['BusinessTravel_Travel_Rarely'] = 1

    if department == "Research & Development":
        data['Department_Research & Development'] = 1
    elif department == "Sales":
        data['Department_Sales'] = 1

    if education_field != "Human Resources":
        data[f'EducationField_{education_field}'] = 1

    if gender == "Male":
        data['Gender_Male'] = 1

    if job_role != "Healthcare Representative":
        data[f'JobRole_{job_role}'] = 1

    if marital_status == "Married":
        data['MaritalStatus_Married'] = 1
    elif marital_status == "Single":
        data['MaritalStatus_Single'] = 1

    if overtime == "Yes":
        data['OverTime_Yes'] = 1

    # Create dataframe
    df_input = pd.DataFrame([data])

    # Match training column order
    df_input = df_input[model.feature_names_in_]

    # Predict probability
    probability = model.predict_proba(df_input)[0][1]

    # Risk assessment
    if probability >= 0.5:
        prediction = "Likely to Leave"
        risk = "High Risk 🔴"
        color = "red"

    elif probability >= 0.2:
        prediction = "Potential Attrition Risk"
        risk = "Medium Risk 🟡"
        color = "orange"

    else:
        prediction = "Likely to Stay"
        risk = "Low Risk 🟢"
        color = "green"

    # Recommendations
    if probability >= 0.5:
        recommendation = """
        <ul>
            <li>Career development discussions</li>
            <li>Promotion opportunities</li>
            <li>Workload review</li>
            <li>Employee engagement initiatives</li>
        </ul>
        """
    elif probability >= 0.2:
        recommendation = """
        Monitor employee satisfaction and engagement levels.
        Consider periodic manager check-ins.
        """
    else:
        recommendation = """
        No immediate retention action required.
        Continue maintaining employee satisfaction.
        """

    return f"""
    <div style="padding:20px;border-radius:12px;border:3px solid {color};background-color:#f8f9fa;">
        <h2 style="color:{color};">{prediction}</h2>
        <hr>
        <p><b>Attrition Probability:</b> {probability:.2%}</p>
        <p><b>Risk Level:</b> {risk}</p>
        <p><b>Recommendation:</b></p>
        {recommendation}
    </div>
    """


demo = gr.Interface(
    fn=predict_attrition,

    inputs=[
        gr.Number(label="Age"),
        gr.Number(label="Monthly Income"),
        gr.Number(label="Total Working Years"),
        gr.Number(label="Years At Company"),
        gr.Number(label="Years Since Last Promotion"),
        gr.Number(label="Years With Current Manager"),

        gr.Dropdown([1, 2, 3, 4], label="Environment Satisfaction"),
        gr.Dropdown([1, 2, 3, 4], label="Job Satisfaction"),
        gr.Dropdown([1, 2, 3, 4], label="Job Involvement"),

        gr.Dropdown(
            ["Travel_Rarely", "Travel_Frequently", "Non-Travel"],
            label="Business Travel"
        ),

        gr.Dropdown(
            ["Sales", "Research & Development", "Human Resources"],
            label="Department"
        ),

        gr.Dropdown(
            ["Life Sciences", "Medical", "Marketing",
             "Technical Degree", "Other", "Human Resources"],
            label="Education Field"
        ),

        gr.Dropdown(
            ["Male", "Female"],
            label="Gender"
        ),

        gr.Dropdown(
            [
                "Sales Executive",
                "Research Scientist",
                "Laboratory Technician",
                "Manufacturing Director",
                "Healthcare Representative",
                "Manager",
                "Sales Representative",
                "Research Director",
                "Human Resources"
            ],
            label="Job Role"
        ),

        gr.Dropdown(
            ["Single", "Married", "Divorced"],
            label="Marital Status"
        ),

        gr.Dropdown(
            ["Yes", "No"],
            label="OverTime"
        )
    ],

    outputs=gr.HTML(label="Prediction Result"),

    title="Employee Attrition Prediction System",

    description="""
    End-to-End Employee Attrition Prediction Application
    using Machine Learning, MLflow and Gradio.
    """
)

if __name__ == "__main__":
    demo.launch()