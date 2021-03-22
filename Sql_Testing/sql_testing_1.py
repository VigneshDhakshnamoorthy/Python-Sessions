import pandas as pd
import pyodbc

server = '192.168.137.15'
database = 'Shopping_Zone'
table_name = 'dbo.f_agent_master'
username = 'sa'
password = 'manoj.111'
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

# cursor.execute(f'SELECT * FROM {database}.{table_name};')
# for row in cursor:
#     print(row)

sql_query = pd.read_sql_query(f'SELECT * FROM {database}.{table_name};',conn)

# data_frame = pd.DataFrame(sql_query)
# print(data_frame)

File_Loc = "../Sql_Testing/agentdata.xlsx"
sql_query.to_excel(File_Loc)
