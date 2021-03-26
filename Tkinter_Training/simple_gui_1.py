from tkinter import *

main_window=Tk()

main_window.title("KMDV")
photo=PhotoImage(file="C:/Users/vigne/Google Drive/DV/KMDV/Logo/Logo PNG 1.png")
main_window.iconphoto(False, photo)

Label(main_window, text="Enter Name").grid(row=2, column=0)
Label(main_window, text="Enter Age").grid(row=3, column=0)
ur_Name=Entry(main_window, width=50, borderwidth=5)
ur_Name.grid(row=2, column=1)
ur_Age=Entry(main_window, width=50, borderwidth=5)
ur_Age.grid(row=3, column=1)


def on_click():
    Label(main_window, text=f'Name : {ur_Name.get()}\nAge : {ur_Age.get()}').grid(row=5, column=1)
    ur_Name.delete(0, 'end')
    ur_Age.delete(0, 'end')


Button(main_window, text="Submit", command=on_click).grid(row=4, column=1)

main_window.mainloop()
