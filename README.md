### Space Shooter Game

This repository contains a space shooter game built using Pygame. Players control a spaceship and shoot at incoming meteors while managing their shield and lives. The game features sprite-based animations, sound effects, and background music.

#### Features

- **Player Control**: Move the spaceship left and right using arrow keys and shoot with the space bar.
- **Dynamic Gameplay**: Encounter and shoot down various meteor sprites with randomized speed and rotation.
- **Scoring and Lives**: Track player score and lives. The game ends when the player loses all lives.
- **Animations and Sounds**: Includes explosion animations and sound effects for shooting and collisions.
- **Background Music**: Plays background music continuously throughout the game.

#### Game Mechanics

- **Player**: Controlled by arrow keys and space bar. Can shoot bullets and hide temporarily when hit.
- **Meteors**: Spawn randomly and move down the screen. They rotate and vary in speed.
- **Bullets**: Fired from the spaceship to destroy meteors.
- **Explosions**: Visual and sound effects for explosions when meteors are hit or the player’s ship is destroyed.

#### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**

   Install the required Python library:

   ```bash
   pip install pygame
   ```

3. **Add Game Assets**

   Ensure the following game assets are in the project directory:
   - `playerShip1_blue.png` (Player ship image)
   - `laserBlue01.png` (Bullet image)
   - `Explosion5.wav` (Explosion sound)
   - `Explosion13.wav` (Additional explosion sound)
   - `sfx_laser1.ogg` (Laser shoot sound)
   - `tgfcoder-FrozenJam-SeamlessLoop.ogg` (Background music)
   - Various meteor images (e.g., `meteorGrey_big1.png`)
   - `back.png` (Background image)

4. **Run the Game**

   Execute the game script:

   ```bash
   python game.py
   ```

#### Code Overview

- **Initialization**: Sets up Pygame, screen dimensions, and game variables.
- **Sprites**: Defines classes for `Player`, `mob` (meteor), `Bullet`, and `Explotion` with respective update and draw methods.
- **Gameplay Loop**: Main game loop handles events, updates sprites, and manages game state (score, lives, etc.).
- **Sound and Music**: Utilizes Pygame's mixer to handle sound effects and background music.

#### Contributing

Feel free to contribute by submitting issues or pull requests. Improvements or new features are always welcome!

---
