import tkinter as tk


root = tk.Tk()
root.geometry("200x300")
root.title('GIAIN')
root.configure(bg="black")
e1 = tk.Text(root)
e1.place(x=10, y=35, height=50, width=180)
l1 = tk.Label(root, text="Output")
l1.place(x=10, y=5)

e2 = tk.Text(root)
e2.place(x=10, y=150, height=30, width=180)
l2 = tk.Label(root, text="You said")
l2.place(x=10, y=120)
b = tk.Button(root, text="Speak", bg="red", fg="white")
b.place(x=50, y=200, height=50, width=100)
root.mainloop()