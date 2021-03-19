import pandas as  pd

file_loc = "../Selenium_Training/file_handle.txt"
print(file_loc)
file = open(file_loc, 'r')

line = file.read().split("\n")
print(line)
dic_name = {}

for lines in line:
    key, value = lines.partition(" : ")[::2]
    print(lines)
    dic_name[key] = value
    print(key, end=" == ")
    print(dic_name.get(key))

print(dic_name.keys())
print(dic_name.values())
print(dic_name.items())
print("-" * 150)

# excel file read

File_Loc = "../Selenium_Training/Excel/moneydata.xlsx"
data_in = pd.read_excel(File_Loc, usecols=[1, 2, 3, 4, 5])
# print(data_in)
# print("-" * 150)

df = pd.DataFrame(data_in)
# print(df.values)
# print("-" * 150)

for df_value in df.values:
    if df_value[0] == "Golkonda Aluminium":
        print(df_value[0]+" % Change "+str(df_value[4]))
