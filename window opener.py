from tkinter import*
 
root=Tk()
root.geometry("400x300")
root.title("main")


def topwin():
    top=toplevel()
    top.geometry("180x100")
    top.title("top level")

    l2=Label(top,text="This is a top level window")
    l2.pack()
     
    top.mainloop()

l =Label(root,text="This is a root window")
btn = Button(root,text="Open Top Level Window",command=topwin)

l.pack()
btn.pack()
