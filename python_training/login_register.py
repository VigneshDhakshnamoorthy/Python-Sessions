file_loc = "../python_training/Files_Test/user_details.txt"


def log_cond (type_log_reg):
    if type_log_reg == "login":
        print ("#### Enter Login Details ####")
        name = input ("Enter Your Name :").lower ()
        password = input ("Enter Password :").lower ()
        login_old (name,password)
    else:
        print ("#### Enter Registration Details ####")
        name = input ("Enter Your Name :").lower ()
        password = input ("Enter Password :").lower ()
        register_new (name,password)


def type_log ():
    type_log_reg = input ("Enter Login / Register :").lower ()
    if type_log_reg != "login" and type_log_reg != "register":
        type_log ()
    else:
        log_cond (type_log_reg)


def login_old (name,password):
    success = False
    with open (file_loc,'r') as file:
        for i in file:
            a,b = i.split (",")
            b = b.strip ()
            if a == name and b == password:
                success = True
                break

    if (success == True):
        print (f'Logged in :  name - {name} and password - {password}')
    else:
        log_cond ("login")


def register_new (name,password):
    with open (file_loc,'a') as file:
        file.write (f'\n{name},{password}')

    print (f'Registered :  name - {name} and password - {password}')
    login_old(name,password)


if __name__ == "__main__":
    type_log ()
