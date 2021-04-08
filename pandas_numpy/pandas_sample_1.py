import pandas as pd
import numpy as np


page=pd.read_html("https://money.rediff.com/gainers/bse/daily/groupm")


page[0]['% Change'] = np.array([float(li.replace("+ ", "")) for li in page[0]['% Change']])

print(page[0].head(6))
print(page[0]['% Change'].loc[page[0]['Company'] == 'ANG Lifesciences Ind'])
print(page[0]['% Change'].loc[page[0]['Company'] == 'ANG Lifesciences Ind']>9.53)


File_Loc = "Files/rediff.xlsx"

page[0].to_excel(File_Loc, index=False)
np_value = np.array(page[0]['% Change'])
print(np_value.sum())
print(np_value.max())
print(np_value.min())
value = [val for val in page[0]['% Change'].loc[page[0]['Company'] == 'ANG Lifesciences Ind']][0]
print("Value : ", value)

print(np_value)

