import tkinter as tk
import math

calc_rt = tk.Tk()
calc_rt.configure(bg="#293C4A", bd=10)
calc_rt.title("Scientific Calculator")

exp = ""
dis = ""
text = tk.StringVar()

dis_Win = tk.Entry(calc_rt, font=('sans-serif', 20, 'bold'), width=30, textvariable=text,
                   bd=5, insertwidth=5, bg='#BBB', justify='right')
dis_Win.grid(columnspan=6, padx=10, pady=15)

parameters = [{'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')},
              {'bd': 5, 'fg': '#000', 'bg': '#db701f', 'font': ('sans-serif', 20, 'bold')},
              {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('sans-serif', 20, 'bold')}]

buttons = {'sin': 'sin(', 'cos': 'cos(', 'tan': 'tan(', 'π': 'π', '%': '%',
           'x²': '²', 'x³': '³', 'x^n': '^', 'x⁻¹': '⁻¹', '√': '√(',
           'log₁₀': 'log₁₀(', 'ln': 'ln(', 'e': 'e', '10^x': '10^', 'abs': 'abs(',
           'DEL': 'DEL', 'AC': 'AC', '7': '7', '8': '8', '9': '9',
           '(': '(', ')': ')', '4': '4', '5': '5', '6': '6',
           '*': '*', '/': '/', '1': '1', '2': '2', '3': '3',
           '+': '+', '-': '-', '=': '=', '.': '.', '0': '0'}

replace = {'sin(': 'math.sin(', 'cos(': 'math.cos(', 'tan(': 'math.tan(', 'π': str(math.pi), '%': '*0.01',
           '²': '**2', '³': '**3', '^': '**', '⁻¹': '**(-1)', '√(': 'math.sqrt(',
           'log₁₀(': 'math.log10(', 'ln(': 'math.log(', 'e': 'math.exp(1)', '10^': '10**', 'abs(': 'abs(',
           'DEL': '', 'AC': '', '9': '9', '8': '8', '7': '7',
           '(': '(', ')': ')', '4': '4', '5': '5', '6': '6',
           '*': '*', '/': '/', '1': '1', '2': '2', '3': '3',
           '+': '+', '-': '-', '=': '', '.': '.', '0': '0'}


def button_click(ch):
    global exp
    global dis

    if "Error" in dis:
        exp = ""
        dis = ""

    if ch == 'AC':
        exp = ""
        dis = ""
    elif ch == 'DEL':
        exp = exp[:-1]
        dis = dis[:-1]
    elif ch == '=':
        if dis:
            try:
                dis = str(eval(exp))
                exp = dis
            except ZeroDivisionError:
                dis = "Error: Cannot divide by zero"
            except SyntaxError:
                dis = "Syntax Error"
            except Exception:
                dis = "Error"
    else:
        dis += ch
        exp += replace[ch]
    text.set(dis)


i = 0
for b, c in buttons.items():
    tk.Button(calc_rt, parameters[((i >= 15) + (i >= 17))], text=b,
              command=lambda char=c: button_click(char)).grid(row=i // 5 + 1, column=i % 5 + 1, sticky="nsew")
    i += 1

calc_rt.mainloop()
