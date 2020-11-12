import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
import requests 
import json

root = tk.Tk()
root.title('Crypto King!!!')
root.geometry('600x300')

def convert_usd():
    usd_val = usd_text.get("1.0",END) 
    print(usd_val)
    r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2CEthereum%2CTether&vs_currencies=usd')
    a = json.loads(r.text)

    curr = [['Bitcoin',int(a["bitcoin"]["usd"])],['Ethereum',int(a["ethereum"]["usd"])],['Tether',int(round(a["tether"]["usd"]))], ]

    for c in curr:
        crypto = int(usd_val)/int(c[1])
        output.insert(END,'USD to ' + c[0] + ' : ' + str(crypto) + '\n')


        



img = ImageTk.PhotoImage(Image.open(requests.get("https://www.dcode.fr/images/dcode.png", stream=True).raw))

panel = Label(root, image = img)
panel.pack()

usd_text = Text(root, height = 1, width = 52) 
usd_text.insert(END, 'How many USD do you have?')
usd_text.pack()


convert_button = Button(root, height = 2, 
                 width = 20,  
                 text ="Convert",command=convert_usd)
convert_button.pack()


output = Text(root, height = 5,  
              width = 52,  
              bg = "light yellow") 

output.pack()

root.mainloop()