import numpy as np
import pandas as pd

data={ 'Name': ['Dv', 'Vd', 'kmdv'], 'Age': [23, 32, 31] }

df=pd.DataFrame(data)
# print(df)


numpy_names=np.array(df['Name'].loc[df['Age'] > 30])
print(numpy_names)
numpy_values=np.array(df['Age'].loc[df['Age'] > 30])

print(numpy_values)
