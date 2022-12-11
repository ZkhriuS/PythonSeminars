# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from tkinter import *
from tkinter import messagebox
from random import randint


def game_window(mode: int):
    window.config(bg='yellow', padx=25, pady=90)
    button_friend_game.destroy()
    button_bot_game.destroy()
    first_player_lbl.grid(column=0, row=0, padx=10)
    sweets.grid(column=1, row=0, padx=10)
    second_player_lbl.grid(column=2, row=0, padx=10)
    if mode == 1:
        button_go_friend.grid(column=1, row=1, pady=40)
    else:
        button_go_bot.grid(column=1, row=1, pady=40)
    sweets_count[0].grid(column=0, row=1)
    sweets_count[1].grid(column=2, row=1)
    sweet_spinbox[0].grid(column=0, row=2)
    sweet_spinbox[1].grid(column=2, row=2)
    if mode == 1:
        sweet_spinbox[0].config(state="normal")
        sweet_spinbox[1].config(state="disabled")
    else:
        sweet_spinbox[0].config(state="disabled")
        sweet_spinbox[1].config(state="disabled")
        value = randint(0, 1)
        sweet_spinbox[value].config(state="normal")


def take_sweets_friend():
    if int(sweets.cget("text")[9:]) > max_sweets:
        if sweet_spinbox[0].cget("state") == "normal":
            num_sweets = int(sweets.cget("text")[
                             9:]) - int(sweet_spinbox[0].get())
            sweet_spinbox[1].config(state="normal")
            sweet_spinbox[0].config(state="disabled")
            sweets_count[0].config(
                text=str(int(sweets_count[0].cget("text"))+int(sweet_spinbox[0].get())))
        elif sweet_spinbox[1].cget("state") == "normal":
            num_sweets = int(sweets.cget("text")[
                             9:]) - int(sweet_spinbox[1].get())
            sweet_spinbox[0].config(state="normal")
            sweet_spinbox[1].config(state="disabled")
            sweets_count[1].config(
                text=str(int(sweets_count[1].cget("text"))+int(sweet_spinbox[1].get())))
    else:
        num_sweets = 0
        winner = 1 if sweet_spinbox[0].cget("state") == "normal" else 2
        messagebox.showinfo("Победитель", str(winner)+"-й игрок")
        window.quit()
    sweets.config(text="Конфеты: "+str(num_sweets))


def take_sweets_bot():
    gamer = 0 if sweet_spinbox[0].cget("state") == "normal" else 1
    bot = 0 if sweet_spinbox[0].cget("state") == "disabled" else 1
    if int(sweets.cget("text")[9:]) > max_sweets:
        num_sweets = int(sweets.cget("text")[
                         9:]) - int(sweet_spinbox[gamer].get())
        sweets_count[gamer].config(text=str(
            int(sweets_count[gamer].cget("text"))+int(sweet_spinbox[gamer].get())))
        sweet_spinbox[gamer].config(state="disabled")
        sweets.config(text="Конфеты: "+str(num_sweets))
        if int(sweets.cget("text")[9:]) > max_sweets:
            num_sweets = int(sweets.cget("text")[9:])
            if bot == 0:
                if num_sweets % (max_sweets+1) != 0:
                    count = num_sweets % (max_sweets+1)
                else:
                    count = max_sweets+1 - int(sweet_spinbox[gamer].get())
            else:
                count = randint(1, 28)
            sweets_count[bot].config(
                text=str(int(sweets_count[bot].cget("text"))+count))
            num_sweets -= count
            sweet_spinbox[gamer].config(state="normal")
    else:
        num_sweets = 0
        winner = "Вы" if sweet_spinbox[gamer].cget(
            "state") == "normal" else "Бот"
        messagebox.showinfo("Победитель", winner)
        window.quit()
    sweets.config(text="Конфеты: "+str(num_sweets))


def menu():
    window.config(bg='yellow', padx=150, pady=90)
    button_friend_game.grid(column=0, row=0)
    button_bot_game.grid(column=0, row=1, pady=10)


num_sweets = 2021
max_sweets = 28
window = Tk()
window.title("Игра с конфетами")
window.geometry("500x300+600+200")
window.resizable(False, False)
button_friend_game = Button(window, text="Игра с друзьями", font=(
    "Courier New", 16, "bold"), width=16, bg="blue", fg="white", command=lambda mode=1: game_window(mode))
button_bot_game = Button(window, text="Игра с ботом", font=(
    "Courier New", 16, "bold"), width=16, bg="blue", fg="white", command=lambda mode=2: game_window(mode))
button_go_friend = Button(window, text="Сделать ход", font=(
    "Courier New", 14, "bold"), bg="lightgreen", fg="black", command=take_sweets_friend)
button_go_bot = Button(window, text="Сделать ход", font=(
    "Courier New", 14, "bold"), bg="lightgreen", fg="black", command=take_sweets_bot)
sweets = Label(window, text="Конфеты: "+str(num_sweets), font=(
    "Courier New", 16, "bold"), bg="yellow", fg="purple")
sweets_count = [Label(window, text="0", font=(
    "Courier New", 16, "bold"), bg="yellow", fg="purple"), Label(window, text="0", font=(
        "Courier New", 16, "bold"), bg="yellow", fg="purple")]
first_player_lbl = Label(window, text="Первый игрок", font=(
    "Courier New", 10, "bold"), bg="yellow", fg="blue")
second_player_lbl = Label(window, text="Второй игрок", font=(
    "Courier New", 10, "bold"), bg="yellow", fg="red")
sweet_spinbox = [Spinbox(window, from_=1, to=max_sweets, font=(
    "Courier New", 16, "bold"), width=4), Spinbox(window, from_=1, to=max_sweets, font=(
        "Courier New", 16, "bold"), width=4)]
menu()
window.mainloop()
