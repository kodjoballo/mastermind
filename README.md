# 🎯 Mastermind (Mini Game)

## 📌 Description
The **Mastermind Game** is a logic-based guessing game where the computer randomly generates a **4-color code**, and the player has to guess it within **10 tries**.  

Each guess is evaluated:
- ✅ **Correct Position** → Right color in the right place  
- 🎨 **Incorrect Position** → Right color but in the wrong place  

The game continues until the player cracks the code or runs out of tries.  

---

## 🚀 How to Run
```js
python.exe mastermind.py

```
Or as usual from a python interpreter



### 🎮 Rules

Colors are represented by single letters:
```js

R (Red), G (Green), B (Blue), Y (Yellow), W (White), O (Orange)
```


The computer generates a secret code of 4 colors.

You must guess the code by typing colors separated by spaces, e.g.:
```js

Guess: R G B Y
```


After each guess, you will see feedback:

```js

Correct Position: 2 | Incorrect Position: 1
```

### 📚 Concepts Used

Random module (random.choice)

Loops & input validation

Dictionaries for counting colors

Game loop with win/lose conditions

### 🖼️ Example Gameplay

```js

Welcome to mastermind, you have 10 tries to guess the code...
The valid colors are R G B Y W O
Guess: R G B Y
Correct Position: 1 | Incorrect Position: 2
Guess: R R G G
Correct Position: 2 | Incorrect Position: 0
Guess: B O Y W
You guessed the code in 3 tries!

```

<p align="center">

![image alt](https://github.com/kodjoballo/mastermind/blob/main/Mastermind.png?raw=true)

</p>


###💡 Ideas to Extend

Add difficulty levels (different code lengths)

Allow duplicate colors or not (user chooses)

Show history of previous guesses and feedback

Build a GUI version with Tkinter


### source code ☺️👇
[source code](https://github.com/kodjoballo/mastermind/blob/main/mastermind.py)
