### This script will grab the applicant's data
### It will run the data through the model to predict the loan status

import os
import pandas as pd
import numpy as np
import pickle


# Variables #
direct = os.getcwd()
os.chdir('..')
parent = os.getcwd()
inputName = 'toModel.csv'
modelName = 'loan pred model.sav'
output = 'results.csv'
#############


#get applicant data
toModel = pd.read_csv(os.path.join(direct, inputName))
print('Applicant data gathered')

#clean data for model input
cleaning = toModel.copy()
cleaning['Dependents_Ord'] = cleaning['Dependents'].apply(lambda x: 3 if x == '3+' else int(x))
cleaning['FamilyIncome'] = cleaning['ApplicantIncome'] + cleaning['CoapplicantIncome']
cleaning['LoanAmountLog'] = np.log(cleaning['LoanAmount'])
cleaning['Married_IO'] = cleaning['Married'].apply(lambda x: 1 if x=='Yes' else 0)
cleaning['FamilySize'] = cleaning['Dependents_Ord'] + cleaning['Married_IO'] + 1
cleaning['IncomePerMember'] = cleaning['FamilyIncome'] / cleaning['FamilySize']
cleaning['Debt_Equity'] = (cleaning['LoanAmount'] * 1000) / cleaning['FamilyIncome']
cleaning['Debt_Equity_Annual'] = (((cleaning['LoanAmount']*1000) / cleaning['Loan_Amount_Term']) * 12) / cleaning['FamilyIncome']
cleaning['Credit_History'] = cleaning['Credit_History'].apply(lambda x: 1 if x == 'Yes' else 0)
print('Data ready for model')

#run data through model
cleaned = cleaning[['Credit_History', 'Debt_Equity', 'Debt_Equity_Annual', 'LoanAmountLog', 'FamilyIncome', 'IncomePerMember']]
model = pickle.load(open(os.path.join(parent, 'Models', modelName), 'rb'))
preds = model.predict(cleaned)
print('Predictions created')

#save results
toModel['Model Run'] = 1
predictions = pd.DataFrame(preds, columns=['Approval'])
results = pd.concat((toModel, predictions), axis=1)
results.to_csv(os.path.join(direct, output), index=False)
print('Predictions saved')
