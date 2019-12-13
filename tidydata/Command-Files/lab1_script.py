import pandas as pd
import numpy as np
import math
import matplotlib
import pyreadstat as pst
import sys

income = []
religion = []

if len(sys.argv) == 1:
    filename = 'pew_conv.txt'
else:
    filename = sys.argv[1]

with open(filename)as file:
    for line in file:
        temp = line.split(';;')
        break

    religion_index = temp.index('\"q16\"')
    income_index = temp.index('\"income\"')

    for line2 in file:
        temp2 = line2.split(';;')

        if '$' in temp2[income_index+1] or 'Don\'t know/Refused' in temp2[income_index+1]:

            if '\"$150,000 or more\"' in temp2[income_index+1]:
                temp2[income_index + 1] = '>$150k'
            if '\"10 to under $20,000\"' in temp2[income_index+1]:
                temp2[income_index + 1] = '$10-20k'
            if '\"100 to under $150,000\"' in temp2[income_index+1]:
                temp2[income_index + 1] = '$100-150k'
            if '\"20 to under $30,000\"' in temp2[income_index+1]:
                temp2[income_index + 1] = '$20-30k'
            if '\"30 to under $40,000\"' in temp2[income_index+1]:
                temp2[income_index + 1] = '$30-40k'
            if '\"40 to under $50,000\"' in temp2[income_index+1]:
                temp2[income_index + 1] = '$40-50k'
            if '\"50 to under $75,000\"' in temp2[income_index+1]:
                temp2[income_index + 1] = '$50-75k'
            if '\"75 to under $100,000\"' in temp2[income_index+1]:
                temp2[income_index + 1] = '$75-100k'
            if '\"Don\'t know/Refused (VOL.)\"' in temp2[income_index+1]:
                temp2[income_index + 1] = 'Don\'t know/refused'
            if '\"Less than $10,000\"' in temp2[income_index+1]:
                temp2[income_index + 1] = '<$10k'

            if '\" Atheist (do not believe in God) \"' in temp2[religion_index+1]:
                temp2[religion_index + 1] = 'Atheist'
            if '\" Agnostic (not sure if there is a God) \"' in temp2[religion_index+1]:
                temp2[religion_index + 1] = 'Agnostic'
            if 'Unity; Unity Church Christ Church Unity' in temp2[religion_index+1]:
                temp2[religion_index + 1] = 'Unity Church Christ'
            if '(VOL)' in temp2[religion_index+1]:
                temp2[religion_index + 1] = temp2[religion_index + 1].replace('(VOL)','')
            if '" ' in temp2[religion_index+1]:
                temp2[religion_index + 1] = temp2[religion_index + 1].replace('" ','')
            if ' "' in temp2[religion_index+1]:
                temp2[religion_index + 1] = temp2[religion_index + 1].replace(' "','')
            
            income.append(temp2[income_index+1])
            religion.append(temp2[religion_index + 1])


data = {'Religion':religion,'Income':income,'Val':1}

results = pd.DataFrame(data)

results['Income'] = pd.Categorical(data['Income'],["<$10k", "$10-20k", "$20-30k", "$30-40k", "$40-50k", "$50-75k",
  "$75-100k", "$100-150k", ">$150k", "Don't know/refused"])

results = results.groupby(['Religion','Income'])['Val'].sum().reset_index()
#results = results.pivot_table('Val','Income','Religion')

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 5)
pd.set_option('display.width', 1000)

print(results)