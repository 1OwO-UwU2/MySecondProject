import tkinter as tk
root = tk.Tk()
root.title("OwO")

def Amogus():
    print("Sus")

def Addition():
    a = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(a + float(entry.get())))

def subtraction():
    a = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(a - float(entry.get())))

def multiplication():
    a = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, str(a * float(entry.get())))

def division():
    a = float(entry.get())
    if float(entry.get()) != 0:
        entry.delete(0, tk.END)
        entry.insert(0, str(a * float(entry.get())))
    else:
       entry.delete(0, tk.END)
       entry.insert(0, "error - Неможливо ділити на нуль")
def NumberClick(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

row = 1
col = 0
entry = tk.Entry(root, widt= 35, borderwidth= 5)
entry.grid(row= 0, column= 0, columnspan= 4,)     
buttons = ["1", "2", "3", "+",
"4", "5", "6", "-",
"7", "8", "9", "*",
"0", "/", "=", "C"]
for i in buttons:
    if i == "C":
         tk.Button(root, text= i,padx=40, pady=20, command= lambda: entry.delete(0, tk.END)).grid(row=row, column=col)
    else:
        tk.Button(root, text= i,padx=40, pady=20, command= lambda num = i:NumberClick(num)).grid(row=row, column=col)
    col += 1
    if col > 3:
        row += 1
        col = 0
root.mainloop ()
 
    #qqqqqqqqqqqqqq@