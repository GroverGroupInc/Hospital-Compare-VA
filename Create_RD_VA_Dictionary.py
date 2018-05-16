def create_RD_VA_dictionary():
    import csv
import pandas as pd
import os
import csv

os.chdir("C:/Users/Valued Customer/Documents/PyCode/PyPython/BayeSnifferPortfolio/HospitalCompare/data/")

with open("FlatFiles/Readmissions and Deaths - VA.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('Posteriors/posterior_RD_VA.csv', 'w', newline='') as posterior_RD_VA:
        fieldnames=['Provider_ID',
                    'Hospital Name', 
                    'State', 
                    'County',
                    'Compare to National'
                    ]  

# This writes the dictionary
   
        csv_writer = csv.DictWriter(posterior_RD_VA, fieldnames=fieldnames, delimiter=',') 

# This writes the column header names
        
        csv_writer.writeheader()

# This deleted the columns in the csv file. 
# To add these columns, you would delete them from here and add to the posterior_RD_VA.csv file.
       
        for line in csv_reader:
            del line['Score']
            del line['Address']
            del line['City']
            del line['ZIP Code']
            del line['Measure ID']
            del line['Measure Name']
            del line['Footnotes']
            del line['Measure Start Date']
            del line['Measure End Date']
            del line['VHA National Rate']
            del line['Denominator']
            del line['Lower Estimate']
            del line['Higher Estimate']
            csv_writer.writerow(line)

# This reads the dictionary with the undeleted header names and their associated columns.

df = pd.read_csv('Posteriors/posterior_RD_VA.csv')

# This prints the dictionary.

print(df)
