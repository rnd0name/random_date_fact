import requests
from datetime import datetime

random_fact_api_base = 'http://numbersapi.com'

def get_date_time() :
    data = str(datetime.now())
    return [data[0:4], data[5:7], data[8:10], data[11:13], data[14:16]]

def get_random_fact() :
    data = str(datetime.now())
    y,m,d,h,min = data[0:4], data[5:7], data[8:10], data[11:13], data[14:16]

    if d[1] == '0' :
        d.replace("0", "")

    date = f'/{m.replace("0", "")}/{d}?json'
    y_date = f'{d}/{m}/{y}'
    time = f'{h}:{min}'

    date_fact_url = random_fact_api_base + date

    date_fact = requests.get(date_fact_url, timeout=10).json()['text']

    return time, y_date, date_fact

time, date, fact = get_random_fact()



from tkinter import Tk, Button, Text, Label, StringVar, END

front_color = 'cyan'
bk_color = 'black'

root = Tk('Today\'s Random Fact')
root.config(background=bk_color)

for i in range(8) :
    root.rowconfigure(i, weight=1)
for i in range(10) :
    root.columnconfigure(i, weight=1)

time_label = Label(root, background=bk_color, foreground=front_color)
time_label.grid(column=0,columnspan=5,row=1,rowspan=1,sticky='nsew')
time_var = StringVar(root, time)
time_label.configure(textvariable=time_var)

date_label = Label(root, background=bk_color, foreground=front_color)
date_label.grid(column=0,columnspan=10,row=0,rowspan=1,sticky='nsew')
date_var = StringVar(root, date)
date_label.configure(textvariable=date_var)

def time_update() :
    time = get_date_time()
    time_var.set(f'{time[3]}:{time[4]}')
    date_var.set(f'{time[2]}/{time[1]}/{time[0]}')
    root.after(4500, time_update)

fact_text = Text(root, background=bk_color, foreground=front_color)
fact_text.grid(row=3, rowspan=5, column=0, columnspan=10, sticky='nsew')

def refresh() :
    fact = get_random_fact()[2]
    fact_text.delete("1.0", END)
    fact_text.insert("1.0", fact)

refresh_button = Button(root, text='Refresh', command=refresh, background=bk_color, foreground=front_color)
refresh_button.grid(column=7, columnspan=3, row=1, rowspan=1, sticky='nsew')

time_update()
refresh()
input()