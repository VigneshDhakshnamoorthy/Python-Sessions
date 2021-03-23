file_loc = "../python_training/Files_Test/customer_details.txt"
list_item = ("name","blood","city")
list_cut = []

customer_dic = { }
file = open (file_loc,"r")
for i in file:
    username,details = i.split (":")
    user_details = details.split (",")
    customer_dic[username] = { }
    for j,k in enumerate (user_details):
        customer_dic[username][list_item[j]] = k.strip ()

file.close ()
print (customer_dic)
for user,deta in customer_dic.items ():
    print (f'Username is : {user}')
    for num,det in deta.items ():
        print (f'{num} : {det}')

# file = open(file_loc,"a")
# username = input("Enter Username : ")
# name = input("Enter Name : ")
# blood = input("Enter Blood Group : ")
# city = input("Enter City Name : ")
#
# file.write(f'{username}:{name},{blood},{city}')
# file.close()
