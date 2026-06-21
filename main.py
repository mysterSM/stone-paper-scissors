import tkinter as tk
import os
import DecisionEngine #this serves as our game engine
import random 

#initialisation of GUI
root = tk.Tk()
root.geometry("1920x1080")
root.title("Stone Paper Scissors")
c = tk.Canvas(width=1920, height=1080)
assets_dir = os.path.dirname((os.path.abspath(__file__)))
bg_path = os.path.join(assets_dir, "assets", "bg.png")
icon_path = os.path.join(assets_dir, "assets", "icon.ico")
root.iconbitmap(icon_path)
bg_image = tk.PhotoImage(file=bg_path)
c.create_image(0, -15, image=bg_image, anchor="nw")
c.pack()

score = 0
comp_score = 0
options = ["stone", "paper", "scissors"]

#Labels
user_score_label = tk.Label(root, text=f"{score}", font=("Bahnschrift", 32, "bold"), bg="#FFFFFF")
comp_score_label = tk.Label(root, text=f"{comp_score}", font=("Bahnschrift", 32, "bold"), bg="#FFFFFF")

totalrounds = 0

def reset(): #reset function
    global score, comp_score, totalrounds
    score = 0
    comp_score = 0
    user_score_label.config(text=f"{score}")
    comp_score_label.config(text=f"{comp_score}")
    DecisionEngine.history=[]
    totalrounds = 0
    c.itemconfig(text_id, text="Let's start the game!")

def check_result(user_move, computer_move): #checks final result
    global score, comp_score
    if user_move==computer_move:
        result = "IT'S A TIE!"
        score+=0.5
        comp_score+=0.5
    elif user_move=="stone" and computer_move=="scissors" or \
        user_move=="paper" and computer_move=="stone" or \
        user_move=="scissors" and computer_move=="paper":
        result = "YOU WIN!"
        score += 1
    else:
        result="YOU LOST!"
        comp_score += 1

    c.itemconfig(text_id, text=result)
    user_score_label.config(text=str(score))
    comp_score_label.config(text=str(comp_score))

def log_move(move): #logs user moves and sends to DecisionEngine for prediction
    global totalrounds
    totalrounds+=1
    if(totalrounds<5):
        comp_choice = random.choice(options)
        check_result(move, comp_choice)
    elif(totalrounds>=5):
        comp_choice = DecisionEngine.boot()
        check_result(move, comp_choice)
    DecisionEngine.record_move(move)

c.create_rectangle(400, 500, 500, 430, fill="white", width=3)#User score rectangle
c.create_rectangle(800, 500, 900, 430, fill="white", width=3)#Computer score rectangle
c.create_window(450, 465, window=user_score_label)#User score
c.create_window(850, 465, window=comp_score_label)#Computer score
c.create_text(450, 525, text="You", fill="#A30000", font=("Bernard MT", 30, "bold"), justify="center")
c.create_text(650, 50, text="STONE PAPER SCISSORS", fill="#A855F7",font=("Bernard MT", 30, "bold"),
               justify="center")
c.create_text(850, 525, text="Quarizon AI", fill="#5f0d58", font=("Bernard MT",30,"bold"),
               justify="center")
text_id = c.create_text(650, 200, text="Let's start the game!", fill="#9E9C9C", font=("Bernard MT", 30, "bold"),
                         justify="center")
#Buttons
quit_btn = tk.Button(text="QUIT", font=("Bahnschrift", 18, "bold"),
                      command=root.destroy, width=8, height=1, bd=3, bg="#050046")
reset_btn = tk.Button(text="RESET", font=("Bahnschrift", 18, "bold"),
                       command=lambda: reset(), width=8, height=1, bd=3, bg="#944300")
stone_btn = tk.Button(text="STONE", font=("Times New Roman", 20, "bold"), command=lambda: log_move("stone"),
                       width = 7, height = 3, bd = 3, bg="#505050")
paper_btn = tk.Button(text="PAPER", font=("Times New Roman", 20, "bold"), command=lambda: log_move("paper"),
                       width = 7, height = 3, bd = 3, bg="#FFFFFF")
scissors_btn = tk.Button(text="SCISSORS", font=("Times New Roman", 20, "bold"), command=lambda: log_move("scissors"),
                       width = 8, height = 3, bd = 3, bg="#0011FA")

c.create_window(75, 50, window=quit_btn)
c.create_window(1275, 50, window=reset_btn)
c.create_window(375, 650, window=stone_btn)
c.create_window(625, 650, window=paper_btn)
c.create_window(875, 650, window=scissors_btn)

root.mainloop()
