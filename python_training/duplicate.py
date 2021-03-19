my_list = ["a", 2, "c", "a", 2, "c", "d", "e", "e", "e"]

my_dict = {i: my_list.count(i) for i in my_list}
print(my_dict)
print(my_list.count("a"))

Name_user = "aabbc"
name_dup = {i: Name_user.count(i) for i in Name_user}
print(name_dup)

my_number = [1, 2, 3, 4, 5, 6]
double_number = [number * 2 for number in my_number]
print(double_number)

check_list = ["vignesh", "vicky", "DV", "KMDV", "Dhesna"]
check_name = input("Enter Name to Check in List : ")

if check_name in check_list:
    print("Name Available in List")
else:
    print("Name Not Available in List")

check_list_dic = {"a": "vignesh", "b": "vicky", "c": "DV", "d": "KMDV", "e": "Dhesna"}
check_name = input("Enter Name to Check in List : ")

if check_name in check_list_dic.values():
    print("Name Available in Dictionary")
else:
    print("Name Not Available in Dictionary")
