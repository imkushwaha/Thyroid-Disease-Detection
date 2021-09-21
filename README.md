# Thyroid Disease Detection

Thyroid disease a very common problem in India, more than one crore people are suffering with the disease every year. Thyroid disorder can speed up or slow down the metabolism of the body.

The main objective of this project is to predict if a person is having compensated hypothyroid, primary hypothyroid, secondary hypothyroid or negative (no thyroid) with the help of Machine Learning. Classification algorithms such as Random Forest, XGBoost and KNN Model have been trained on the thyroid dataset, UCI Machine Learning repository. After hyperparameter tuning XGBoost model has performed well with better accuracy, precision and recall. Application has deployed on Heroku with the help of flask framework.

# Webpage Link


# Demo 


# Technical Aspects

- Python 3.7 and more
- Important Libraries: sklearn, pandas, numpy, matplotlib & seaborn
- Front-end: HTML, CSS 
- Back-end: Flask framework
- IDE: Jupyter Notebook, Pycharm & VSCode
- Database: Cassandra 
- Deployment: Heroku

# How to run this app 

Code is written in Python 3.7 and more. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.

- Create virtual environment - conda create -n myenv python=3.7
- Activate the environment - conda activate myenv
- Install the packages - pip install -r requirements.txt
- Run the app - python run app.py

# Workflow

## Data Collection

Thyroid Disease Data Set from UCI Machine Learning Repository.

Link:https://archive.ics.uci.edu/ml/datasets/thyroid+disease

## Data Pre-processing

- Missing values handling by Simple imputation (KNN Imputer)
- Outliers detection and removal by boxplot and percentile methods
- Categorical features handling by ordinal encoding and label encoding
- Feature scaling done by Standard Scalar method
- Imbalanced dataset handled by SMOTE
- Drop unnecessary columns

## Model Creation and Evaluation

- Various classification algorithms like Random Forest, XGBoost, KNN etc tested.
- Random Forest, XGBoost and KNN were all performed well. XGBoost was chosen for the final model training and testing.
- Hyper parameter tuning was performed using RandomizedSearchCV
- Model performance evaluated based on accuracy, confusion matrix, classification report.


## Database Connection
Cassandra database used for this project.

## Model Deployment
The final model is deployed on Heroku using Flask framework.

## UI





## Project Documents

- HLD: https://github.com/imkushwaha/Thyroid-Disease-Detection/blob/main/Docs/TDD_HLD_V1.0.pdf

- LLD: https://github.com/imkushwaha/Thyroid-Disease-Detection/blob/main/Docs/TDD_LLD_V1.0.pdf

- Architecture: https://github.com/imkushwaha/Thyroid-Disease-Detection/blob/main/Docs/TDD_Architecture_V1.0.pdf

- Wireframe: https://github.com/imkushwaha/Thyroid-Disease-Detection/blob/main/Docs/TDD_Wireframe_V1.0.pdf

- Detailed Project Report: https://github.com/imkushwaha/Thyroid-Disease-Detection/blob/main/Docs/TDD_DPR.pdf


# Author

Upendra Kumar: https://www.linkedin.com/in/imupendra/


# Help Me Improve

Hello Reader if you find any bug please consider raising issue I will address them asap.
