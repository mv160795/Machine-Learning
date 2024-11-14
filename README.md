**OVERVIEW**                                      
The objective of this project is to build a predictive model that can determine whether a loan application will be approved (loan_status = 1) or denied (loan_status = 0). The model is trained using historical data that includes personal, financial, and loan-related details of applicants.

**KEY FEATURES :**      
**Column Transformer :** Powerful tool to apply different preprocessing steps on subsets of features (columns) in dataset.                          
**Pipeline :** It is a way to streamline machine learning workflows by chaining multiple steps, such as preprocessing and model training, into a single object.      

**DATASET**                                       
The dataset contains 14 columns and 45,000 rows with the following features:                  

**Columns:**                                      
person_age , person_gender , person_education , person_income , person_emp_exp , person_home_ownership , loan_amnt , loan_intent , loan_int_rate , loan_percent_income , cb_person_cred_hist_length , credit_score , previous_loan_defaults_on_file , loan_status                                                          

**LIBRARIES**                               
This project uses the following Python libraries:       
Pandas: For data manipulation and analysis.                      
NumPy: For numerical operations on arrays.                          
Scikit-learn (Sklearn): For building and evaluating machine learning models.              
Matplotlib: For data visualization and plotting.              
Seaborn: For creating informative and attractive statistical graphics.                  

**FILES**                          
**Raw data**                         ---> loan_data.csv                          
**Classification**                   ---> classification.ipynb                      
**Data import and Preprocessing**    ---> data_import.py                   

**MODELS**   
**Classification Models : **
**Target:**  --->   loan_status                         
1. K-Nearest Neighbors (KNN)                        
2. Naive Bayes                        
3. Logistic Regression                   
4. Random Forest                      
5. Logistic                   
                      
**Performance Metrics**                               
**Accuracy:** The proportion of correct predictions made by the model.                   
**Confusion Matrix:** A table used to evaluate the classification performance by comparing the predicted and actual values.                   
**ROC Curve:** A graphical representation of the model's ability to distinguish between classes (approved vs denied).                    
**Precision-Recall Curve:** A curve to evaluate the precision and recall of the model at different thresholds.     



