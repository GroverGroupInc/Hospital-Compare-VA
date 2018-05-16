import os
import pandas as pd
import csv
os.chdir("C:/Users/Valued Customer/Documents/PyCode/PyPython/BayeSnifferPortfolio/HospitalCompare/")

def get_latex_RD_VA_data():
    
#    import os
    import pandas as pd
#import csv
#import os

df3 = pd.read_excel('data/Posteriors/posteriors_RD_VA_Counts.xlsx', sheet_name='Counts')
df3['A'] = '&'
df3['Total'] = .20*df3['Worse than the VHA National Rate'] + .30*df3['No different than the VHA National Rate'] + .50*df3['Better than the VHA National Rate']
df3['B'] = '&'
df3['25thile'] = pd.qcut(df3['Total'], 10, labels=False, duplicates='drop')
df3['C'] = '&'
df3['D'] = '&'
df3['D1'] = 'Rank'
df3['E'] = '\\\ \hline'
df3['F'] = '|'

#df3 = df3[['Provider', 'Hospital', 'A', 'State', 'A', 'County', 'A', 'Total', 'A', '25thile', 'E' ]]

df3 = df3[['Hospital', 'A', 'State', 'B', 'County', 'C', '25thile', 'E' ]]
df3 = df3.sort_values(["State","County", "Hospital", "25thile"], ascending=True)   
#print(df3)
######################################################################################################
writer = pd.ExcelWriter('data/Posteriors/posteriors_RD_VA_LaTex.xlsx', engine='xlsxwriter')
df3.to_excel(writer, sheet_name='Latex', header=False, index=False)
writer.save()
#close()



