from tkinter import *
root=Tk()
Label(root, text="First").grid(row=0, sticky=W)
Label(root, text="Second").grid(row=1, sticky=W)

entry1 = Entry(root)
entry1 = Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

checkbutton.grid(columnspan=2, sticky=W)

image.grid(row=0, column=2, columnspan=2, rowspan=2,
           sticky=W+E+N+S, padx=5, pady=5)

button1.grid(row=2, column=2)
button2.grid(row=2, column=3)
