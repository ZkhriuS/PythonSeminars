# Создайте программу для игры в ""Крестики-нолики"".
from tkinter import *
from tkinter import messagebox


def set():
    global state_X
    global state_O
    draw = True
    row = int(spinbox[0].get())-1
    column = int(spinbox[1].get())-1
    if field[row*3+column].cget("text") not in "XO":
        field[row*3+column].config(text=player_label.cget("text"),
                                   fg=player_label.cget("fg"))
        if player_label.cget("text") == "X":
            player_label.config(text="O", fg="red")
            state_X = state_X + 2**(row*3+column)
            for i in win_states:
                if (state_X & i) == i:
                    messagebox.showinfo("Победитель", "X")
                    window.quit()
                    draw = False
        else:
            player_label.config(text="X", fg="blue")
            state_O = state_O + 2**(row*3+column)
            for i in win_states:
                if (state_O & i) == i:
                    messagebox.showinfo("Победитель", "O")
                    window.quit()
                    draw = False
        for item in field:
            if item.cget("text") not in "XO":
                draw = False
        if draw:
            messagebox.showinfo("Победитель", "Ничья!")
            window.quit()


win_states = (7, 56, 448, 73, 146, 292, 273, 84,
              15, 23, 39, 71, 135, 263, 31, 47, 79, 143, 271, )
window = Tk()
window.title("Крестики-нолики")
window.geometry("500x350+600+200")
window.resizable(False, False)
window.config(bg='yellow', padx=90, pady=50)
size = 3
width = 20
state_X = 0
state_O = 0
player_label = Label(window, text="X", font=(
    "Courier New", 16, "bold"), bg="yellow", fg="blue")
player_label.grid(column=1, row=0)
horizontal = Label(window, text="row", font=(
    "Courier New", 14, "bold"), bg="yellow", fg="purple")
horizontal.grid(column=0, row=1)
vertical = Label(window, text="column", font=(
    "Courier New", 14, "bold"), bg="yellow", fg="purple")
vertical.grid(column=0, row=2)
field = []
for i in range(size):
    for j in range(size):
        field.append(Label(window, text="_", font=(
            "Courier New", 16, "bold"), bg="white", fg="blue"))
        field[i*3+j].grid(column=j+2, row=i, padx=20, pady=20)
spinbox = [Spinbox(window, from_=1, to=size, font=(
    "Courier New", 16, "bold"), width=4), Spinbox(window, from_=1, to=size, font=(
        "Courier New", 16, "bold"), width=4)]
spinbox[0].grid(column=1, row=1)
spinbox[1].grid(column=1, row=2)
button_go = Button(window, text="Сделать ход", font=(
    "Courier New", 14, "bold"), bg="lightgreen", fg="black", command=set)
button_go.grid(column=1, row=3)
window.mainloop()
