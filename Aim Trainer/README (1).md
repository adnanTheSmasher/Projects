
# Aim Trainer - README

## Introduction

This project is a Python implementation of an **Aim Trainer Game** built using the `pygame` library.  
The game is inspired by popular aim training tools used by gamers to improve reflexes, accuracy, and reaction time.  

The player’s goal is to click on targets that appear randomly on the screen before they disappear.  
Performance is measured in terms of **speed**, **accuracy**, and **hits**. Once the player runs out of lives, 
a final results screen displays the overall stats.  

This project demonstrates real-time event-driven programming, collision detection, user input handling, 
and rendering graphics using Pygame.  

---

## Features

- Randomly generated targets that grow and shrink dynamically.  
- Lives system: Player starts with 5 lives, losing one each time a target disappears.  
- Performance tracking:  
  - **Time played**  
  - **Hits**  
  - **Clicks**  
  - **Speed (targets/second)**  
  - **Accuracy (%)**  
- End screen summarizing the player’s performance.  
- Minimal and clean design to focus on gameplay.  

---

## Project File

### `Aim_Trainer.py`

This file contains the full implementation of the Aim Trainer game.  

**Key Components**:  

1. **Global Variables and Setup**  
   - `WIDTH`, `HEIGHT`: Screen dimensions.  
   - `LIVES`: Number of allowed misses.  
   - `TARGET_INCREMENT`: Frequency of target spawn.  
   - Colors, fonts, and Pygame initialization are handled here.  

2. **Class `Target`**  
   Represents the clickable targets.  
   - Properties: Position `(x, y)`, size, growth state.  
   - Methods:  
     - `update()`: Controls target growth and shrink behavior.  
     - `draw(win)`: Draws concentric circles to form the target.  
     - `collide(x, y)`: Detects whether a mouse click hits the target.  

3. **Helper Functions**  
   - `draw(win, targets)`: Renders all targets on the screen.  
   - `format_time(secs)`: Converts elapsed time into `MM:SS.ms` format.  
   - `draw_top_bar(win, elapsed_time, targets_pressed, misses)`: Displays stats at the top of the screen.  
   - `end_screen(win, elapsed_time, target_pressed, clicks)`: Shows results and waits for the player to quit.  
   - `get_middle(surface)`: Centers text on the screen.  

4. **Main Loop (`main()`)**  
   - Controls the game’s event loop.  
   - Handles spawning targets at intervals.  
   - Processes user clicks and checks collisions.  
   - Tracks hits, misses, total clicks, and elapsed time.  
   - Ends the game when lives reach zero and displays performance results.  

---

## Gameplay Instructions

1. Run the game:  
   ```bash
   python Aim_Trainer.py
   ```

2. Click on the red-and-white targets before they shrink and disappear.  

3. Each missed target costs one life. The game ends after 5 misses.  

4. Stats are shown at the top bar:  
   - **Time**: Elapsed time since the start.  
   - **Speed**: Targets hit per second.  
   - **Hits**: Number of successful hits.  
   - **Lives**: Remaining attempts.  

5. Once the game ends, a results screen appears with your final **time**, **speed**, **hits**, and **accuracy**.  

---

## Example Gameplay

- Targets spawn randomly across the screen.  
- The player clicks them before they shrink.  
- A top status bar updates in real time.  
- At the end, performance stats are displayed like this:  

```
Time: 01:23.4
Speed: 2.5 t/s
Hits: 45
Accuracy: 87.3%
```

---

## Design Choices

- **Dynamic Target Behavior**: Targets grow and shrink to introduce variety and difficulty.  
- **Lives System**: Limited chances increase challenge and provide a clear win/loss condition.  
- **Simple UI**: Focuses on essential feedback without distractions.  
- **Performance Metrics**: Encourages self-improvement by tracking accuracy and speed.  

---

## Possible Improvements

- Add difficulty levels (increase spawn frequency or decrease target size).  
- Add sound effects for hits and misses.  
- Track high scores or maintain a leaderboard.  
- Introduce different target types with unique effects.  
- Add timed challenge mode where performance is measured in a fixed time.  

---

## Requirements

This project requires **Python 3.x** and the **Pygame** library.  

To install dependencies:  

```bash
pip install -r requirements.txt
```

---

## Conclusion

The Aim Trainer project demonstrates how to build a simple yet effective reflex-training game in Python.  
It combines graphical rendering, event-driven programming, and real-time performance tracking into a single interactive application.  

This project can be extended with additional features like difficulty settings, scoring systems, and advanced visual effects.  
It provides a strong foundation for understanding how modern 2D games are structured.  

---

**Author**: Adnan Hatim  
**Language**: Python 3  
**Library**: Pygame  
