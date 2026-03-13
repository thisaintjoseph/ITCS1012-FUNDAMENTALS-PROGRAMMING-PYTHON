import tkinter as tk

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result_label.config(text=f"The Sum is {num1+num2}")
    except:
        result_label.config(text="wrong input")

def substract():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        result_label.config(text=f"Diff is {n1-n2}")
    except:
        result_label.config(text="wrong input")

def multiply():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_label.config(text=f"Multiply is {a*b}")
    except:
        result_label.config(text="wrong input")

def divide():
    try:
        x = float(entry1.get())
        y = float(entry2.get())
        if y == 0:
            result_label.config(text="cant divide by zero")
        else:
            result_label.config(text=f"Divide is {x/y}")
    except:
        result_label.config(text="wrong input")

window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg="#003049")

result_frame = tk.Frame(window, bg="#003049")
result_frame.pack(fill="x", side="top")
result_label = tk.Label(result_frame, text="Result here", bg="white", height=2)
result_label.pack(fill="x")

input_frame = tk.Frame(window, bg="#003049")
input_frame.pack(pady=10)
label1 = tk.Label(input_frame, text="Enter 1st Number:", bg="white")
label1.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(input_frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(input_frame, text="Enter 2nd Number:", bg="white")
label2.grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(input_frame)
entry2.grid(row=1, column=1, padx=5, pady=5)

button_frame = tk.Frame(window, bg="#003049")
button_frame.pack(pady=10)
btn1 = tk.Button(button_frame, text="Add", command=add)
btn1.grid(row=0, column=0, padx=5, pady=5)
btn2 = tk.Button(button_frame, text="Substract", command=substract)
btn2.grid(row=0, column=1, padx=5, pady=5)
btn3 = tk.Button(button_frame, text="Multiply", command=multiply)
btn3.grid(row=1, column=0, padx=5, pady=5)
btn4 = tk.Button(button_frame, text="Divide", command=divide)
btn4.grid(row=1, column=1, padx=5, pady=5)

window.mainloop()
