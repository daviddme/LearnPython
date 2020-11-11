import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
import requests 

root = tk.Tk()
root.title('Crypto King!!!')
root.geometry('600x300')

def convert_usd():
    usd_val = usd_text.get("1.0",END) 
    print(usd_val)

    curr = [['Bitcoin',14096],['Ethereum',400],['Tether',1.01]]
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