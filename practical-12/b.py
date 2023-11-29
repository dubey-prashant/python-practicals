import tkinter as tk

root =tk.Tk()

label1 = tk.Label(root,text = "A list of favourite languages...")

listbox = tk.Listbox(root)
listbox.insert(1,"PHP")
listbox.insert(2, "Python")
listbox.insert(3, "Java")
listbox.insert(4, "C#")

label1.pack()
listbox.pack()

root.mainloop()
