from tkinter import *
# Global variable to store the expression
expression = ""
# Function to update the expression in the input field
def press(key):
   global expression
   expression += str(key)
   input_text.set(expression)
# Function to evaluate the final expression
def equal():
   global expression
   try:
       result = str(eval(expression)) # Evaluate the expression
       input_text.set(result)
       expression = "" # Clear the expression after evaluation
   except:
       input_text.set("Error")
       expression = ""
# Function to clear the input field
def clear():
   global expression
   expression = ""
   input_text.set("")
# Main GUI window setup
root = Tk()
root.title("Simple Calculator")
root.geometry("312x324")
root.resizable(0, 0)
# StringVar to hold the input text
input_text = StringVar()
# Input field frame
input_frame = Frame(root, width=312, height=50, bd=0)
input_frame.pack(side=TOP)
# Input field widget
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
# Buttons frame
btns_frame = Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()
# Button layout and commands
buttons = [
   ('C', 1, 0, lambda: clear()), ('/', 1, 3, lambda: press('/')),
   ('7', 2, 0, lambda: press(7)), ('8', 2, 1, lambda: press(8)), ('9', 2, 2, lambda: press(9)), ('*', 2, 3, lambda: press('*')),
   ('4', 3, 0, lambda: press(4)), ('5', 3, 1, lambda: press(5)), ('6', 3, 2, lambda: press(6)), ('-', 3, 3, lambda: press('-')),
   ('1', 4, 0, lambda: press(1)), ('2', 4, 1, lambda: press(2)), ('3', 4, 2, lambda: press(3)), ('+', 4, 3, lambda: press('+')),
   ('0', 5, 0, lambda: press(0)), ('.', 5, 2, lambda: press('.')), ('=', 5, 3, lambda: equal())
]
for (text, row, col, cmd) in buttons:
   Button(btns_frame,
          text=text,
          fg="black",
          width=10,
          height=3,
          bd=0,
          bg="#fff" if text.isdigit() else "#eee",
          cursor="hand2",
          command=cmd).grid(row=row -1 if text == 'C' else row,
                            column=col,
                            padx=1,
                            pady=1)
root.mainloop()