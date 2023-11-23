import tkinter as tk

app = tk.Tk()
app.minsize(400, 500)
a = tk.Radiobutton(app, text='bouttona', command=lambda: print("a"); app.destroy())
b = tk.Radiobutton(app, text='bouttonb', command=lambda: )
#a.deselect()
a.pack()
b.pack()
app.mainloop()