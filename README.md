# Nokia Snake Game

## Overview
A Python implementation of the classic Nokia Snake game using the Turtle module. The snake grows as it consumes food, with the score increasing accordingly. The game ends if the snake collides with the walls or itself, offering a nostalgic gaming experience.

## Project Outline
- The game begins with a small snake and randomly placed food.
- As the snake consumes food:
  - It grows in length.
  - The score increases.
- Game ends upon:
  - Collision with any of the four screen walls.
  - Collision with its own body.

## Detailed Clarifications
1. **Game Logic:**
   - The snake moves continuously in the direction set by arrow keys.
   - Food appears at random positions on the screen.
   - Each food item eaten adds points to the score.

2. **End Conditions:**
   - Wall collision: The game checks if the snake's head crosses screen boundaries.
   - Self-collision: Checks if the snake's head touches its body.

3. **Technical Features:**
   - Utilizes the `turtle` module for graphics.
   - Dynamic movement control using keyboard events.
   - Real-time score display on the game screen.

## Links
- [GitHub Repository](#https://github.com/NC-Aravindh/Snake-game/tree/main)

## My Process
1. Analyzed game mechanics and defined the core logic.
2. Developed snake movement and collision detection.
3. Incorporated score tracking and food generation.
4. Tested gameplay for bugs and improved user experience.

## Built With
- **Python**: Core programming language.
- **Turtle Module**: For rendering the game graphics and handling UI components.

## Author
[Your Name](Aravindh NC)

