# PHYSICS

WaveLab — A Simulation-Based Learning Tool for Sound Waves

WaveLab is an interactive, visualization-driven learning tool built using Python (Tkinter).
It allows students and educators to explore sound waves, adjust wave parameters, observe live animations, and test their understanding through a built-in quiz system.

The program features a cyberpunk-inspired UI, dynamic wave animations, and a responsive layout that adjusts to window size.

🚀 Features
🎛️ Wave Simulation

Add multiple waves with customizable:

Frequency

Amplitude

Wave Type: Sine, Square, Sawtooth

*Color

Real-time animated wave plotting at ~60 FPS

Adjustable animation speed

Grid and axes toggle

Smooth, continuous motion using a time-based algorithm

🧠 Interactive Quiz Module

Difficulty levels: Easy, Medium, Hard

Multiple-choice questions with instant feedback

Score tracking

End-of-quiz summary

Integrated directly into the simulation interface

🎨 Cyberpunk UI

Neon glowing animated titles

Modern layout and centered interface

Responsive resizing

Start screen and main simulation window

📁 Project Structure
PHYSICS/
│── main.py
│── wave_sim.py
│── quiz_frame.py
│── utils.py
│── README.md  ← (this file)

🧩 How It Works (Algorithm Overview)

WaveLab follows a structured algorithm:

1. Initialization

Creates main Tkinter window

Centers window on screen

Loads cyberpunk welcome screen

Switches to main simulation frame after clicking Start Simulation

Initializes the WaveSimulator (canvas, controls, quiz frame)

2. Wave Management

Maintains a list of waves (dictionary of frequency, amplitude, type, color)

Allows adding waves via a popup UI

Supports clearing waves and resetting time

3. Animation Algorithm

Uses a timer loop running every 16 ms

Simulation time t increases based on user-controlled speed

For each wave:

Calculates vertical position using:

Sine

Square

Sawtooth formulas

Draws the wave across the canvas

Supports multiple waves drawn simultaneously

4. Drawing Module

Grid lines, axes, and wave labels on the canvas

Automatically recalculates layout when window resizes

Neon glow animations for UI titles

5. Quiz Engine

Select difficulty

Randomize questions

Display choices

Show correctness feedback

Track and display score

6. Event Handling

Window resizing

Button interactions

Neon title glow cycles

Quiz toggle

Wave addition/removal

🛠️ Installation
1. Clone the Repository
git clone https://github.com/JamesCarl05/PHYSICS.git
cd PHYSICS

2. Requirements

WaveLab uses only built-in Python modules:

tkinter

math

random

No external dependencies required.

3. Run the Program
python main.py

📘 Usage Instructions
Start Page

Launch the program

Click START SIMULATION

Main Simulation

Press Start to animate waves

Add waves with custom settings

Toggle grid/axes

Adjust animation speed

Reset time

Clear waves

Quiz

Click Start/End Quiz

Select difficulty level

Answer questions and view explanations

🧪 Educational Purpose

WaveLab is ideal for:

Physics students learning about waves

Teachers demonstrating sound wave behavior

Interactive laboratory simulations

Science fair or school projects

💡 Future Improvements

Fourier synthesis module

Saving/loading wave configurations

Exporting wave graphs

Additional wave types
