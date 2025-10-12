# :video_game: Tic-Tac-Toe (Python Essentials 1)

A simple **Tic-Tac-Toe** game written in Python as part of the *Python Essentials 1* course.  
The program lets you play against the computer in a text-based console version of the game.

---

## :toolbox: Tech stack
| Tool / Library | Purpose |
|----------------|----------|
| **Python 3.x** | Core programming language |
| **venv** | Virtual environment for dependency isolation |
| **pydoc** | Built-in documentation generator |

## :jigsaw: Game Rules & Assumptions

These are based on the *Python Essentials 1* course requirements:

- :joystick: The **program** plays as **`X`**  
- :bust_in_silhouette: The **user** plays as **`O`**
- :zap: The **program always starts first** — placing its `X` in the **center** of the board
- :1234: **Board numbering:** Squares are numbered **row by row**, starting from `1` → `9`
- :speech_balloon: **User input:**  
  - The user chooses a square by typing its number (`1–9`).  
  - The move must:
    - Be an integer
    - Be within range `1–9`
    - Point to an **unoccupied** field
- :brain: **Game logic:**  
  - The program checks after each move if the game is over
  - Determines one of four outcomes:
    1. The game continues  
    2. **Draw** (no more available moves)  
    3. **You win** :trophy:  
    4. **Computer wins** :computer:

---

## :package: Setup

```bash

# Clone the repository
git clone https://github.com/Pulsarnixx/tic-tac-toe.git
cd tic-tac-toe

# Run the game
python tic_tac_toe.py

```

---

## :arrow_forward: Example Run

```bash
$ python tic_tac_toe.py

Welcome to Tic-Tac-Toe!
You play as O. Computer plays as X.
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move (1-9):

...

+-------+-------+-------+
|       |       |       |
|   O   |   O   |   O   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   X   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   X   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Winner: Player
```

---