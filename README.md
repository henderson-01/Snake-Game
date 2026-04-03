# Classic Snake Game 🐍

## 📖 Description

A retro-style Snake game built with Python and Pygame. This project recreates the classic experience with a Nokia-inspired color palette.
Control the snake, eat the food to grow longer, and avoid hitting the walls or your own tail! As you eat, and your score increases.

*I made this game as part of my Python coding learning journey.*

## ✅ Features

- **Classic Gameplay:** Navigate a grid to eat food.
- **Retro Aesthetics:** "Nokia Green" background and dark elements.
- **Score Tracking:** Real-time score display.
- **Game Over Screen:** Options to restart (`C`) or quit (`Q`).
- **Input Handling:** Logic to prevent the snake from reversing into itself immediately.

## 💻 Prerequisites

This guide is tailored for **Ubuntu Desktop** users.

### 1. Install System Dependencies

Ensure your system has Python and the virtual environment creator installed:

```bash
sudo apt update && sudo apt install python3-venv -y
```

## 👇 Installation

### 2. Set Up a Virtual Environment

It is best practice to isolate project dependencies.

- **Open your terminal** in the folder containing `snake_game.py`.
- **Create the environment:**

    ```bash
    python3 -m venv venv
    ```

- **Activate it:**

    ```bash
    source venv/bin/activate
    ```

- **Install Pygame:**
    Once active (you will see `(venv)` in your terminal), install the required library:

    ```bash
    pip install pygame
    ```

## ▶️ How to Play

- Navigate to the folder containing the game in your terminal.
- Run the game:

    ```bash
    python snake_game.py
    ```

- **Controls:**
  - **Arrow Keys:** Move Up, Down, Left, Right.
  - **Q:** Quit the game (when on the Game Over screen).
  - **C:** Play Again (when on the Game Over screen).

## 💡 Code Highlights (For Learners)

If you are looking at the code, here are the key concepts used:

- **Grid System:** The game uses a block size (`SNAKE_BLOCK = 15`). All positions (snake segments and food) are calculated to snap to this grid using math logic.
- **Game Loop:** The `while not game_over:` loop is the heart of the game, updating the screen and checking logic every frame.
- **List Management:** The snake is represented as a list of coordinates (`snake_List`), growing as food is eaten and removing the tail as it moves.

---

## ⚠️ Disclaimer

This project is provided "as-is" without any warranty of any kind. I am not responsible for any issues, data loss, or problems caused (code-related or otherwise) that may occur from using this Information. **Use it at your own risk.**
