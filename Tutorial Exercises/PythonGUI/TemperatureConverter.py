import tkinter

def convert():
    if txt_f.get():
        lbl_c["text"] = str(round((5/9) * float(txt_f.get()) - 32.00, 2)) + " \N{DEGREE CELSIUS}"

window = tkinter.Tk()
window.title("Temperature Converter")

txt_f = tkinter.Entry(width=10)
txt_f.grid(row=0, column=0)

lbl_f = tkinter.Label(text="\N{DEGREE FAHRENHEIT}")
lbl_f.grid(row=0, column=1)

btn_convert = tkinter.Button(text="\N{RIGHTWARDS BLACK ARROW}", command=convert)
btn_convert.grid(row=0, column=2, padx=10)

lbl_c = tkinter.Label(text="\N{DEGREE CELSIUS}")
lbl_c.grid(row=0, column=4, padx=10)

window.mainloop()