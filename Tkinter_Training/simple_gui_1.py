from tkinter import *

main_window = Tk()

Label (main_window, text="Enter Name").grid(row=0, column=0)
Label (main_window, text="Enter Age").grid(row=1, column=0)
ur_Name = Entry(main_window, width=50, borderwidth=5)
ur_Name.grid(row=0, column=1)
ur_Age = Entry(main_window, width=50, borderwidth=5)
ur_Age.grid(row=1, column=1)


def on_click ():
    print (f'Your Name is {ur_Name.get()} and your Age is {ur_Age.get()}')


Button (main_window, text="Submit", command=on_click).grid(row=2, column=1)


main_window.mainloop()
