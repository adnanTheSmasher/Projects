# Speed Typing Test (Console-Based)

## 📖 Overview
This project is a **console-based Speed Typing Test** application built in Python using the `curses` library. It challenges users to type a randomly chosen line of text as quickly and accurately as possible, while calculating their **Words Per Minute (WPM)** in real time.  

The project is fully text-based and runs inside the terminal, making it lightweight, interactive, and ideal for practicing typing speed without requiring any external GUI libraries.  

This repository represents one of my learning milestones in Python programming, particularly focusing on working with the `curses` module, handling keyboard input, and designing simple but engaging terminal-based applications.  

---

## ✨ Features
- **Interactive Console UI**: Uses `curses` for real-time input and text display.  
- **Randomized Text Selection**: Loads typing text from an external file (`wpm_text.txt`).  
- **WPM Calculation**: Dynamically calculates and displays Words Per Minute while typing.  
- **Accuracy Feedback**: Highlights correct characters in green and incorrect characters in red.  
- **Restart & Exit Option**: Allows multiple test rounds, or exiting the program using the `ESC` key.  
- **Minimal & Lightweight**: Purely console-based, requiring no external dependencies apart from Python’s standard library.  

---

## 📂 Project Structure
speed_typing_test/
├── main.py # The main program containing all logic
├── wpm_text.txt # External file containing sample texts
└── README.md # Documentation (this file)


### `main.py`
The core Python script containing the logic for the Speed Typing Test.  

Functions inside:
- **`start_screen(stdscr)`**: Displays a welcome screen.  
- **`display_text(stdscr, target, current, wpm)`**: Shows target text, highlights typed characters, and displays live WPM.  
- **`load_text()`**: Loads a random line from `wpm_text.txt`.  
- **`wpm_test(stdscr)`**: Core typing logic (keyboard handling, WPM calculation, and completion check).  
- **`main(stdscr)`**: Initializes colors, manages game flow, and allows multiple rounds.  

### `wpm_text.txt`
A simple text file containing multiple lines of text. Each line is a typing challenge. The `load_text()` function picks one randomly each round.  

---

## ⚙️ How It Works
1. Program starts with a welcome screen.  
2. User presses a key to begin.  
3. A random line from `wpm_text.txt` is displayed.  
4. User types the text:  
   - Correct characters appear in **green**.  
   - Incorrect characters appear in **red**.  
   - WPM updates dynamically.  
5. **Backspace** removes characters.  
6. **ESC** exits the program.  
7. On completion, a congratulatory message appears, and the user can restart or exit.  

---

## 💡 Design Choices
- **Why `curses`?**  
  It allows real-time text display, colors, and non-blocking input, unlike `input()`.  
- **Why external text file?**  
  Easy customization without editing the code.  
- **WPM Formula:**  
  \[
  WPM = \frac{\text{characters typed}}{5} \div \frac{\text{time (seconds)}}{60}
  \]  
- **Edge Cases Handled:**  
  - Multiple backspace key codes (`KEY_BACKSPACE`, `\b`, `\x7f`).  
  - Prevents division by zero in early calculations.  
  - ESC key to exit safely.  

---

## 🚀 How to Run
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/Projects.git
   cd Projects/speed_typing_test
2. Ensure you have Python 3 installed.

3. Run the program: python main.py
4. Keep wpm_text.txt in the same folder as main.py.


🎯 Conclusion

This Speed Typing Test project is a fun, lightweight, and educational way to practice typing skills. While simple in concept, it demonstrates important programming principles like user input handling, real-time feedback, file management, and modular design.
It also reflects my growth as a programmer—starting from small console projects and building towards more complex systems. By keeping the design modular and customizable, this project can easily be extended with new features in the future.
