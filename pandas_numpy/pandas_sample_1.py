import pandas as pd

page = pd.read_html("https://money.rediff.com/gainers")
print(page[0]['Company'].head(6))