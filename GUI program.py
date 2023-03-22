import json
import requests
from tkinter import *

window = Tk()
window.title("Fun Fact Generator")
window.geometry('800x80')


def get_fun_fact():

    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    resoponse = requests.request("GET", url)
    data = json.loads(resoponse.text)
    useless_fact = data['text']
    lbl.configure(text=useless_fact)


btn = Button(window, text='Click Me', command=get_fun_fact)
btn.pack()

lbl = Label(window, text='Click the button to get a random fact')
lbl.pack()

window.mainloop()
tkinter.Tk.mainloop(n=0)
