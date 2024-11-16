## 👋 Hi there!

<h1>❤️ Heart Disease Prediction Using Machine Learning</h1> 

<h2>🚀 Project Overview</h2>

Heart disease is a leading cause of mortality worldwide.
This project is a classification problem where the goal is to predict the likelihood of heart disease in patients based on various health indicators. It was part of my Final Year Project (FYP), aiming to apply machine learning techniques for early detection and prevention of heart disease. By leveraging multiple classification algorithms, this model helps in identifying high-risk patients and can be used by healthcare professionals to facilitate early diagnosis and intervention.

The key objective of this project is to build an accurate, reliable, and interpretable model for heart disease prediction that can potentially save lives through early identification.

<h2>🔎 Key Features</h2>

Algorithms: Used 5 different algorithms to predict heart disease risk:

- Decision Tree
- Random Forest
- Logistic Regression
- Gradient Boosted Trees
- Naïve Bayes

Preprocessing:

- Data cleaning: Handled missing values and outliers.
- SMOTE (Synthetic Minority Over-sampling Technique) used to handle imbalanced data.
- Feature scaling using StandardScaler.
Model Evaluation:

- Performance Metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC
- Confusion Matrix used for performance visualization.
  
<h2>🔧 Tech Stack</h2>

- Programming: Python
- Libraries: Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib,Skimpy,Streamlit

<h2>📊 Dataset</h2>
The dataset used for this project is from Kaggle and the target variable was HeartDiseaseorAttack
Link: https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset

<h2>🏗️ Workflow</h2>

Implemented CRISP-DM Methodology

- Step 1: Data Collection & Preprocessing
Cleaned and handled missing values using imputation and SMOTE.

- Step 2: Data Exploration
Performed exploratory data analysis (EDA) to understand correlations and the importance of features.

- Step 3: Model Building & Tuning
Trained 5 different algorithms and performed hyperparameter tuning for optimization.
Selected XGBOOST as the final model for deployment.

- Step 4: Evaluation & Model Selection
Used various metrics like ROC-AUC, Confusion Matrix, and F1-Score to evaluate model performance.

- Step 5 Deployment:
Deployed the model on a web-based application.

![image](https://github.com/user-attachments/assets/6bd928ec-8207-4ea4-aaba-a83647c5e1a0)

<h2>🏆 Model Evaluation Results</h2>

![image](https://github.com/user-attachments/assets/92e353ac-e9b4-4865-a066-5c9dc4d563ec)

**Key Takeaways**
- Random Forest and XGBoost performed consistently well before and after tuning, with XGBoost achieving the highest ROC-AUC and recall after tuning.
- Decision Tree showed improvements in Precision and F1-Score after tuning, although recall slightly decreased.
- Logistic Regression maintained a lower performance compared to tree-based models, but still provided solid results.
- Gaussian Naïve Bayes consistently underperformed in almost all metrics, highlighting its limitations in this classification problem.


<h2> 📈 Key Results</h2>

- The XGBoost Model was the best-performing model, with high accuracy (94.22%), precision (98%), and ROC-AUC score of 0.98.
- The model can predict heart disease risk with high reliability and can support early detection in healthcare systems.

<h2>🌟 Future Improvements</h2>

- Incorporating Diverse Data

  - Genomics and Imaging Data: Integrating genetic and medical imaging data could improve prediction accuracy.
  - Combining Multiple Datasets: Including lifestyle, environmental, and patient history data will provide a more comprehensive understanding.

- Ethical Framework Enhancement

  - Improved Privacy Policies: Strengthening data encryption and privacy regulations to protect patient information.
  - Bias Detection: Implementing algorithms to detect and mitigate biases in predictions.
  - Regular Audits: Ensuring the model is continuously audited for compliance and fairness.
    
- Real-Time Medical Knowledge Integration

  - Continuous Learning: Updating the model with the latest research and treatment guidelines in real-time.
  - Dynamic Updates: Ensuring the model adapts over time with new data from patients and clinical research.

- Health Organization Partnerships

  - Collaboration for Validation: Partnering with healthcare institutions for real-world testing and feedback.
  - Pilot Testing: Running live pilot tests to assess the model’s impact in clinical settings.

  <h2> 📸 Screenshot of Web-Based Application</h2>
  The screenshots below demonstrate the clean, intuitive design, allowing users to input patient data, view predictions, and explore relevant medical information directly through the app. The application also allows users to switch between English and Malay, ensuring 
  that healthcare professionals from diverse backgrounds can seamlessly interact with the system.

  **Screenshot 1**
    
  ![image](https://github.com/user-attachments/assets/85c66be3-164a-4a61-ab36-65e25b7872b3)

  **Screenshot 2**

  ![image](https://github.com/user-attachments/assets/d6da1cf4-cad2-424c-9bb9-d21f86d465c0)

  **Screenshot 3 (English)**
  
  ![image](https://github.com/user-attachments/assets/44769f0b-1473-48b0-b8ef-35edcaa400a5)

  **Screenshot 4 (Malay)**
  
  ![image](https://github.com/user-attachments/assets/47a670f4-257f-4d25-a1c7-01970ce0252a)

  **Screenshot 5 (Predictions)**
  
  ![image](https://github.com/user-attachments/assets/23dfe62e-e429-4dc5-a928-15ba59b0c3cf)

  **Screenshot 6 (Predictions)**
  
  ![image](https://github.com/user-attachments/assets/a1ad87a8-e5d5-4a2d-800f-a18f223d8ec5)





