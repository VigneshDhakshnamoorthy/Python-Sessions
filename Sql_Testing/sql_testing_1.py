import pandas as pd
import pyodbc
import time

server = '192.168.137.15'
database = 'Shopping_Zone'
table_name = 'dbo.f_agent_master'
username = 'sa'
password = 'manoj.111'
t1 = time.perf_counter()
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

# cursor.execute(f'SELECT * FROM {database}.{table_name};')
# for row in cursor:
#     print(row)

sql_query = pd.read_sql_query(f'SELECT * FROM {database}.{table_name};',conn)

# print(sql_query)

# save files
# File_Loc = "../Sql_Testing/agentdata.xlsx"
# sql_query.to_excel(File_Loc)

# Columns
# print(sql_query.columns)

# AGENT_USERNAME
# print(sql_query["AGENT_USERNAME"])

# head
# print(sql_query.head(6))

# iloc
# print(sql_query.iloc[1:6])
# print(sql_query.iloc[3,3])

# # loc filter
# print(sql_query.loc[sql_query["AGENT_USERNAME"] == "Vigneshd@shoppingzoneindia.com"])
# print(sql_query.loc[sql_query["AGENT_USERNAME"].str.contains('Vignesh')])

# print(sql_query.loc[sql_query["AGENT_USERNAME"].str.contains('Vignesh') | sql_query["AGENT_USERNAME"].str.contains(
# 'vignesh')])

index_vignesh = sql_query.loc[sql_query["AGENT_USERNAME"] == "Vigneshd@shoppingzoneindia.com"].index.item()
print(sql_query.iloc[index_vignesh,24])

t2 = time.perf_counter()
print(f'Took {round(t2 - t1,2)} Seconds to finish')
