from tkinter import *

shouldReset = False


def handleClick(btnVal):
    global shouldReset
    curr = strVar.get()
    if btnVal=="=":
        strVar.set(eval(curr))
        shouldReset = True
    else:
        if shouldReset and not (btnVal in ['/','*','+','-']):
            strVar.set(btnVal)
        else:
            strVar.set(curr+btnVal)
        shouldReset = False

window = Tk()

window.title('Calculator')

strVar = StringVar()
label = Label(window, textvariable=strVar)
label.grid(row=0, column=0, columnspan=4)

Button(window, text="7",
            command=lambda:handleClick("7"),
            width=5, height=2).grid(row=1, column=0)
Button(window, text="8",
            command=lambda:handleClick("8"),
            width=5, height=2).grid(row=1, column=1)
Button(window, text="9",
            command=lambda:handleClick("9"),
            width=5, height=2).grid(row=1, column=2)
Button(window, text="/",
            command=lambda:handleClick("/"),
            width=5, height=2).grid(row=1, column=3)

Button(window, text="4",
            command=lambda:handleClick("4"),
            width=5, height=2).grid(row=2, column=0)
Button(window, text="5",
            command=lambda:handleClick("5"),
            width=5, height=2).grid(row=2, column=1)
Button(window, text="6",
            command=lambda:handleClick("6"),
            width=5, height=2).grid(row=2, column=2)
Button(window, text="*",
            command=lambda:handleClick("*"),
            width=5, height=2).grid(row=2, column=3)

Button(window, text="1",
            command=lambda:handleClick("1"),
            width=5, height=2).grid(row=3, column=0)
Button(window, text="2",
            command=lambda:handleClick("2"),
            width=5, height=2).grid(row=3, column=1)
Button(window, text="3",
            command=lambda:handleClick("3"),
            width=5, height=2).grid(row=3, column=2)
Button(window, text="-",
            command=lambda:handleClick("-"),
            width=5, height=2).grid(row=3, column=3)

Button(window, text=".",
            command=lambda:handleClick("."),
            width=5, height=2).grid(row=4, column=0)
Button(window, text="0",
            command=lambda:handleClick("0"),
            width=5, height=2).grid(row=4, column=1)
Button(window, text="=",
            command=lambda:handleClick("="),
            width=5, height=2).grid(row=4, column=2)
Button(window, text="+",
            command=lambda:handleClick("+"),
            width=5, height=2).grid(row=4, column=3)

window.mainloop()
