import tkinter as tk
import os
from random import *
root = tk.Tk()
root.title("Stone Paper Scissors")
root.resizable(False,False)
c = tk.Canvas(width=1000, height=1000)
c.pack()
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir,"assets","icon.ico")
root.iconbitmap(icon_path)
bg_path = os.path.join(script_dir,"assets", "bg.gif")
bg_image = tk.PhotoImage(file=bg_path)
c.create_image(0, 0, image=bg_image,anchor="nw")
top_label = tk.Label(root, text="STONE PAPER SCISSORS",font=("Bahnschrift", 20, "bold"))
c.create_window(500,40, window=top_label)
label1 = tk.Label(root, text="You", font=("Bell MT",16, "bold"))
label2 = tk.Label(root, text="Computer", font=("Bell MT",16,"bold"))
c.create_window(333,250, window=label1)
c.create_window(666,250, window=label2)
c.create_rectangle(300,270, 366, 320,fill="white")
c.create_rectangle(633,270, 699, 320, fill="white")
global score
score = 0
global comp_score 
comp_score = 0 
user_score_label = tk.Label(root, text=f"{score}", font=("Times New Roman",20,"bold"))
comp_score_label = tk.Label(root, text=f"{comp_score}",font=("Times New Roman",20,"bold"))
c.create_window(333,295,window=user_score_label)
c.create_window(666,295,window=comp_score_label)
options=["stone","paper","scissors"]

condition_label = tk.Label(root, text="Lets start the game!",font=("Cooper",20))
c.create_window(500, 390,window=condition_label)
def play(user):
    comp_choice=choice(options)
    global score, comp_score
    if comp_choice==user:
        result="IT'S A TIE!"
        
        score += 0.5
        comp_score += 0.5
    elif (user=="paper" and comp_choice=="stone") or (user=="stone" and comp_choice=="scissors") or (user=="scissors" and comp_choice=="paper"):
        result = "YOU WIN!"
        score+=1
    else:
        result = "YOU LOSE!"
        comp_score += 1
    condition_label.config(text=f"{result}")
    user_score_label.config(text=f"{score}")
    comp_score_label.config(text=f"{comp_score}")
stone_btn = tk.Button(root, text="Stone",font=("Arial",20,"bold"),command=lambda: play("stone"),bg="#7C7C7C",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#7C7C7C")
paper_btn = tk.Button(root, text="Paper",font=("Arial",20,"bold"),command= lambda: play("paper"),bg="#FFFFFF",fg="#000000",activebackground="#000000",activeforeground="#FFFFFF")
scissor_btn = tk.Button(root, text="Scissors",font=("Arial",20,"bold"), command=lambda: play("scissors"),bg="#1E3A8A",fg="#FFD700",activebackground="#FFD700",activeforeground="#1E3A8A")
c.create_window(270,550,window=stone_btn)
c.create_window(470,550,window=paper_btn)
c.create_window(700,550,window=scissor_btn)
root.mainloop()