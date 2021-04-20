import pandas as pd
import numpy as np
import sqlite3 as sql

data_base = pd.read_csv("Sql_Testing/database.txt")
# num_base = data_base.to_numpy()
# print(num_base[10])
# value = np.where(num_base == "Imedia i99 Digital Game Phone")
# print(num_base[value[0][0]][0])
# print(data_base.columns)
database = "Sql_Testing/db/product.db"
table_name = "product"
conn = sql.connect(database)
data_base.to_sql(table_name, conn, if_exists='replace', index=False)

conn = sql.connect(database)
sqlite_db = pd.read_sql(f'SELECT * FROM {table_name}', conn)
print(sqlite_db)
