import pandas as pd
import numpy as np

data_base = pd.read_csv("Sql_Testing\database.txt")
num_base = data_base.to_numpy()
print(num_base[10])
value = np.where(num_base == "Imedia i99 Digital Game Phone")
print(num_base[value[0][0]][0])