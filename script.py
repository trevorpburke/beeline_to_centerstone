#!/usr/bin/env python
# this script takes in an Excel document of Contractors from Beeline and
# changes the doc to accomodate Centerstone (CAFM) HR uploads 
# Written by Trevor Burke circa June 2016

import pandas as pd
import time

from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfilename

# GUI windows 
Tk().withdraw() # prevents the root window from appearing
filename = askopenfilename(initialdir ='~/Downloads') # show an "Open" dialog box and return the path to the selected file
timestr = time.strftime("%m-%d-%Y")

save_file = asksaveasfilename(initialdir='~/Documents/beeline_reports', initialfile='onboard_' + timestr)

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
df.to_csv(save_file, sep='\t', index=False)

