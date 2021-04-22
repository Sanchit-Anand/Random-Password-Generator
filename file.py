from random import choice
from tkinter import *
import tkinter.messagebox as tmsg

labelColorList = ['#ff0000', '#800080', 'black', '#7f7f7f']
buttonColorList = ['#acddde', '#caf1de', '#e1f8dc', '#ffe7c7']

charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '%']

def harry(event):
    randomNumber = choice(charList), choice(charList), choice(charList), choice(charList), choice(charList), choice(charList), choice(charList), choice(charList), choice(charList), choice(charList), choice(charList), choice(charList)
    my_label.config(text=randomNumber, fg=choice(labelColorList))
    widget.config(bg=choice(buttonColorList))

def doubleclick(event):
    value = tmsg.showwarning('Warning!', 'Don\'t double click! It will hang the program!')

root = Tk()
root.title('Random Password Generator')
root.geometry('644x334')
root.minsize(500, 150)

heading = Label(root, text='Random Password Generator', font='calibri 20 bold')
heading.pack()

widget = Button(root, text='Generate', bg=choice(buttonColorList), font='comicsansms', padx=20, pady=5)
widget.pack(pady=15)
widget.bind('<Button-1>', harry)
widget.bind('<Double-Button-1>', doubleclick)

my_label = Label(text='Click the above button to generate random number.', fg=choice(labelColorList), font='consolas 13')
my_label.pack()

root.mainloop()
