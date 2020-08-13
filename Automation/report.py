### this script will take the results from the model run and generate a report
### it will update the applicants database to reflect the new applicants

import os
import pandas as pd

# Variables #
direct = os.getcwd()
inputName = 'results.csv'
dbName = 'applicants.csv'
#############

#gather data
modelRun = pd.read_csv(os.path.join(direct, inputName))
print('Results gathered')

#parse results
approved = modelRun.loc[modelRun['Approval'] == 1]
non = modelRun.loc[modelRun['Approval'] == 0]

#generate reprot
report = "The following filled out the pre approval form and were approved:\n"
for ix, row in approved.iterrows():
    tstmp = row['Timestamp']
    contact = row['Email Address']
    gender = row['Gender']
    married = row['Married']
    if gender == 'Female':
        if married == 'Yes':
            greet = 'Mrs.'
        else:
            greet = 'Ms.'
    else:
        greet = 'Mr.'
    info = '{} {} at {}'.format(greet, contact, tstmp)
    report = report + info + '\n'
    
report = report + '----------------------\n'
report = report + 'The following filled out the pre approval form and were NOT approved:\n'
for ix, row in non.iterrows():
    tstmp = row['Timestamp']
    contact = row['Email Address']
    gender = row['Gender']
    married = row['Married']
    if gender == 'Female':
        if married == 'Yes':
            greet = 'Mrs.'
        else:
            greet = 'Ms.'
    else:
        greet = 'Mr.'
    info = '{} {} at {}'.format(greet, contact, tstmp)
    report = report + info + '\n'
print('Report generated')

#update db
db = pd.read_csv(os.path.join(direct, dbName))
merged = pd.concat((db, modelRun), axis=0)
merged.to_csv(os.path.join(direct, dbName), index=False)
print('database updated')
print('\n\n')
print(report)
