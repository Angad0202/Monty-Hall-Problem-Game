import tkinter as tk
import io
import urllib
from PIL import Image, ImageEnhance
from PIL import ImageTk
import random
from time import sleep

def on_gate_click(event):
    global last_gate_clicked
    user_choice = event.widget['text']
    if last_gate_clicked:
        last_gate_clicked.config(bg='white')
    event.widget.config(bg='red')
    last_gate_clicked = event.widget
    text.delete('1.0', tk.END)
    text.insert(tk.END, "you selected "f"{user_choice}!")
    monty_choice = monty_selects_gate(gates, prize_gate, user_choice)
    text_monty.insert(tk.END, "monty selected "f"{monty_choice}!")
    switch_or_stay_label = tk.Label(text='Switch or Stay')
    switch_or_stay_label.place(x=250,y=500)
    switch_or_stay_label.config(font=("Courier", 20, "bold"), fg="blue")
    switch_button = tk.Button(text="Switch", command=lambda: switch(user_choice,monty_choice,prize_gate))
    switch_button.place(x=150,y=500)
    stay_button = tk.Button(text="Stay", command=lambda: reveal(user_choice,prize_gate))
    stay_button.place(x=500,y=500)

def reveal(user_choice,prize_gate):
    if user_choice==prize_gate:
        text_prize.insert(tk.END, "YOU WON")
    else:
        text_prize.insert(tk.END, "YOU LOST :(")

def switch(user_choice,monty_choice,prize_gate):
    if user_choice==prize_gate:
        
        text_prize.insert(tk.END, "YOU LOST:(")
    else:
        text_prize.insert(tk.END, "YOU WON!!!")



def monty_selects_gate(gates, prize_gate, user_choice):
    available_gates = list(filter(lambda x: x != prize_gate and x != user_choice, gates))
    monty_choice = random.choice(available_gates)
    return monty_choice

def choose_prize_gate(gates):
    prize_gate = random.choice(gates)
    return prize_gate

def play_again():
    text.delete('1.0', tk.END)
    text_monty.delete('1.0', tk.END)
    text_prize.delete('1.0', tk.END)
    global prize_gate
    prize_gate = choose_prize_gate(gates)



gates = ["Gate 1", "Gate 2", "Gate 3"]
last_gate_clicked = None
prize_gate = choose_prize_gate(gates)
root = tk.Tk()
root.title("Monty Hall Game")
root.geometry("720x600")

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.place(x=300,y=50)

text = tk.Text(root, height=1, width=20)
text.place(x=30,y=10)
text_monty = tk.Text(root, height=1, width=30)
text_monty.place(x=450,y=10)
text_prize = tk.Text(root, height=1, width=20)
text_prize.place(x=250,y=10)


gate1_image = Image.open("gate1.png")
gate1_image = ImageTk.PhotoImage(gate1_image)

gate1_label = tk.Label(root, image=gate1_image, text="Gate 1")
gate1_label.image = gate1_image
gate1_label.bind("<Button-1>", on_gate_click)
gate1_label.place(x=20,y=80)

gate2_image = Image.open("gate2.png")
gate2_image = ImageTk.PhotoImage(gate2_image)

gate2_label = tk.Label(root, image=gate2_image, text="Gate 2")
gate2_label.image = gate2_image
gate2_label.bind("<Button-1>", on_gate_click)
gate2_label.place(x=250,y=80)

gate3_image = Image.open("gate3.png")
gate3_image = ImageTk.PhotoImage(gate3_image)

gate3_label = tk.Label(root, image=gate3_image, text="Gate 3")
gate3_label.image = gate3_image
gate3_label.bind("<Button-1>", on_gate_click)
gate3_label.place(x=470,y=80)


root.mainloop()
