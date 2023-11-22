import tkinter as tk

app = tk.Tk()
app.minsize(400, 500)
a = tk.Radiobutton(app, text='bouttona')
b = tk.Radiobutton(app, text='bouttonb')
a.deselect()
a.pack()
b.pack()
app.mainloop()