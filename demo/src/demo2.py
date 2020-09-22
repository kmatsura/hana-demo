import tkinter as tk

def say_hello():
    print("Hello", flush=True)

root = tk.Tk()
root.title("HANA")
label = tk.Label(root, text="test_label")
label.pack()
entry = tk.Entry(master=root, width=10)
entry.pack()
entry.insert(0, "Hello")
bt = tk.Button(master=root, text="Say", command=say_hello)
bt.pack()
root.mainloop()