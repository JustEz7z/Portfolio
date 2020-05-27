import requests
from tkinter import *

def solver (a,b,c):
    result = a * b * c
    return "For today your bitcoins cost " + str(result) + " gryvnia"

def inserter(value):
    """ Inserts value into text widget """
    try:
        output.delete("0.0","end")
        output.insert("0.0",value)
    except TclError:
        output.delete("0.0","end")
        output.insert("0.0",value)

def handler():
    """ Get the content of entries and passes result to the output area """
    try:
        # except for the correct values
        b_val = float(b.get())
        inserter (solver(price_of_usd, b_val, usd))
    except ValueError:
        inserter("You must enter only amount of bitcoins")


bitcoin_api_url = 'https://blockchain.info/ticker'
coursmoney_url = 'http://bank-ua.com/export/exchange_rate_cash.json'

response = requests.get(bitcoin_api_url)
response_json = response.json()
price_of_usd = (response_json["USD"]['buy'])

cours = requests.get(coursmoney_url)
cours_json = cours.json()
usd = float(cours_json[1]['rateBuy'])

root = Tk()
# name of window
root.title("Bitcoin calculator")
# size of window
root.minsize(725,500)
# cannot change window
root.resizable(width=False, height=False) 

# create frame
frame = Frame(root)
frame.grid(row=9,column=6)

# text for bitcoin
a_lab = Label(frame, bg="red", font="Arial 32", text="BITCOIN = "+str(price_of_usd)).grid(row=0,column=0, sticky = N+S+W+E )
 
# create field for input amount bitcoin
b = Entry(frame, font= "Arial 28", width=7)
b.grid( row=3, column=3,  sticky = N+S+W+E)

# text for amount of bitcoin
b_lab = Label(frame, bg="green", font= "Arial 18", text="Amount\nof Bitcoin ").grid(row=3, column=0, sticky = N+S+W+E)

# text for USD
c_lab = Label(frame, bg="yellow", font= "Arial 18", text="USD = "+str(usd)).grid(row=2, column=0, sticky = N+S+W+E)

# button Enter
but = Button(frame, bg ="grey", text="Enter", command=handler).grid(row=3, column=4, padx=(10,0), sticky = N+S+W+E)
 
# area for output result
output = Text(frame, bg="lightblue", font="Arial 18", width=75, height=2)
output.grid(row=7, columnspan=6)
 
# start
root.mainloop()