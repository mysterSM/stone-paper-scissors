#DecisionEngine v1.0
from random import *
history = [] #keeps in track of history of moves played by user
options = ["stone","paper","scissors"]

def record_move(user_choice): #records user's choices from main game
    history.append(user_choice)
    if(len(history) > 5):
        history.pop(0)

def predict_player_move(): #calculates the most common move and prepares a counter-move
   
    move_counts = {'stone': 0, 'paper': 0, 'scissors': 0}

    for move in history:
        move_counts[move] += 1

    highest = max(move_counts.values())
    common_move = []
    for move in move_counts:
        if move_counts[move] == highest:
            common_move.append(move)
    for move in reversed(history):
        if move in common_move:
            return move
def counter_move(move):
    predicted_move = ""
    if(move=="stone"):
        predicted_move = "paper"
        return predicted_move
    
    elif(move=="scissors"):
        predicted_move = "stone"
        return predicted_move
    
    elif (move=="paper"):
        predicted_move = "scissors"
        return predicted_move 
    
def randomizer(predicted_move): #creates a 70/30 chance of either playing counter attack or random
    if(random()>0.7): 
        return choice(options)
    else:
        return predicted_move
def boot(): #acts an entry point for the main script to obtain moves
    a = predict_player_move()
    b = counter_move(a)
    c = randomizer(b)
    return c