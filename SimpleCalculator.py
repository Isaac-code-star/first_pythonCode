from tkinter import *

expression = ""


def press(num):
    global expression

    expression = expression + str(num)
    equation.set(expression)


def equal_press():
    try:
        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:
        equation.set("ERROR!!")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == '__main__':
    GUI = Tk()
    GUI.geometry("300x350")
    GUI.title("Simple Calculator")

    equation = StringVar()

    expression_field = Entry(GUI, textvariable=equation)
    expression_field.grid(row=1, columnspan=6, ipadx=100, ipady=5)

    buttonReset = Button(GUI, text="Clear", font=10, height=2, width=4, command=clear)
    buttonReset.grid(row=2, column=3)
    buttonDivide = Button(GUI, text="/", font=10, height=2, width=4, command=lambda: press("/"))
    buttonDivide.grid(row=2, column=1)

    buttonMultiply = Button(GUI, text="*", font=10, height=2, width=4, command=lambda: press("*"))
    buttonMultiply.grid(row=2, column=2)

    buttonSeven = Button(GUI, text="7", font=10, height=2, width=4, command=lambda: press(7))
    buttonSeven.grid(row=3, column=0)

    buttonEight = Button(GUI, text="8", font=10, height=2, width=4, command=lambda: press(8))
    buttonEight.grid(row=3, column=1)

    buttonNine = Button(GUI, text="9", font=10, height=2, width=4, command=lambda: press(9))
    buttonNine.grid(row=3, column=2)

    buttonMinus = Button(GUI, text="-", font=10, height=2, width=4, command=lambda: press("-"))
    buttonMinus.grid(row=3, column=3)

    buttonFour = Button(GUI, text="4", font=10, height=2, width=4, command=lambda: press(4))
    buttonFour.grid(row=4, column=0)

    buttonFive = Button(GUI, text="5", font=10, height=2, width=4, command=lambda: press(5))
    buttonFive.grid(row=4, column=1)

    buttonSix = Button(GUI, text="6", font=10, height=2, width=4, command=lambda: press(6))
    buttonSix.grid(row=4, column=2)

    buttonPlus = Button(GUI, text="+", font=10, height=2, width=4, command=lambda: press("+"))
    buttonPlus.grid(row=4, column=3)

    buttonOne = Button(GUI, text="1", font=10, height=2, width=4, command=lambda: press(1))
    buttonOne.grid(row=5, column=0)

    buttonTwo = Button(GUI, text="2", font=10, height=2, width=4, command=lambda: press(2))
    buttonTwo.grid(row=5, column=1)

    buttonThree = Button(GUI, text="3", font=10, height=2, width=4, command=lambda: press(3))
    buttonThree.grid(row=5, column=2)

    buttonZero = Button(GUI, text="0", font=10, height=2, width=4, command=lambda: press(0))
    buttonZero.grid(row=6, column=1)

    buttonDecimal = Button(GUI, text=".", font=10, height=2, width=4, command=lambda: press("."))
    buttonDecimal.grid(row=6, column=2)

    buttonEqual = Button(GUI, text='=', font=10, height=2, width=4, command=equal_press)
    buttonEqual.grid(row=5, column=3)

    GUI.mainloop()
