#def get_twitter_RD_VA_data():
def get_twitter_infection_data():
    import os
import pandas as pd
import os

import csv
os.chdir("C:/Users/Valued Customer/Documents/PyCode/PyPython/BayeSnifferPortfolio/HospitalCompare/")

#import Get_Latex_RD_VA_Data

df4 = pd.read_excel('data/Posteriors/posteriors_RD_VA_Counts.xlsx', sheet_name='Counts')
df4['F'] = '|'
df4['Total'] = .20*df4['Worse than the VHA National Rate'] + .30*df4['No different than the VHA National Rate'] + .50*df4['Better than the VHA National Rate']
df4['G'] = '#PoT'
df4['25thile'] = pd.qcut(df4['Total'], 10, labels=False, duplicates='drop')
df4['H'] = '#RD_VA'
df4['I'] = 'Score ='
df4['J'] = 'High is good'
#df4['E'] = '\\\ \hline'

df4 = df4[['G', 'F', 'H', 'F', 'Hospital', 'F', 'State', 'F', 'County', 'F', 'I', '25thile', 'F', 'J']]

df4 = df4.sort_values(["State","County", "Hospital", "25thile"], ascending=True)   
#print(df4)
##########################################################################################
writer = pd.ExcelWriter('data/Posteriors/posteriors_RD_VA_Twitter.xlsx', engine='xlsxwriter')
df4.to_excel(writer, sheet_name='Twitter', header=False, index=True)
writer.save()
writer.close()
###########################################################################################
#https://stackoverflow.com/questions/41073246/writing-to-csv-file-without-line-space-in-python-3
#with open('records.csv','w', newline='') as csvfile:
#    csvwriter = csv.writer(csvfile)
#    csvwriter.writerow(fields)
#    csvwriter.writerows(rows)




