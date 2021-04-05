import numpy as np
import pandas as pd

data = {'Name': ['Dv', 'Vd', 'kmdv'], 'Age': [23, 32, 31]}

df = pd.DataFrame(data)
# print(df)

print(df.loc[df['Name'] == 'kmdv'])
