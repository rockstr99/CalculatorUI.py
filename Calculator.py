# hi this is a simple calculator & it also has a user interface .
# i created it with help of tkinter & python

from tkinter import *
from tkinter import messagebox

def buttonClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator= ""
    text_Input.set("")

def btnEqualInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""

cal = Tk()
cal.title("Arpit's Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font= ('arial', 20, 'bold'), textvariable = text_Input, bd= 30, insertwidth = 4, bg = "grey", justify = "right").grid(columnspan = 4)

btn7 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "7" , bd= 38, fg = "black", bg = "grey",command = lambda:buttonClick(7)).grid(row = 1, column = 0)
btn8 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "8" , bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick(8)).grid(row = 1, column = 1)
btn9 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "9" , bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick(9)).grid(row = 1, column = 2)
Addition = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "+" , bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick("+")).grid(row = 1, column = 3 )
btn4 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "4" , bd= 38, fg = "black", bg = "grey",command = lambda:buttonClick(4) ).grid(row = 2, column = 0)
btn5 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "5" , bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick(5)).grid(row = 2, column = 1)
btn6 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "6" , bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick(6)).grid(row = 2, column = 2)
Substract = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "-" , bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick("-")).grid(row = 2, column = 3)
btn1 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "1" , bd= 38, fg = "black", bg = "grey" ,command = lambda:buttonClick(1)).grid(row = 3, column = 0)
btn2 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "2" , bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick(2)).grid(row = 3, column = 1)
btn3 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "3" , bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick(3)).grid(row = 3, column = 2)
Multiply = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "*" , bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick("*")).grid(row = 3, column = 3)
btn0 = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "0" , pady = 16, bd= 38, fg = "black", bg = "grey" ,command = lambda:buttonClick(0)).grid(row = 4, column = 0)
btnClear = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "C" ,pady = 16, bd= 38, fg = "black" , bg = "grey", command = btnClearDisplay).grid(row = 4, column = 1)
Equal = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "=" ,pady = 16, bd= 38, fg = "black" , bg = "grey", command = btnEqualInput).grid(row = 4, column = 2)
Divide = Button(cal, padx = 16,  font= ('arial', 20, 'bold'), text = "/" , pady = 16,bd= 38, fg = "black" , bg = "grey",command = lambda:buttonClick("/")).grid(row = 4, column = 3)


cal.mainloop()