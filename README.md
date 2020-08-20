# [Use this link to fill out application and get loan approval status](https://forms.gle/TxX6AF3d1JuNdgET9)

# Loan Prediction
This project was part of a hackathon found on [Analytics Vidhaya Loan Prediction](https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/). Other projects can be found at the [main GitHub repo](https://github.com/joepollastrini).

#### -- Project Status: [Active]

## Project Intro/Objective
The purpose of this project is to automate the loan eligibility process based on customer detail provided while filling out an online application form.  To automate the process, the dataset will be utilized to identify customer segments that are eligible for the loan amount requested so that a company can specifically target these customers.

### Methods Used
* Descriptive Statistics
* Feature Engineering
* Data Visualization
* Predictive Modeling
* Machine Learning
* Cluster Analysis
* Cross Validation
* Hyperparameter Optimization

### Technologies
* Python
* Jupyter Notebooks
* Google Forms


### Requirements/Imports
* Python 3.8.1
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Scikit Learn
* Requests
* Stats
* Pickle
* google_funcs

## Project Description
****1. Data:**** Train and Test sets downloaded from [Analytics Vidhaya](https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/#ProblemStatement), (at the bottom).  Data set was mostly clean but contained missing values.

****2. EDA:**** Explored the training data set to visualize the breakdown of variable categories and their proportion of loan approval status.  Without any look at the data, I hypothesized that income and credit history would be the two most important factors.  Results were interesting.  I also created new variables, mostly debt/equity ratios in hopes these would create better indicators of financial health.

****3. Imputation:****  I was first interested in how many specific variables I had to impute as well as if any applicants had more than one missing value.  Working from the least amount missing to the most, I filled in the missing values.  Many were imputed using a KNN model, however, some were filled based on probability within grouping.  For example, missing marriage values were based on gender of the applicant.  Credit History had the most missing values and seems to be the most important variable.  Correct imputation prediction will likely improve model accuracy.

****4. Model Build:****  I utilized 4 types of models as well as multiple types of model inputs.  The 4 model types included logistic regression, a random forest with maximum depth, and random forest with a limited depth, and a decision tree.  The following are descriptions of the types of model inputs I tried:
  * v2: Dependents are dummy variables, not ordinal
  * v3: Log family income and loan amount
  * v4: remove outliers from family income and loan amount
  * v5: remove dependents and married and use family size and outliers removed
  * v6: remove dependents and married and use family size
  * v7: remove outliers, make model for inliers and model for outliers, recombine for predictions
 
 ****5. Automation:****  I built out a system that would be similar to one put in place at an actual bank.  Using Google Forms as the application for loan pre-approval, the scripts grab that user data, run it through the model, and create a report for the agents.
 
 ****6. Next Steps:****  Email report.
 
 
## Needs of this project
* Data Exploration/Descriptive Statistics
* Data Processing/Cleaning
* Predictive Modeling

## Getting Started
1. Ensure local machine has program that can run python and iPython notebooks.
2. Download the following for code to run:
 * forModel_train.csv and forModel_test.csv
 * RF Model Build (KNN Imputed, Cross Validation, Hyperparameter Optimization).ipynb
 * Final Model.ipynb
3. Download the following to see work/thought process
 * train_loan_data.csv and test_loan_data.csv
 * Loan Prediction EDA.ipynb
 * Loan Prediction Impute and Clean.ipynb
 * Entire KNN Imputation folder (to see KNN model build process)
 * Entire Models Folder (stores models created from above files)
 * KNN Impute and Clean
4. Download the Automation folder for the full project (takes user input and creates report)

## Contributing Members

****Team Lead:**** [Joe Pollastrini](https://github.com/joepollastrini)
* ****Email:**** joepollastrini@gmail.com
* ****Phone:**** (630)-418-3594

## Contact
* Feel free to contact team leads with any questions, comments, or concerns!
