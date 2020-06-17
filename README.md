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

### Technologies
* Python
* Jupyter Notebooks


### Requirements/Imports
* Python 3.8.1
* Pandas
* Numpy
* Matplotlib
* Seaborn
* Scikit Learn
* Requests
* Stats

## Project Description
****1. Data:**** Train and Test sets downloaded from [Analytics Vidhaya](https://datahack.analyticsvidhya.com/contest/practice-problem-loan-prediction-iii/#ProblemStatement), (at the bottom).  Data set was mostly clean but contained missing values.

****2. EDA:**** Explored the training data set to visualize the breakdown of variable categories and their proportion of loan approval status.  Without any look at the data, I hypothesized that income and credit history would be the two most important factors.  Results were interesting.  I also created new variables, mostly debt/equity ratios in hopes these would create better indicators of financial health.

****3. Imputation:****  I was first interested in how many specific variables I had to impute as well as if any applicants had more than one missing value.  Working from the least amount missing to the most, I filled in the missing values.  Most were filled with the mode, however, some were filled based on probability within grouping.  For example, missing marriage values were based on gender of the applicant.  Credit History had the most missing values, so I tried to build a seperate model to predict this, however the model just predicted having a history (the mode).

****4. Model Build:****  I utilized 4 types of models as well as multiple types of model inputs.  The 4 model types included logistic regression, a random forest with maximum depth, and random forest without maximum depth, and a decision tree.  The following are descriptions of the types of model inputs I tried:
  * v2: Dependents are dummy variables, not ordinal
  * v3: Log family income and loan amount
  * v4: remove outliers from family income and loan amount
  * v5: remove dependents and married and use family size and outliers removed
  * v6: remove dependents and married and use family size
  * v7: remove outliers, make model for inliers and model for outliers, recombine for predictions
 
 ****5. Next Steps:****  Lower FPR rate.

## Needs of this project
* data exploration/descriptive statistics
* data processing/cleaning
* predictive modeling

## Getting Started
1. Ensure local machine has program that can run iPython notebooks.
2. Download the following:
 * Loan Prediction EDA
 * Loan Prediction Impute and Clean
 * Loan Prediction Model Build
 * Loan Prediction Rand Forest
3. Run above in same order as listed
4. Download Work.zip and extract for all other files used prior to finished product.

## Contributing Members

****Team Lead:**** [Joe Pollastrini](https://github.com/joepollastrini)
* ****Email:**** joepollastrini@gmail.com
* ****Phone:**** (630)-418-3594
* [Linkedin](www.linkedin.com/in/joe-pollastrini-a56b24104)

## Contact
* Feel free to contact team leads with any questions, comments, or concerns!
