def get_RD_VA_counts():
    import os
import pandas as pd
import os

import Create_RD_VA_Dictionary

import os
import csv
os.chdir("C:/Users/Valued Customer/Documents/PyCode/PyPython/BayeSnifferPortfolio/HospitalCompare/")


df = pd.read_csv('data/Posteriors/posterior_RD_VA.csv')

#input("#################### Press Enter to produce and view the revised dictionary generated data... ####################")
df.columns = ['Provider', 'Hospital', 'State', 'County', 'National']

df1 = df[(df.National != 'Not Available') &
         (df.National != 'Number of Cases Too Small')] 

#print(df1)
##################################################
df2 = pd.crosstab([df.Provider, df.Hospital, df.State, df.County], [df1.National], margins=False) 
##################################################
writer = pd.ExcelWriter('data/Posteriors/posteriors_RD_VA_Counts.xlsx', engine='xlsxwriter')

df2.to_excel(writer, sheet_name='Counts')

#########################INSTRUCTIONS############################
## Run 1st time as: writer.save() then 2nd time as #writer.save()

writer.save()
#writer.close()

os.remove('data/Posteriors/posterior_RD_VA.csv')
