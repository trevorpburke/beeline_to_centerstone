#!/usr/bin/env python
# this script takes in an Excel document of Contractors from Beeline and
# changes the doc to accomodate Centerstone (CAFM) HR uploads 
# Written by Trevor Burke (trevorpburke@gmail.com) circa June 2016

import pandas as pd
import time
import sys

filename = sys.argv[1]

timestr = time.strftime("%m-%d-%Y")

# deleting, modifying, and inserting column data 
df = pd.read_excel(filename)

df = df.drop(df.columns[[6, 9, 10]], axis=1)

df.rename(columns={'Beeline ID': 'Employee ID',
                    'Contingent Worker First Name': 'First Name',
                    'Contingent Worker Last Name': 'Last Name',
                    'Date': 'Hire Date', 
                    'Date.1': 'End Date',
                    'Location Name': 'Business Site', 
                    'Assignment Manager': 'Workers Manager',
                    'Billing Department Name': 'Supervisory Org'}, inplace=True)

df.insert(loc=8, column='Employee Type Name', value='Contractor')

# save to Desktop 
df.to_csv("~/Documents/onboard_" + timestr, sep='\t', index=False)
