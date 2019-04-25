from tkinter import *
root=Tk()
root.title("Python Calculator")
scvalue1=StringVar()
scvalue1.set("")

screen=Entry(root,font=("arial",25,"bold"),text=scvalue1,fg='red',bg='white',justify='left',bd=10)
screen.pack(side=RIGHT)
scvalue2=StringVar()
scvalue2.set("")
screen=Entry(root,font=("arial",25,"bold"),text=scvalue2,fg='red',bg='white',justify='left',bd=10)
screen.pack(side=RIGHT)

root.geometry("500x700")
root.mainloop()

