# Quick Start Guide

## First Time Setup

1. **Ensure Python is installed** (version 3.7 or higher):
   ```powershell
   python --version
   ```

2. **Install required dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```
   
   Or install pygame directly:
   ```powershell
   pip install pygame
   ```

## Running the Game

1. **Navigate to the game directory**:
   ```powershell
   cd Alien_Invasion
   ```

2. **Run the game**:
   ```powershell
   python Alien_Invasion.py
   ```

## Game Controls Quick Reference

- **Arrow Keys**: Move ship left/right
- **SPACEBAR**: Fire bullets
- **P Key**: Start/Restart game
- **ESC Key**: Quit game
- **Mouse**: Click "Play" button to start

## Troubleshooting

### "pygame not found" error
```powershell
pip install pygame
```

### Game window doesn't appear
- Check that you're in the correct directory (`Alien_Invasion`)
- Ensure pygame is installed correctly
- Try running: `python -m pygame.examples.aliens` to test pygame installation

### Game runs too fast/slow
- Modify `ship_speed`, `bullet_speed`, and `alien_speed` in `Settings.py`

### Missing ship image
- The game will work without the ship image file
- It will use a generated rectangle as placeholder
- To use a custom ship: add `Ship_converted.bmp` to the project root

## Performance Tips

- Close other applications to improve performance
- Lower the screen resolution in `Settings.py` if needed:
  ```python
  self.screen_width = 600
  self.screen_height = 450
  ```

## First Play Experience

1. Launch the game
2. You'll see a "Play" button in the center
3. Click it or press 'P' to start
4. Use arrow keys to move your ship
5. Press SPACEBAR to shoot aliens
6. Try to clear all aliens before they reach the bottom!

## Customization

Want to modify the game? Check out these files:
- `Settings.py` - Change speeds, colors, difficulty
- `Aliens.py` - Modify alien appearance
- `Ship.py` - Customize your ship
- `Bullet.py` - Change bullet properties

Have fun! 🚀
