# 🧓 NHANES Age Group Prediction Web Application

---

## 🚀 Project Overview

This project was developed as part of the **Summer Analytics 2025 Hackathon** hosted by the **Consulting and Analytics Club, IIT Guwahati**. The core objective was to build a machine learning model that can accurately classify individuals into two age groups: **Seniors (65 years and above)** and **Adults** — using health, lifestyle, and lab test data.

The foundation of this work lies in the **National Health and Nutrition Examination Survey (NHANES)** — a comprehensive and nationally representative dataset collected by the CDC. NHANES uniquely combines interviews, physical examinations, and laboratory tests to provide a holistic view of health trends in the United States.

This project leverages a focused subset of NHANES data to design an intuitive and powerful predictive system that can identify senior age group status with remarkable accuracy.                  

---

## 📊 Dataset Details

The dataset comprises **6,287 entries** and includes **7 key features**, each carefully selected for their relevance to health and aging:

| Feature  | Description                   |
| -------- | ----------------------------- |
| RIDAGEYR | Age in Years                  |
| RIAGENDR | Gender (1 = Male, 2 = Female) |
| PAQ605   | Physical Activity Level       |
| BMXBMI   | Body Mass Index (BMI)         |
| LBXGLU   | Blood Glucose Level           |
| DIQ010   | Diabetes Status Indicator     |
| LBXGLT   | Glucose Tolerance             |
| LBXIN    | Insulin Level                 |

The **target variable** distinguishes between **Adults** and **Seniors (65+)** based on the `age_group` label.

---

## 🎯 Project Objective

The goal was to create a **robust, reliable classification model** that predicts whether an individual belongs to the senior age group based on physiological and behavioral data. Such a model could have significant implications for public health, enabling:

* Early identification of aging-related health risks
* Better-targeted healthcare interventions
* Data-driven policy formulation for aging populations

---

## 🛠 Methodology

### Data Preprocessing

* **Cleaning:** Removed unique identifiers and handled missing values by imputing median values to maintain data integrity.
* **Encoding:** Converted age group labels into binary form: `Adult = 0`, `Senior = 1`.
* **Stratified Splitting:** Data was split into training (80%) and testing (20%) sets to ensure balanced class distribution.

### Model Selection & Training

* Used a **Random Forest Classifier**, well-known for its robustness, interpretability, and performance on structured data.
* Set to 100 decision trees to strike an optimal balance between bias and variance.
* Trained on the processed dataset with hyperparameters chosen for stability.

---

## 📈 Evaluation & Performance

The model demonstrated **exceptional accuracy and generalization**:

| Metric   | Training Set | Testing Set |
| -------- | ------------ | ----------- |
| Accuracy | 100%         | 100%        |
| F1 Score | 1.000        | 1.000       |

* **Confusion Matrix** shows perfect classification without false positives or negatives.
* These results underscore the model’s potential effectiveness in real-world health predictions.

---

## 🖥 Web Application Overview

To make this solution accessible, an **interactive web application** was developed using **Streamlit**:

### Features:

* **🏃 Individual Prediction**
  Users manually enter personal health data to instantly predict if they belong to the senior age group. The form includes intuitive labels and value ranges to minimize confusion.

* **📂 Batch Prediction**
  Users can upload a CSV file containing multiple records for bulk prediction, with the results displayed immediately and downloadable for further analysis.

### User Interface Highlights:

* Clear, welcoming home screen with concise instructions
* Sidebar navigation with options always expanded for ease of use
* Visual feedback on prediction results
* Informative tooltips and data descriptions to guide users

---

### 📸 App Preview

**Home Screen**  
![image](https://github.com/user-attachments/assets/3edfca85-ce02-487d-9152-4eb65d1a0e86)

**Individual Prediction**  
![image](https://github.com/user-attachments/assets/e7511e3c-339c-4956-a062-18dfcc48ef0c)

**Batch Prediction**  
![image](https://github.com/user-attachments/assets/8574e010-46b2-4403-aa50-28b943447cc2)

---

## 💡 Impact & Significance

This project exemplifies the power of **health data analytics** in transforming raw data into actionable insights:

* Supports **public health initiatives** aimed at senior care
* Demonstrates effective use of **machine learning in healthcare**
* Enhances understanding of how key health indicators relate to aging

By participating in this hackathon, I strengthened my skills in **data preprocessing, machine learning modeling, and user-centric application design**, delivering a solution that is both practical and impactful.

---

## 🔮 Future Work & Enhancements

* Integrate **explainability** modules to interpret individual predictions and feature contributions.
* Expand dataset features with more NHANES variables for richer insights.
* Experiment with advanced algorithms (e.g., Gradient Boosting, Neural Networks) for enhanced accuracy.
* Optimize the web app for scalability and real-time analytics.
* Incorporate **visual analytics dashboards** for exploratory data analysis within the app.

---

## 🤝 Acknowledgments

* **CDC & NHANES** for the comprehensive dataset enabling this research.
* **Consulting and Analytics Club, IIT Guwahati** for organizing the inspiring Summer Analytics 2025 Hackathon.
* Open-source libraries and frameworks, including **Streamlit** and **scikit-learn**, which powered development.

---

## 🌐 Explore the Live App

Try the fully functional web app hosted on Streamlit Cloud:
👉 [https://agepredictionapp.streamlit.app/](https://agepredictionapp.streamlit.app/)

Thank you for exploring the **NHANES Age Group Prediction** project!  
