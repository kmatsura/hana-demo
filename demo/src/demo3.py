import tkinter as tk


def pushed(num):
    name = entry0.get()
    response = f"{name}さん\nボタン{num}が押されました。"
    label0.config(text = response)

root = tk.Tk()
label0 = tk.Label(root)
label0.pack()
entry0 = tk.Entry(root)
entry0.pack()
buttons = []
for num in range(4):
    buttons.append(tk.Button(master=root, text=f"ボタン{num}", command = lambda x = num : pushed(x)))
    buttons[num].pack()
root.mainloop()