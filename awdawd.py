import tkinter as tk

window = tk.Tk()
window.geometry("200x290")
window.title("Kalkulačka")
window.resizable(False, False)


def ac():
    ent.delete('0', tk.END)


def delete():
    ent.delete(len(ent.get())-1, tk.END)


def znak(znk):
    ent.insert(tk.END, znk)

def equal():
    try:
        vysledek = eval(ent.get())
        ent.delete("0", tk.END)
        ent.insert(tk.END, vysledek)
    except:
        ent.delete(0, tk.END)
        ent.insert(0, "Syntax error")

ent = tk.Entry(
    width=23,
    bg="grey",
    fg="white",
    font=("Calibri", 12)
)

ent.grid(column=0, row=0, sticky="W", columnspan=50)

btn_AC = tk.Button(
    text="AC",
    width=5,
    height=3,
    bg="dark grey",
    command=ac
)
btn_AC.grid(column=0, row=1, sticky="W")

btn_del = tk.Button(
    text="DEL",
    width=5,
    height=3,
    bg="dark grey",
    command=delete
)
btn_del.grid(column=1, row=1, sticky="W")

btn_procento = tk.Button(
    text="%",
    width=5,
    height=3,
    bg="dark grey"
)
btn_procento.grid(column=2, row=1, sticky="W")

btn_deleno = tk.Button(
    text="/",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak("/")
)
btn_deleno.grid(column=3, row=1, sticky="W")

btn_7 = tk.Button(
    text="7",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(7)
)
btn_7.grid(column=0, row=2, sticky="W")

btn_8 = tk.Button(
    text="8",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(8)
)
btn_8.grid(column=1, row=2, sticky="W")

btn_9 = tk.Button(
    text="9",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(9)
)
btn_9.grid(column=2, row=2, sticky="W")

btn_krat = tk.Button(
    text="X",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak("*")
)
btn_krat.grid(column=3, row=2, sticky="W")

btn_4 = tk.Button(
    text="4",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(4)
)
btn_4.grid(column=0, row=3, sticky="W")

btn_5 = tk.Button(
    text="5",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(5)
)
btn_5.grid(column=1, row=3, sticky="W")

btn_6 = tk.Button(
    text="6",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(6)
)
btn_6.grid(column=2, row=3, sticky="W")

btn_minus = tk.Button(
    text="-",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak("-")
)
btn_minus.grid(column=3, row=3, sticky="W")

btn_1 = tk.Button(
    text="1",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(1)
)
btn_1.grid(column=0, row=4, sticky="W")

btn_2 = tk.Button(
    text="2",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(2)
)
btn_2.grid(column=1, row=4, sticky="W")

btn_3 = tk.Button(
    text="3",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(3)
)
btn_3.grid(column=2, row=4, sticky="W")

btn_plus = tk.Button(
    text="+",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak("+")
)
btn_plus.grid(column=3, row=4, sticky="W")

btn_0 = tk.Button(
    text="0",
    width=11,
    height=3,
    bg="dark grey",
    command=lambda: znak(0)
)
btn_0.grid(column=0, columnspan=3, row=5, sticky="W")

btn_carka = tk.Button(
    text=",",
    width=5,
    height=3,
    bg="dark grey",
    command=lambda: znak(".")
)
btn_carka.grid(column=2, row=5, sticky="W")

btn_rovnitko = tk.Button(
    text="=",
    width=5,
    height=3,
    bg="dark grey",
    command=equal
)
btn_rovnitko.grid(column=3, row=5, sticky="W")


window.mainloop()