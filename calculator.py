import library.primops as primops
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import re 


main = tb.Window(size=(400, 450), themename="darkly")
main.title("calculator v0.1") 
display_var = tb.StringVar(value="0")
buttons_text = [["7","8","9","/"], ["4","5","6","*"], ["1","2","3","-"], ["C","0","=","+"]]
operator = ["/", "*", "-", "+"]

Style = tb.Style()
Style.configure('button.TButton', font=('Helvetica', 24))


def operatorcheck():
    current_text = display_var.get()
    current_ops = [op for op in operator if op in current_text]
    return len(current_ops)

def get_operator_simple(expression):
    """Checks the expression string for known arithmetic operators."""
    for op in operator:
        if op in expression:
            return op
    
    return None

def calculate():
    current_text = display_var.get()
    current_ops = get_operator_simple(current_text)
    abval = re.split(r"([+-/*])", current_text)
    a = float(abval[0])
    b = float(abval[2])
    result = round(primops.something(current_ops, a, b), 2)
    display_var.set(f"{result:g}")
    



def onclick(c):
    current_text = display_var.get()
    current_ops = operatorcheck()
    if c == "C":
        display_var.set("0")
    elif c == "=":
        print("calculating")
        calculate()
    elif c in operator:
        if current_text[-1] in operator:
            display_var.set(current_text.strip()[:-1] + c)
        elif current_text == "0":
            pass
        elif current_ops == 1 :
            pass
        else:
            display_var.set(current_text + c)
    else:
        if current_text == "None":
            display_var.set("0")
        else:
            pass
        if display_var.get() == "0":
            display_var.set(c)
        else:
            display_var.set(current_text + c)

for i in range(4):
    main.columnconfigure(i, weight=1)
for i in range(1,5):
    main.rowconfigure(i, weight=1)
for row in range(1, 5):
    for col in range (4):
        tb.Button(main, 
                  text=buttons_text[row - 1][col],
                  style=("button.TButton"),
                  command=lambda c = buttons_text[row - 1][col]: onclick(c)
                  ).grid(row = row, column=col, sticky="nsew")

tb.Label(
    main, 
    textvariable = display_var, 
    font=("Helvetica", 32), 
    anchor=E,            
    bootstyle="inverse-dark",
    padding=15               
).grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

main.mainloop()
