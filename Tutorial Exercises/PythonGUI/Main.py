import tkinter
import random

border_effects = {
    "flat": tkinter.FLAT,
    "sunken": tkinter.SUNKEN,
    "raised": tkinter.RAISED,
    "groove": tkinter.GROOVE,
    "ridge": tkinter.RIDGE,
}

def basic():
    window = tkinter.Tk()
    window.title("Basic")

    label = tkinter.Label(text="Hello, Tkinter", fg="white", bg="black")
    label.pack()

    button = tkinter.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow", )
    button.pack()

    entry = tkinter.Entry(fg="yellow", bg="blue", width=50)
    entry.pack()

    window.mainloop()

def basic_frames():
    window = tkinter.Tk()
    window.title("Basic Frames")

    frame_a = tkinter.Frame()
    frame_b = tkinter.Frame()

    label_a = tkinter.Label(master=frame_a, text="I'm in Frame A")
    label_a.pack()

    label_b = tkinter.Label(master=frame_b, text="I'm in Frame B")
    label_b.pack()

    frame_b.pack()
    frame_a.pack()

    frame1 = tkinter.Frame(master=window, width=100, height=100, bg="red")
    frame1.pack(fill=tkinter.X)

    frame2 = tkinter.Frame(master=window, width=50, height=50, bg="yellow")
    frame2.pack()

    frame3 = tkinter.Frame(master=window, width=25, height=25, bg="blue")
    frame3.pack(fill=tkinter.X)

    frame = tkinter.Frame(master=window, width=150, height=150)
    frame.pack()

    label1 = tkinter.Label(master=frame, text="I'm at (0, 0)", bg="red")
    label1.place(x=0, y=0)

    label2 = tkinter.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
    label2.place(x=75, y=75)

    label3 = tkinter.Label(master=frame, text="I'm at (50, 100)", bg="green")
    label3.place(x=50, y=100)

    window.mainloop()

def frame_borders():
    window = tkinter.Tk()
    window.title("Frame Borders")

    for relief_name, relief in border_effects.items():
        frame = tkinter.Frame(master=window, relief=relief, borderwidth=5)
        frame.pack(side=tkinter.RIGHT)
        label = tkinter.Label(master=frame, text=relief_name)
        label.pack()

    window.mainloop()

def grid():
    window = tkinter.Tk()
    window.title("Grid")

    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)

        for j in range(3):
            frame = tkinter.Frame(
                master=window,
                relief=tkinter.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            label = tkinter.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack(padx=5, pady=5)

    window.mainloop()

def grid1():
    window = tkinter.Tk()
    window.title("Grid 1")

    window.rowconfigure(0, minsize=50)
    window.columnconfigure([0, 1, 2, 3], minsize=50)

    label1 = tkinter.Label(text="1", bg="black", fg="white")
    label2 = tkinter.Label(text="2", bg="black", fg="white")
    label3 = tkinter.Label(text="3", bg="black", fg="white")
    label4 = tkinter.Label(text="4", bg="black", fg="white")

    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1, sticky="ew")
    label3.grid(row=0, column=2, sticky="ns")
    label4.grid(row=0, column=3, sticky="nsew")

    window.mainloop()

def address_entry_form():
    window = tkinter.Tk()
    window.title("Address Entry Form")

    frame_form = tkinter.Frame(master=window, borderwidth=3, relief=tkinter.SUNKEN)
    frame_form.pack()

    lbl_frst_nme = tkinter.Label(master=frame_form, text="First Name:")
    lbl_frst_nme.grid(row=0, column=0, sticky="e")
    txt_frst_nme = tkinter.Entry(master=frame_form, width=50)
    txt_frst_nme.grid(row=0, column=1)

    lbl_last_nme = tkinter.Label(master=frame_form, text="Last Name:")
    lbl_last_nme.grid(row=1, column=0, sticky="e")
    txt_last_nme = tkinter.Entry(master=frame_form, width=50)
    txt_last_nme.grid(row=1, column=1)

    lbl_addr1 = tkinter.Label(master=frame_form, text="Address Line 1:")
    lbl_addr1.grid(row=2, column=0, sticky="e")
    txt_addr1 = tkinter.Entry(master=frame_form, width=50)
    txt_addr1.grid(row=2, column=1)

    lbl_addr2 = tkinter.Label(master=frame_form, text="Address Line 2:")
    lbl_addr2.grid(row=3, column=0, sticky="e")
    txt_addr2 = tkinter.Entry(master=frame_form, width=50)
    txt_addr2.grid(row=3, column=1)

    lbl_city = tkinter.Label(master=frame_form, text="City:")
    lbl_city.grid(row=4, column=0, sticky="e")
    txt_city = tkinter.Entry(master=frame_form, width=50)
    txt_city.grid(row=4, column=1)

    lbl_stat = tkinter.Label(master=frame_form, text="State/Province:")
    lbl_stat.grid(row=5, column=0, sticky="e")
    txt_stat = tkinter.Entry(master=frame_form, width=50)
    txt_stat.grid(row=5, column=1)

    lbl_pstl_cde = tkinter.Label(master=frame_form, text="Postal Code:")
    lbl_pstl_cde.grid(row=6, column=0, sticky="e")
    txt_pstl_cde = tkinter.Entry(master=frame_form, width=50)
    txt_pstl_cde.grid(row=6, column=1)

    lbl_ctry = tkinter.Label(master=frame_form, text="Country:")
    lbl_ctry.grid(row=7, column=0, sticky="e")
    txt_ctry = tkinter.Entry(master=frame_form, width=50)
    txt_ctry.grid(row=7, column=1)

    frame_buttons = tkinter.Frame(master=window, borderwidth=3)
    frame_buttons.pack(fill=tkinter.X, ipadx=5, ipady=5)

    btn_sbmt = tkinter.Button(master=frame_buttons, text="Submit")
    btn_sbmt.pack(side=tkinter.RIGHT, padx=10, ipadx=10)

    btn_clr = tkinter.Button(master=frame_buttons, text="Clear")
    btn_clr.pack(side=tkinter.RIGHT, ipadx=10)

    window.mainloop()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Write a program that simulates rolling a six-sided die. There should be one button with the text "Roll".
# When the user clicks the button, a random integer from 1 to 6 should be displayed.
def roll_die():
    window = tkinter.Tk()
    window.title("Roll Die")
    window.columnconfigure(0, minsize=150)
    window.rowconfigure([0, 1], minsize=50)

    def roll():
        lbl_result["text"] = str(random.randint(1, 6))

    btn_roll = tkinter.Button(text="Roll", command=roll)
    lbl_result = tkinter.Label()
    btn_roll.grid(row=0, column=0, sticky="nsew")
    lbl_result.grid(row=1, column=0)

    window.mainloop()

if __name__ == '__main__':

    basic()

    basic_frames()
    frame_borders()

    grid()
    grid1()

    address_entry_form()

    # event handling
    window = tkinter.Tk()
    window.bind("<Key>", handle_keypress)
    window.mainloop()

    # Write a program that simulates rolling a six-sided die. There should be one button with the text "Roll".
    # When the user clicks the button, a random integer from 1 to 6 should be displayed.
    roll_die()
