# 🧠 Stone Paper Scissors - Quarzion AI Edition V4.0

A modern Python implementation of the classic **Stone Paper Scissors** game featuring a custom-built AI opponent called **Quarzion AI**.

Unlike traditional versions that rely entirely on random choices, Quarzion AI analyzes player behavior and attempts to predict future moves using the **DecisionEngine v1.0**.

Built with **Python** and **Tkinter**.

---

## ✨ Features

### 🎮 Modern GUI

* Built using Tkinter
* Custom background support
* Custom game icon
* Dynamic result messages
* Real-time score tracking
* Reset button for quick restarts

### 🤖 Quarzion AI

* Records recent player moves
* Analyzes move frequency
* Predicts the player's most likely next move
* Selects a counter move
* Uses a weighted decision system to avoid becoming completely predictable

### 📊 Score System

* Player vs Quarzion AI scoreboard
* Win, Lose and Tie detection
* Ties award 0.5 points to both sides

---

## 🧠 How Quarzion AI Works

The current AI uses **DecisionEngine v1.0**:

1. Stores the player's recent move history.
2. Determines the most frequently played move.
3. Predicts the player's next move.
4. Chooses the counter move.
5. Occasionally plays a random move to remain less predictable.

This creates a more challenging experience than a standard random opponent.

---

## 📂 Project Structure

```text
stone-paper-scissors/
│
├── main.py
├── DecisionEngine.py
│
├── assets/
│   ├── bg.png
│   └── icon.ico
│
├── CHANGELOG.md
├── LICENSE
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/MysterSM/stone-paper-scissors.git
cd stone-paper-scissors
```

### Run the game

```bash
python main.py
```

---

## 🔮 Planned Features

* Advanced Quarzion AI behavior tracking
* Persistent player profiles
* Improved UI and animations
* Sound effects
* Additional game modes
* Difficulty settings
* Enhanced visual effects

---

## 📜 Changelog

See `CHANGELOG.md` for detailed version history.

---

## 👨‍💻 Author

**Sharodik Mondal**

GitHub: MysterSM