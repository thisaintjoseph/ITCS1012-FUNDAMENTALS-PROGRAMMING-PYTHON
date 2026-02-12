import tkinter as tk

window = tk.Tk()

window.title("Student Profile")
window.geometry("600x600")
window.resizable(True,False)
window.configure(bg="brown",cursor="hand2")


label = tk.Label(window,text="Student Profile",font=("Calibri",65,"bold"),fg="black",bg="Brown")
label.pack(padx=30,pady=20)
tk.Label(window,text="Name:Joseph Afable",font=("Times New Roman",20),bg="Brown").pack(anchor="w")
tk.Label(window,text="Age:19",bg="Brown",font=("Calibri",20)).pack(anchor="w")
tk.Label(window,text="Course and Section:BSIT-1A",font=("Calibri",20),bg="Brown").pack(anchor="w")
tk.Label(window,text="Birthday:December 19,2006",bg="Brown",font=("Calibri",20)).pack(anchor="w")
tk.Label(window,text="Motto:Life is short, make it shorter",bg="Brown",font=("Calibri",20)).pack(anchor="w")

window.mainloop()
