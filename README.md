**Loan Status Prediction**                              
This repository contains a machine learning project aimed at predicting whether a loan applicant will be approved or not based on various features such as age, work experience, loan amount, credit score, and more.

**Problem Overview**                                      
The objective of this project is to build a predictive model that can determine whether a loan application will be approved (loan_status = 1) or denied (loan_status = 0). The model is trained using historical data that includes personal, financial, and loan-related details of applicants.

**Dataset**                                       
The dataset contains 14 columns and 45,000 rows with the following features:                  

**Columns:**                                      
person_age , person_gender , person_education , person_income , person_emp_exp , person_home_ownership , loan_amnt , loan_intent , loan_int_rate , loan_percent_income , cb_person_cred_hist_length , credit_score , previous_loan_defaults_on_file , loan_status                             

**Target:**                        
loan_status   --->  This is the target variable, where 1 indicates loan approval, and 0 indicates denial.                              

**Libraries**                              
This project uses the following Python libraries:

Pandas: For data manipulation and analysis.                      
NumPy: For numerical operations on arrays.                          
Scikit-learn (Sklearn): For building and evaluating machine learning models.              
Matplotlib: For data visualization and plotting.              
Seaborn: For creating informative and attractive statistical graphics.                  
                     
**Models**                             
K-Nearest Neighbors (KNN)                        
Naive Bayes                        
Logistic Regression                   
Random Forest                      
Logistic                   
                      
**Performance Metrics**                               
**Accuracy:** The proportion of correct predictions made by the model.                   
**Confusion Matrix:** A table used to evaluate the classification performance by comparing the predicted and actual values.                   
**ROC Curve:** A graphical representation of the model's ability to distinguish between classes (approved vs denied).                    
**Precision-Recall Curve:** A curve to evaluate the precision and recall of the model at different thresholds.         

