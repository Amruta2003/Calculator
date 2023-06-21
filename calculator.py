# tkinter is a framework used to create GUI elements
from tkinter import *

# To create the main window
window = Tk()               
window.geometry("350x600")        #size of the window
window.title("Calculator")       #title of the window

#frame1 to create the title
frame1=Frame(window)
frame1.pack(pady=5)
titleLabel=Label(frame1, text="          Calculator          ",font=("Arial",30),bg="pink")
titleLabel.pack()

#frame2 to create input field
frame2=Frame(window)
frame2.pack(pady=5)

#an entry field widget where the user can enter numbers and see the results.
entry = Text(frame2, width=30, height=3, borderwidth=2,bg="grey")
entry.grid(row=0, column=0, columnspan=3)

#frame2 to create grids
frame3=Frame(window)
frame3.pack(pady=5)

buttons = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['0','. ', '+'],
    ['- ', '* ', '/ ']
]


# function is called when a number button is clicked
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, str(current) + str(number))

#function is called when the clear button ('C') is clicked
def button_clear():
    entry.delete(0, END)

#function is called when the clear button ('X') is clicked
def button_last():
    entry.delete(len(entry.get())-1)

#function is called when the equal button ('=') is clicked.
def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, END)
    entry.insert(END, result)

# Create buttons and place them in the window
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        button = Button(frame3, text=buttons[i][j], padx=40, pady=20,bg="pink",font=('Arial', 14),highlightbackground="red",
                        command=lambda x=buttons[i][j]: button_click(x))
        button.grid(row=i+1, column=j)

# Create clear button
clear_button = Button(frame3, text='C', padx=40, pady=20,bg="pink",font=('Arial', 14), highlightbackground="pink",command=button_clear)
clear_button.grid(row=len(buttons)+1, column=0)

# Create equal button
equal_button = Button(frame3, text='=', padx=40, pady=20,bg="pink",font=('Arial', 14), highlightbackground="pink",command=button_equal)
equal_button.grid(row=len(buttons)+1, column=1)

# Create clear button for last character
clear_last = Button(frame3, text='X', padx=40, pady=20,bg="pink",font=('Arial', 14), highlightbackground="pink",command=button_last)
clear_last.grid(row=len(buttons)+1, column=2)

# Start the GUI event loop
window.mainloop()

