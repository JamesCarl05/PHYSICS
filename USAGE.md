# How to Use WaveLab

## Running the Application

### Basic Launch
```bash
python main.py
```

This will:
1. Open a centered window (900x650)
2. Display the animated "WAVELAB" neon banner
3. Initialize the wave simulator
4. Start the interactive simulation

## Interface Overview

### Title Banner
- **Animated Neon Text**: "WAVELAB" cycles through magenta → cyan → violet
- **Auto-resizing**: Banner adapts to window size
- **Glow Effect**: Updates every 320ms for cyberpunk aesthetic

### Simulation Canvas
- Main area for wave visualization
- Updates in real-time as window resizes
- Displays all active wave propagations

## Customizing the Application

### Change Window Size
Edit `main.py` (lines 13-14):
```python
window_width = 900   # Change to desired width
window_height = 650  # Change to desired height
```

### Change Neon Colors
Edit `main.py` (lines 31-33):
```python
neon1 = "#ff00ff"  # Magenta
neon2 = "#00e5ff"  # Cyan
neon3 = "#8f00ff"  # Violet
```

### Adjust Glow Speed
Edit `main.py` (line 60):
```python
root.after(320, glow)  # Change 320 to milliseconds desired
```

## Keyboard & Mouse Controls
Check `wave_sim.py` for interactive controls documentation.

---
*For code examples, see [EXAMPLES/](./EXAMPLES/)*
