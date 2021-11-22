import tkinter as tk
from tkinter.constants import END
from typing import Text
import sendmail
import time

root = tk.Tk()
root.geometry('300x420')
root.title('Automated Email')
ico_url = r'C:\Users\tomas_53ozbyy\Desktop\Coding\Automated Email\robot.ico'
root.iconbitmap(ico_url)

title = tk.Frame(root)
tk.Label(title, text='Automated Email Sender').pack()
title.pack()
tk.Label(text='').pack()


addresses = tk.Frame(root, highlightbackground='grey', highlightthickness=1)

global num
num = 420
global c_row
c_row = 2


def add():
    global c_row
    c_row += 1
    tk.Entry(addresses, width=10).grid(row=c_row, column=0)
    tk.Entry(addresses, width=30).grid(row=c_row, column=1)

    global num
    num += 18
    root.geometry(f'300x{num}')


def clear():
    adrs_e1.delete(0, END)
    adrs_e2.delete(0, END)

    for entry in addresses.grid_slaves():
        if int(entry.grid_info()["row"]) > 2:
            entry.grid_forget()

    global num
    num = 420
    root.geometry(f'300x{num}')


def get_contacts():
    recipients_data = {}
    for entry in addresses.grid_slaves():
        if int(entry.grid_info()["row"]) >= 2:
            if int(entry.grid_info()["column"]) == 1:
                email = entry.get()
            if int(entry.grid_info()["column"]) == 0:
                name = entry.get()
                try:
                    recipients_data[str(name)] = str(email)
                except:
                    pass
    return recipients_data


buttons = tk.Frame(addresses)
add_b = tk.Button(buttons, text='Add', command=add).grid(row=0, column=1)
clear_b = tk.Button(buttons, text='Clear', command=clear).grid(row=0, column=2)
buttons.grid(row=0, column=0, columnspan=3)

adrs_l1 = tk.Label(addresses, text='Name').grid(row=1, column=0)
adrs_l2 = tk.Label(addresses, text='Email').grid(row=1, column=1, columnspan=3)
adrs_e1 = tk.Entry(addresses, width=10)
adrs_e1.grid(row=2, column=0)
adrs_e2 = tk.Entry(addresses, width=30)
adrs_e2.grid(row=2, column=1)

addresses.pack()
tk.Label(text='').pack()


emailinfo = tk.Frame(root, highlightbackground='grey', highlightthickness=1)
subj_l = tk.Label(emailinfo, text='Subject:', width=8)
subj_e = tk.Entry(emailinfo, width=30)
msg_t = tk.Text(emailinfo, width=30, height=10)

subj_l.grid(row=0, column=0)
subj_e.grid(row=0, column=1)
msg_t.grid(row=1, column=0, pady=10, columnspan=2)

emailinfo.pack()
tk.Label(text='').pack()


def ending():
    lbl = tk.Label(text='Success', fg='green')
    lbl.pack()
    time.sleep(2)

    clear()
    subj_e.delete(0, END)
    msg_t.delete("1.0", END)


tk.Button(root, text='Send', command=lambda: [sendmail.send(
    recipients=get_contacts(), subject=subj_e.get(), message=msg_t.get("1.0", END)),
    ending()]).pack()


root.mainloop()
