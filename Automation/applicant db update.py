### This sript will grab responses from the online form (Google Forms)
### It will then update the locally saved database
### It will return any new applicants since the last update, as a new database

import pandas as pd
import google_funcs as gf
import os

#variables#
spreadsheet_code = '1O5fJjor141NtkKtRGd2S_HWL4Z3fTYEYBdOiizbrUqQ'
tab_name = 'Form Responses 1'
scope = ['https://www.googleapis.com/auth/spreadsheets']
dbName = 'applicants.csv'
output = 'toModel.csv'
###########


#get info from google sheets
data = gf.pull_sheet_data(scope, spreadsheet_code, tab_name)
df = pd.DataFrame(data[1:], columns=data[0])

#clean dataframe
# column renaming
df.rename(columns = {'Are you married?':'Married'
          ,'How many dependents do you have?  (Do not count spouse if married)':'Dependents'
          ,'Did you graduate high school?':'Education'
          ,'Are you self-employed?':'Self_Employed'
          ,"What is your monthly pre-tax income? (If married, do not include your spouse's income)":'ApplicantIncome'
          ,"What is your spouse's monthly pre-tax income?":'CoapplicantIncome'
          ,'What is the loan amount you are applying for?':'LoanAmount'
          ,"What term length are you applying for?":'Loan_Amount_Term'
          ,'Do you have a credit history?':'Credit_History'
          ,'What area will the house be?':'Property_Area'}, inplace=True)
df['Education'] = df['Education'].apply(lambda x: 'Graduate' if x == 'Yes' else 'Not Graduate')
print('Google Drive data cleaned')

#get old applications (already in database)
dbPath = os.path.join(os.getcwd(), dbName)
apps = pd.read_csv(dbPath)
print('Old database grabbed')

#get applications already ran through model
already_ran = apps.loc[apps['Model Run'] == 1]

#get applications to be run through model
together = pd.concat((df, apps), axis=0, sort=False)
together.drop(columns=['Model Run'], inplace=True)
modelApps = together.drop_duplicates(subset = ['Timestamp', 'Email Address'], keep=False)
print('Applicants for model run determined')

#output applicants to database
modelApps.to_csv(os.path.join(os.getcwd(), output), index=False)
print('Applicant data saved')
