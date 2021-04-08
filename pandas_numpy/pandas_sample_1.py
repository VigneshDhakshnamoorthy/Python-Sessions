import pandas as pd

page=pd.read_html("https://money.rediff.com/gainers/bse/daily/groupm")

page[0]['% Change'] = [float(li.replace("+ ", "")) for li in page[0]['% Change']]

print(page[0].head(6))
print(page[0]['% Change'].loc[page[0]['Company'] == 'Anuroop Packaging Lt'])

File_Loc = "Files/rediff.xlsx"

page[0].to_excel(File_Loc, index=False)