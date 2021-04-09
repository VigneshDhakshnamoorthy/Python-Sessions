import pandas as pd
import numpy as np

page = pd.read_html("https://www.x-rates.com/table/?from=INR&amount=1")


np_country = np.array(page[1]["Indian Rupee"])
np_money = np.array(page[1]["inv. 1.00 INR"])

np_index = np.where(np_money > 50)

for index, count in zip(np_country[np_index],np_money[np_index]):
    print(f'{index} - {count}')
