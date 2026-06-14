import math
import tkinter as tk

root = tk.Tk()
root.resizable(False,False)
root.title("PyCalculator")
root.configure(bg="#1e1e1e")

display = tk.Entry(root, width=10, borderwidth=10, font=("Arial", 28), justify="right")
display.grid(row=0, columnspan=4, padx=10, pady=10, sticky="ew")

calculated = False

def clear():
    global calculated
    calculated = False
    display.delete(0, tk.END)

def press(key):
    global calculated
    if calculated:
        if str(key) not in ["+", "-", "*", "/", "^"]:
            display.delete(0, tk.END)
        calculated = False
    display.insert(tk.END, key)

def backspace():
    global calculated
    current = display.get()
    if current == "Error":
        display.delete(0, tk.END)
    else:
        display.delete(0, tk.END)
        display.insert(tk.END, current[:-1])
    calculated = False

def square():
    global calculated
    try:
        result = float(display.get())**2
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")
    calculated = True

def square_root():
    global calculated
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")
    calculated = True

def safe(expression):
    characters = "0123456789+-*/(). "
    for char in expression:
        if char not in characters:
            return False
    return True

def calculate():
    global calculated
    try:
        expression = display.get().replace("^", "**")
        display.delete(0, tk.END)
        if not safe(expression):
            display.insert(tk.END, "Error")
            calculated = True
            return
        result = eval(expression)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
    calculated = True

btn1 = tk.Button(root, text="1", width=10, height=3, command=lambda: press(1),)
btn2 = tk.Button(root, text="2", width=10, height=3, command=lambda: press(2))
btn3 = tk.Button(root, text="3", width=10, height=3, command=lambda: press(3))
btn4 = tk.Button(root, text="4", width=10, height=3, command=lambda: press(4))
btn5 = tk.Button(root, text="5", width=10, height=3, command=lambda: press(5))
btn6 = tk.Button(root, text="6", width=10, height=3, command=lambda: press(6))
btn7 = tk.Button(root, text="7", width=10, height=3, command=lambda: press(7))
btn8 = tk.Button(root, text="8", width=10, height=3, command=lambda: press(8))
btn9 = tk.Button(root, text="9", width=10, height=3, command=lambda: press(9))
btn0 = tk.Button(root, text="0", width=10, height=3, command=lambda: press(0))
btn_dot = tk.Button(root, text=".", width=10, height=3, command=lambda: press('.'))
btn_equal = tk.Button(root, text="=", width=10, height=3, command=lambda: calculate())
btn_add = tk.Button(root, text="+", width=10, height=3, command=lambda: press('+'))
btn_subtract = tk.Button(root, text="-", width=10, height=3, command=lambda: press('-'))
btn_multiply = tk.Button(root, text="*", width=10, height=3, command=lambda: press('*'))
btn_divide = tk.Button(root, text="/", width=10, height=3, command=lambda: press('/'))
btn_back = tk.Button(root, text="⌫", width=10, height=3, command=backspace)
btn_sqrt = tk.Button(root, text="√", width=10, height=3, command=square_root)
btn_square = tk.Button(root, text="x²", width=10, height=3, command=square)
btn_power = tk.Button(root, text="xʸ", width=10, height=3, command=lambda: press('^'))

btn_left_bracket = tk.Button(root, text="(", width=10, height=3, command=lambda: press("("))
clear_btn = tk.Button(root, text="C", width=21, height=3, command=clear)
btn_right_bracket = tk.Button(root, text=")", width=10, height=3, command=lambda: press(")"))

btn_power.grid(row=1, column=0)
btn_square.grid(row=1, column=1)
btn_sqrt.grid(row=1, column=2)
btn_back.grid(row=1, column=3)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)

btn_dot.grid(row=5, column=0)
btn0.grid(row=5, column=1)
btn_equal.grid(row=5, column=2)
btn_add.grid(row=2, column=3)
btn_subtract.grid(row=3, column=3)
btn_multiply.grid(row=4, column=3)
btn_divide.grid(row=5, column=3)

btn_left_bracket.grid(row=6, column=0)
clear_btn.grid(row=6, column=1, columnspan=2)
btn_right_bracket.grid(row=6, column=3)

root.mainloop()