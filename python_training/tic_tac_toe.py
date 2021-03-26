input_user={ 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " " }


def print_board():
    for x in input_user.keys():
        if 1 <= x <= 3:
            print(input_user[x], "|| ", end="")

    print()

    for x in input_user.keys():
        if 4 <= x <= 6:
            print(input_user[x], "|| ", end="")

    print()

    for x in input_user.keys():
        if 7 <= x <= 9:
            print(input_user[x], "|| ", end="")


def input_from_x():
    print()
    if " " in input_user.values():
        x=int(input("Enter number (X) : "))
        if input_user[x] == " ":
            input_user[x]="X"
            print_board()
            input_from_o()

        else:
            input_from_x()

    else:
        print("Done")


def input_from_o():
    print()
    if " " in input_user.values():
        x=int(input("Enter number (O) : "))
        if input_user[x] == " ":
            input_user[x]="O"
            print_board()
            input_from_x()

        else:
            input_from_o()
    else:
        print("Done")


win_log={"X": False, "O": False}


def winner_find(wl):
    if input_user[1] == input_user[2] == input_user[3] == wl:
        win_log[wl]=True
    if input_user[4] == input_user[5] == input_user[6] == wl:
        win_log[wl]=True
    if input_user[7] == input_user[8] == input_user[9] == wl:
        win_log[wl]=True
    if input_user[1] == input_user[4] == input_user[7] == wl:
        win_log[wl]=True
    if input_user[2] == input_user[5] == input_user[8] == wl:
        win_log[wl]=True
    if input_user[3] == input_user[6] == input_user[9] == wl:
        win_log[wl]=True
    if input_user[1] == input_user[5] == input_user[9] == wl:
        win_log[wl]=True
    if input_user[3] == input_user[5] == input_user[7] == wl:
        win_log[wl]=True


input_from_x()

winner_find("X")
winner_find("O")

if win_log["X"]==True:
    print("X is Winner")
if win_log["O"]==True:
    print("O is Winner")
