from tkinter import *

window = Tk()

kg = StringVar()
grams = ""
pounds = ""
ounces = ""

e1 = Entry ( window , textvariable = kg , width = 20 )

def calc():
    t1.delete(1.0,END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    print (kg.get())
    kg1 = float (kg.get())
    grams = kg1 * 1000
    pounds = kg1 * 2.2
    ounces = kg1 * 35.2
    print ( grams , pounds , ounces )
    t1.insert( END, grams)
    t2.insert( END , pounds)
    t3.insert( END, ounces)

b1 = Button (window , text = 'convert' , command = calc , width = 20  , height = 2  )
t1 = Text (window , width = 20  , height = 2  )
t2 = Text (window , width = 20  , height = 2  )
t3 = Text (window , width = 20  , height = 2  )

b1.grid( row = 0 ,column = 0 )
e1.grid (row =  0 , column = 1)
t1.grid (row =  1 , column = 0)
t2.grid (row =  1 , column = 1)
t3.grid (row =  1 , column = 2)




window.mainloop()