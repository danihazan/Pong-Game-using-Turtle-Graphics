# Pong Game using Turtle Graphics
# Pong Game

A classic Pong Game implemented in Python using the `turtle` module. This two-player game lets players control paddles to bounce a ball back and forth while scoring points.
<img src="https://github.com/user-attachments/assets/a348a5c9-fd1c-4918-9618-f3f713bb06e1" alt="Pomodoro Timer" width="300">

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Game Controls](#game-controls)
5. [How to Play](#how-to-play)
6. [Files in the Project](#files-in-the-project)

---

## Overview

Pong Game is a recreation of the timeless arcade game where two players control paddles to keep a bouncing ball in play. The first player to miss the ball gives a point to their opponent. The game offers smooth paddle control, increasing ball speed, and a scoreboard.

---

## Features

- **Two-Player Gameplay**: Players control paddles on the left and right sides of the screen.
- **Dynamic Ball Speed**: The ball increases speed with every successful paddle bounce.
- **Scorekeeping**: A real-time scoreboard updates as points are scored.
- **Collision Detection**: Ball bounces off paddles and walls for continuous gameplay.

---

## Installation

### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the game using the following command:
   ```bash
   python main.py
---
## Game Controls

- **Right Paddle**:
  - **Up Arrow (`↑`)**: Move the paddle upwards.
  - **Down Arrow (`↓`)**: Move the paddle downwards.

- **Left Paddle**:
  - **`W`**: Move the paddle upwards.
  - **`S`**: Move the paddle downwards.

## How to Play

1. **Start the Game**: Run the game script using Python:
   python main.py

2. **Control the Paddles**:
   - Player 1 (left paddle) uses the `W` (up) and `S` (down) keys.
   - Player 2 (right paddle) uses the `Up` and `Down` arrow keys.

3. **Objective**:
   - Hit the ball with your paddle to keep it in play.
   - If your opponent misses the ball, you score a point.

4. **Game Over**:
   - The game continues indefinitely, and the scoreboard updates dynamically.
   - Compete to see who can score the most points!

--- 
## Files in the Project

1. **`main.py`**:
   - The main script that initializes the game window, paddles, ball, and scoreboard.
   - Contains the main game loop for ball movement, paddle control, and collision detection.

2. **`paddle.py`**:
   - Implements the `Paddle` class.
   - Handles the movement of the paddles (up and down) and sets their initial positions.

3. **`ball.py`**:
   - Implements the `Ball` class.
   - Manages the ball's movement, collision detection with walls and paddles, and speed adjustments.

4. **`scoreboard.py`**:
   - Implements the `Scoreboard` class.
   - Displays and updates the scores for both players.






