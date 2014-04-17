from tkinter import *
win = Tk()
win.title('Calculator')
displist=[]

# Will hold the display of the calculator
textbox = StringVar()
textbox.set("")

glister = []

def globalfunc(glist, val):
    print (val)
    glist = glist.append(val)
    print (glist)
    return glist

def buttonClicked(event):
    button = event.widget
    displist.append #create list and take integers from that 
    value = button.cget("text") # cget recognizes the text of the button

    globalfunc(glister, value)


   



buttons = []  # holds all buttons
for buttonNum in range(0,10):
    # creates a new button with that number
    button = Button(win, text=str(buttonNum))
    button.pack()
    button.bind("<Button-1>", buttonClicked)
    # binds function to event
    buttons.append(button)
    button.grid(row=int(buttonNum/3)+1 , column=buttonNum % 3) 

# need to handle the non-numeric buttons
# how to loop over some characters instead of numbers?


functions = ["%","*","-","+","="]
for operator in range(0,5):
    button = Button(win, text=str(functions[operator]))
    button.pack()
    button.bind("<Button-1>", buttonClicked)
    functions.append(button)
    button.grid(row=int(operator+1) , column=4)
    
"""
bdiv = Button(win, text="/")
bmul = Button(win, text="*")
badd = Button(win, text="+")
bsub = Button(win, text="-")
bequ = Button(win, text="=")
bclr = Button(win, text='c')
b1.grid(row=3, column=1)
b2.grid(row=3, column=2)
b3.grid(row=3, column=3)
b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)
b7.grid(row=1, column=1)
b8.grid(row=1, column=2)
b9.grid(row=1, column=3)
b0.grid(row=4, column=1)
bdiv.grid(row=1, column=4)
bmul.grid(row=2, column=4)
badd.grid(row=4, column=4)
bsub.grid(row=3, column=4)
bequ.grid(row=4, column=3)
bclr.grid(row=4, column=2)
"""
l = Label(win, textvariable=textbox)
l.grid(row=0, column=2)

win.mainloop()

