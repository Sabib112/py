
from tkinter import *
from tkinter import messagebox
from PIL  import Image, ImageTk

root = Tk()
root.title("Denomination Calculator")
root.configure(bg="lightblue")
root.geometry("680x400")

upload = Image.open("denomination.png")
upload = upload.resize((380,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="lightblue")
label.place(x=180, y=20)

label1 = Label(root, text="hey user! welcome to denomination calculator application", bg="lightblue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "alert", "do you want to count the denomination count?")
    if MsgBox == 'ok':
        topwin()
    
button1 = Button(root, text="lets start",command=msg, bg="brown", fg="white")
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Count")
    top.configure(bg="lightgrey")
    top.geometry("600x350+50+50")

    label= Label(top, text="Enter total amount", bg="lightgrey")
    entry= Entry(top)
    lbl= Label(top, text="Denomination Count", bg="lightgrey")

    l1 = Label(top, text="2000", bg="lightgrey")
    l2 = Label(top, text="500", bg="lightgrey")
    l3 = Label(top, text="100", bg="lightgrey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)