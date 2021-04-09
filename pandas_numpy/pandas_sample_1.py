import pandas as pd
import numpy as np

page = pd.read_html("https://money.rediff.com/gainers/bse/daily/groupall")

page[0]['% Change'] = np.array([float(li.replace("+ ", "")) for li in page[0]['% Change']])
File_Loc = "Files/rediff.xlsx"
page[0].to_excel(File_Loc, index=False)


np_columns = np.array(page[0].columns)
np_company = np.array(page[0]['Company'])
np_prev_close = np.array(page[0]['Prev Close (Rs)'])
np_current_price = np.array(page[0]['Current Price (Rs)'])
np_change = np.array(page[0]['% Change'])

# print(np_columns)
# print(np_company)
# print(np_prev_close)
# print(np_current_price)
# print(np_change)

np_index = np.where(np_prev_close == np_prev_close.max())
print(f'Company : {np_company[np_index]}')
print(f'Prev Close (Rs) : {np_prev_close[np_index]}')
print(f'Current Price (Rs) : {np_current_price[np_index]}')
print(f'% Change : {np_change[np_index]}')

