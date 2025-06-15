from tkinter import *
from random import choice
from tkinter import messagebox
import pygame

pygame.mixer.init()

root = Tk()
root.title("Color Game")

welcome_gameover_label = Label(root, text="Welcome to the Color Game!", font=("Trebuchet MS", 40))
welcome_gameover_label.pack(pady=100)

score = 0
timeLeft = 60
game_started = False

root.geometry("1000x90")
root.iconbitmap("C:/Users/91868/Downloads/rainbow-image.ico")

# Load the sound files
try:
    correct_sound = pygame.mixer.Sound("C:/Users/91868/Downloads/the-correct-answer-33-183620.mp3")
except pygame.error as e:
    messagebox.showerror("Sound Error", f"Could not load correct sound: {e}. Please ensure file path is correct.")
    correct_sound = None

try:
    
    wrong_sound = pygame.mixer.Sound("C:/Users/91868/Downloads/buzzer-or-wrong-answer-20582.mp3")
except pygame.error as e:
    messagebox.showerror("Sound Error", f"Could not load wrong sound: {e}. Please ensure file path is correct.")
    wrong_sound = None

#main game code:
def startGame(event=None):
    global timeLeft, score, game_started

    if not game_started:
        game_started = True
        timeLeft = 60
        score = 0
        
        welcome_gameover_label.pack_forget()
        scoreLabel.pack_forget()
        timeLabel.pack_forget()
        
        scoreLabel.config(text="Score: 0")
        scoreLabel.pack(pady=5)
        timeLabel.config(text="Time Left: " + str(timeLeft))
        timeLabel.pack(pady=5)
        Frame.pack(pady=20)

        countdown()
        shuffler()
        Answer.focus_set()
    else:
        answer()

def countdown():
    global timeLeft, score, game_started

    if timeLeft > 0:
        timeLeft -= 1
        timeLabel.config(text="Time Left: " + str(timeLeft))
        root.after(1000, countdown)
    elif timeLeft == 0 and game_started:
        messagebox.showinfo("Time Over", "Your Score: " + str(score))
        game_started = False
        
        Answer.config(state=DISABLED)
        ansButton.config(state=DISABLED)
        
        Frame.pack_forget()
        welcome_gameover_label.config(text="Game Over!")
        welcome_gameover_label.pack(pady=100)
        
        scoreLabel.config(text="Game Over! Final Score: " + str(score))

def shuffler():
    global wordColor
    if timeLeft > 0:
        Answer.delete(0, END)
        ansLabel.after(400, lambda: ansLabel.config(text=""))
        
        colors = ['red', 'yellow', 'brown', 'blue', 'orange', 'purple', 'pink', 'black', 'green', 'magenta', 'navy']
        word = choice(colors)
        wordColor = choice(colors)
        
        colorLabel.config(text=word, fg=str(wordColor))
        Answer.focus_set()
    else:
        colorLabel.config(text="")

def answer():
    global timeLeft, score, game_started

    if timeLeft > 0 and game_started:
        entered_answer = Answer.get().lower()
        if wordColor.lower() == entered_answer:
            score += 1
            ansLabel.config(text="You're correct!", font=("Trebuchet MS", 15))
            if correct_sound:
                correct_sound.play()
        else:
            ansLabel.config(text="Incorrect", font=("Trebuchet MS", 15))
            
            if wrong_sound:
                wrong_sound.play()
        
        scoreLabel.config(text="Score: " + str(score))
        shuffler()
    elif not game_started:
        ansLabel.config(text="Press Enter to Start!", font=("Trebuchet MS", 15))
    else:
        ansLabel.config(text="Time is up!", font=("Trebuchet MS", 15))

scoreLabel = Label(root, text="Enter to START!", font=("Trebuchet MS", 24))
scoreLabel.pack(pady=5)

timeLabel = Label(root, text="Time Left: " + str(timeLeft), font=("Trebuchet MS", 12))
timeLabel.pack(pady=5)

Frame = Frame(root)

Label(Frame, text="Type the color of the text shown!", font=("Trebuchet MS", 20)).grid(row=0, column=0, columnspan=3, pady=20)

colorLabel = Label(Frame, text="", font=("Trebuchet MS", 30))
colorLabel.grid(row=1, column=0, columnspan=3, pady=20)

Answer = Entry(Frame, font=("Arial", 25))
Answer.grid(row=2, column=1, pady=20)

ansButton = Button(Frame, text="Check It", command=answer)
ansButton.grid(row=2, column=2, pady=20)

ansLabel = Label(Frame, text="", font=("Trebuchet MS", 20))
ansLabel.grid(row=3, column=0, columnspan=3, pady=20)

Answer.focus_set()
root.bind('<Return>', startGame)

root.mainloop()