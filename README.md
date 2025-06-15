# Python Color Game

## Overview

A simple yet addictive color game built using Python's `tkinter` for the GUI and `pygame.mixer` for sound effects. The objective of the game is to type the *color* of the word displayed, not the word itself, as quickly and accurately as possible before the time runs out. It's a fun way to test your reflexes and color recognition!

## Features

* **Engaging Gameplay:** Simple rules, challenging execution.
* **Dynamic Colors:** Words appear in a random color, requiring quick thinking.
* **Score Tracking:** Keep track of your correct answers.
* **Countdown Timer:** A 60-second timer adds to the challenge.
* **Sound Feedback:** Auditory cues for correct and incorrect answers enhance the experience.
* **Tkinter GUI:** Intuitive and responsive graphical user interface.

## How to Play

1.  **Run the Game:** Execute the `color_game.py` (or whatever you named your main script, e.g., `main.py`) file.
2.  **Start:** Press the `Enter` key or click "Check It" to begin the game.
3.  **Type the Color:** A word will appear (e.g., "blue" in red color). You need to type `red` into the input box.
4.  **Submit:** Press `Enter` again or click "Check It" to submit your answer.
5.  **Score:** Your score will update based on correct answers.
6.  **Time Limit:** The game lasts for 60 seconds. When time runs out, your final score will be displayed.

## Installation

To run this game, you'll need Python installed on your system.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Nilanjana2003/Python-Color-Game.git](https://github.com/Nilanjana2003/Python-Color-Game.git)
    cd Python-Color-Game
    ```

2.  **Install Dependencies:**
    This game requires the `pygame` library.
    ```bash
    pip install pygame
    ```

3.  **Download Sound Files (if not included in repo):**
    Ensure you have the following MP3 files in the specified paths, or update the paths in the script to where you store them:
    * `the-correct-answer-33-183620.mp3` (for correct answers)
    * `buzzer-or-wrong-answer-20582.mp3` (for incorrect answers)   

## Usage

Run the main Python script:
```bash
python your_game_script_name.py
