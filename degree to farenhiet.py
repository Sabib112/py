import tkinter as tk

window=tk.Tk()
window.title('imperial to metric temperature converter')
window.resizable(width=False, height=False)



frm_entry = tk.Frame(master=window)
ent_temp = tk.Entry(master=frm_entry, width=10)
lbl_temp= tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temp.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0 , column=1, sticky="w")


lbl_result= tk.Label(master=window ,text= '\N{DEGREE CELSIUS}')

def farenheit_to_celsius():
    farenheit = ent_temp.get()
    celsius = (5/9)*(float(farenheit)-32)
    lbl_result['text']= f'{round(celsius, 2)} \N{DEGREE CELSIUS}'

btn_convert = tk.Button(
    master=window,
    text='--->',
    command=farenheit_to_celsius,
)

frm_entry.grid(row=0,column=0,padx=10)
btn_convert.grid(row=0,column=1,pady=10)
lbl_result.grid(row=0,column=2,padx=10)
window.mainloop()