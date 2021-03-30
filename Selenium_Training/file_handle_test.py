import pandas as pd

# file_loc = "../Selenium_Training/file_handle.txt"
# print(file_loc)
# file = open(file_loc, 'r')
#
# line = file.read().split("\n")
# print(line)
# dic_name = {}
#
# for lines in line:
#     key, value = lines.partition(" : ")[::2]
#     print(lines)
#     dic_name[key] = value
#     print(key, end=" == ")
#     print(dic_name.get(key))
#
# print(dic_name.keys())
# print(dic_name.values())
# print(dic_name.items())
# print("-" * 150)

# excel file read

File_Loc = "Files/moneydata.xlsx"
data_in = pd.read_excel(File_Loc)
# print(data_in)
# print("-" * 150)

df = pd.DataFrame(data_in)
# print("-" * 150)
# print(df.values)
print("-" * 150)
for df_value in df.values:
    if df_value[0] == "Tantia Constructions":
        print(df_value[0] + " % Change " + str(df_value[4]))
print("-" * 50)

index_com = df.loc[df["Company"] == "Tantia Constructions"].index.item()
print(df.iloc[1, 4])
print("-" * 150)

print(df.count())
print("-" * 150)
print(df.head(5))
# print("-" * 150)
# print(df.items)
print("-" * 150)
print(df.axes)
print("-" * 150)

print(df.get("Company"))
print("-" * 150)
print((df.loc[df["% Change"] > 3]))

print("-" * 150)
print(df.loc[df["% Change"] > 3].sort_values(by="Prev Close (Rs)", ascending=False))
