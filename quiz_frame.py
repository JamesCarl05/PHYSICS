import tkinter as tk
from tkinter import ttk, messagebox
import random

class QuizFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.levels = ["Easy", "Average", "Hard"]  # Changed "Medium" to "Average"
        self.questions_by_level = self.build_questions()
        self.level_var = tk.StringVar(value=self.levels[0])
        self.current_q = None
        self.q_index = 0
        self.score = 0
        self.total = 0
        self.create_widgets()

    def build_questions(self):
        return {
            "Easy": [
                {"text": "Which variable controls the height of the wave?",
                 "choices": [("Frequency", "A", "Frequency changes how fast the wave oscillates."),
                             ("Amplitude", "B", "Amplitude controls the height of the wave."),
                             ("Phase", "C", "Phase shifts the wave position."),
                             ("Wavelength", "D", "Wavelength is related to frequency and speed.")],
                 "correct": "B"},
                {"text": "Which wave type is smooth and periodic?",
                 "choices": [("Sine", "A", "Sine wave is smooth and periodic."),
                             ("Square", "B", "Square wave has abrupt changes."),
                             ("Saw", "C", "Saw wave ramps linearly."),
                             ("Triangle", "D", "Triangle wave is piecewise linear.")],
                 "correct": "A"},
                {"text": "What does frequency measure?",
                 "choices": [("Wave height", "A", "Height is amplitude."),
                             ("Oscillations per second", "B", "Frequency is in Hz, measuring cycles per second."),
                             ("Wave speed", "C", "Speed is separate from frequency."),
                             ("Wave color", "D", "Color is for visualization.")],
                 "correct": "B"},
                {"text": "A higher amplitude means?",
                 "choices": [("Faster wave", "A", "Speed is not amplitude."),
                             ("Louder sound", "B", "Higher amplitude corresponds to louder volume."),
                             ("More cycles", "C", "Cycles are frequency."),
                             ("Shorter wavelength", "D", "Wavelength depends on frequency.")],
                 "correct": "B"},
                {"text": "What is a sound wave?",
                 "choices": [("Light wave", "A", "Light is electromagnetic."),
                             ("Mechanical wave", "B", "Sound requires a medium like air."),
                             ("Radio wave", "C", "Radio is electromagnetic."),
                             ("Static wave", "D", "Static is not a wave type.")],
                 "correct": "B"},
                {"text": "Which tool simulates waves?",
                 "choices": [("Calculator", "A", "Not for waves."),
                             ("WaveLab", "B", "WaveLab is designed for wave simulations."),
                             ("Paint app", "C", "Not for physics."),
                             ("Spreadsheet", "D", "Not interactive for waves.")],
                 "correct": "B"},
                {"text": "What unit is frequency in?",
                 "choices": [("Meters", "A", "Length unit."),
                             ("Hertz", "B", "Hz measures cycles per second."),
                             ("Seconds", "C", "Time unit."),
                             ("Volts", "D", "Electrical unit.")],
                 "correct": "B"},
                {"text": "Amplitude affects what?",
                 "choices": [("Speed", "A", "Speed is constant."),
                             ("Loudness", "B", "Higher amplitude means louder sound."),
                             ("Frequency", "C", "Frequency is separate."),
                             ("Direction", "D", "Direction is not affected.")],
                 "correct": "B"},
                {"text": "A sine wave looks like?",
                 "choices": [("Square", "A", "Square is blocky."),
                             ("Smooth curve", "B", "Sine is a smooth sinusoidal curve."),
                             ("Ramp", "C", "Ramp is sawtooth."),
                             ("Flat line", "D", "Flat is no oscillation.")],
                 "correct": "B"},
                {"text": "What is interference?",
                 "choices": [("Wave addition", "A", "Waves combine in interference."),
                             ("Wave speed", "B", "Not directly."),
                             ("Wave color", "C", "Visualization only."),
                             ("Wave type", "D", "Type is sine/square/etc.")],
                 "correct": "A"}
            ],
            "Average": [
                {"text": "Increasing frequency does what?",
                 "choices": [("Increases height", "A", "Height is amplitude."),
                             ("Speeds oscillation", "B", "Higher frequency means faster cycles."),
                             ("Slows wave", "C", "Frequency doesn't slow speed."),
                             ("Changes color", "D", "Color is arbitrary.")],
                 "correct": "B"},
                {"text": "Which wave has abrupt jumps?",
                 "choices": [("Sine", "A", "Smooth."),
                             ("Square", "B", "Square jumps between levels."),
                             ("Saw", "C", "Ramp shape."),
                             ("Triangle", "D", "Smooth transitions.")],
                 "correct": "B"},
                {"text": "If amplitude doubles, height?",
                 "choices": [("Halves", "A", "Opposite."),
                             ("Doubles", "B", "Directly proportional."),
                             ("Stays same", "C", "No change."),
                             ("Quadruples", "D", "Not squared.")],
                 "correct": "B"},
                {"text": "Speed slider affects?",
                 "choices": [("Frequency", "A", "Separate."),
                             ("Animation speed", "B", "Controls how fast time advances."),
                             ("Amplitude", "C", "Not amplitude."),
                             ("Wave type", "D", "Type is fixed.")],
                 "correct": "B"},
                {"text": "What is wavelength?",
                 "choices": [("Wave height", "A", "Height is amplitude."),
                             ("Distance per cycle", "B", "Wavelength is the length of one cycle."),
                             ("Time per cycle", "C", "That's period."),
                             ("Wave speed", "D", "Speed is separate.")],
                 "correct": "B"},
                {"text": "Interference can create?",
                 "choices": [("Louder waves", "A", "Constructive interference."),
                             ("Quieter waves", "B", "Destructive interference."),
                             ("Faster waves", "C", "Not speed."),
                             ("Both A and B", "D", "Depending on phase.")],
                 "correct": "D"},
                {"text": "A 1000 Hz wave has?",
                 "choices": [("Low pitch", "A", "High frequency is high pitch."),
                             ("High pitch", "B", "1000 Hz is audible high pitch."),
                             ("No sound", "C", "It's audible."),
                             ("Slow oscillation", "D", "Fast oscillation.")],
                 "correct": "B"},
                {"text": "Wave speed depends on?",
                 "choices": [("Frequency", "A", "Speed is medium-dependent."),
                             ("Medium", "B", "Speed varies by material."),
                             ("Amplitude", "C", "Amplitude doesn't affect speed."),
                             ("Color", "D", "Visualization.")],
                 "correct": "B"},
                {"text": "What is resonance?",
                 "choices": [("Wave reflection", "A", "Not exactly."),
                             ("Amplified oscillation", "B", "Resonance amplifies at natural frequency."),
                             ("Wave absorption", "C", "Opposite."),
                             ("Wave splitting", "D", "Not splitting.")],
                 "correct": "B"},
                {"text": "Doubling frequency halves?",
                 "choices": [("Amplitude", "A", "No."),
                             ("Wavelength", "B", "Wavelength = speed / frequency."),
                             ("Speed", "C", "Speed constant."),
                             ("Period", "D", "Period = 1/frequency.")],
                 "correct": "B"}
            ],
            "Hard": [
                {"text": "For a traveling wave, phase is?",
                 "choices": [("2*pi*f*t", "A", "Missing spatial part."),
                             ("k*x - 2*pi*f*t", "B", "Standard form for right-moving wave."),
                             ("Amplitude only", "C", "Not just amplitude."),
                             ("Random", "D", "Deterministic.")],
                 "correct": "B"},
                {"text": "In WaveLab, high frequency shows?",
                 "choices": [("Slow waves", "A", "Opposite."),
                             ("Dense oscillations", "B", "Visual density for high freq."),
                             ("Flat line", "C", "No."),
                             ("Large amplitude", "D", "Separate.")],
                 "correct": "B"},
                {"text": "Sound speed in air is ~?",
                 "choices": [("300 m/s", "A", "Close, but 343 m/s."),
                             ("343 m/s", "B", "Standard value."),
                             ("1000 m/s", "C", "Too fast."),
                             ("10 m/s", "D", "Too slow.")],
                 "correct": "B"},
                {"text": "Interference patterns depend on?",
                 "choices": [("Amplitude", "A", "Also phase."),
                             ("Phase difference", "B", "Key for interference."),
                             ("Frequency", "C", "Also matters."),
                             ("All of the above", "D", "Multiple factors.")],
                 "correct": "D"},
                {"text": "A square wave's Fourier series has?",
                 "choices": [("Only even harmonics", "A", "Odd harmonics."),
                             ("Only odd harmonics", "B", "Square wave has odd harmonics."),
                             ("No harmonics", "C", "It does."),
                             ("Infinite harmonics", "D", "Yes, but odd.")],
                 "correct": "B"},
                {"text": "Wavelength formula is?",
                 "choices": [("f / v", "A", "No."),
                             ("v / f", "B", "Wavelength = speed / frequency."),
                             ("f * v", "C", "No."),
                             ("a / f", "D", "Amplitude not involved.")],
                 "correct": "B"},
                {"text": "Resonance occurs at?",
                 "choices": [("Any frequency", "A", "Specific."),
                             ("Natural frequency", "B", "Matches the system's frequency."),
                             ("Low amplitude", "C", "Opposite."),
                             ("High speed", "D", "Not necessarily.")],
                 "correct": "B"},
                {"text": "Doppler effect changes?",
                 "choices": [("Amplitude", "A", "Not primarily."),
                             ("Frequency", "B", "Frequency shifts with motion."),
                             ("Wavelength", "C", "Related to frequency."),
                             ("Both B and C", "D", "Frequency and wavelength.")],
                 "correct": "D"},
                {"text": "A wave's energy is proportional to?",
                 "choices": [("Frequency", "A", "Not directly."),
                             ("Amplitude squared", "B", "Energy ~ A^2."),
                             ("Speed", "C", "Not squared."),
                             ("Wavelength", "D", "Inverse.")],
                 "correct": "B"},
                {"text": "In standing waves, nodes are?",
                 "choices": [("High amplitude", "A", "Opposite."),
                             ("Zero displacement", "B", "Points of no motion."),
                             ("Antinodes", "C", "Antinodes are max."),
                             ("Moving points", "D", "Nodes are stationary.")],
                 "correct": "B"}
            ]
        }

    def create_widgets(self):
        self.config(height=180)
        top = ttk.Frame(self)
        top.pack(fill="x", pady=(0, 5))

        ttk.Label(top, text="Quiz Level:").pack(side="left")
        ttk.OptionMenu(top, self.level_var, self.level_var.get(),
                       *self.levels, command=self.change_level).pack(side="left", padx=6)
        ttk.Button(top, text="Start Level", command=self.start_level).pack(side="left", padx=10)
        self.score_label = ttk.Label(top, text="Score: 0/0")
        self.score_label.pack(side="left", padx=20)

        self.q_text = tk.Text(self, height=4, wrap="word",
                              font=("Segoe UI", 11),
                              state="disabled", relief="groove", bd=2)
        self.q_text.pack(fill="x", pady=(5, 5))

        self.choice_frame = ttk.Frame(self)
        self.choice_frame.pack(fill="x", pady=(0, 5))

        bottom = ttk.Frame(self)
        bottom.pack(fill="x")
        self.next_btn = ttk.Button(bottom, text="Next Question",
                                   command=self.next_question,
                                   state="disabled")
        self.next_btn.pack(pady=5)

    def change_level(self, *_):
        self.score = 0
        self.total = 0
        self.q_index = 0
        self.update_score_label()
        self.clear_question_area()
        self.next_btn.config(state="disabled")

    def start_level(self):
        level = self.level_var.get()
        self.questions = list(self.questions_by_level[level])
        random.shuffle(self.questions)
        self.score = 0
        self.total = len(self.questions)
        self.q_index = 0
        self.next_btn.config(state="disabled")
        self.ask_question()

    def clear_question_area(self):
        self.q_text.config(state="normal")
        self.q_text.delete("1.0", "end")
        self.q_text.config(state="disabled")
        for widget in self.choice_frame.winfo_children():
            widget.destroy()

    def ask_question(self):
        self.clear_question_area()
        if self.q_index >= len(self.questions):
            self.finish_quiz()
            return

        q = self.questions[self.q_index]
        self.current_q = q
        self.q_text.config(state="normal")
        self.q_text.insert("1.0", f"Q{self.q_index + 1}: {q['text']}")
        self.q_text.config(state="disabled")

        choices = list(q["choices"])
        random.shuffle(choices)

        for idx, choice in enumerate(choices):
            key = chr(65 + idx)
            btn = ttk.Button(self.choice_frame, text=f"{key}. {choice[0]}",
                             command=lambda c=choice: self.select_choice(c))
            btn.pack(fill="x", pady=3)

        self.next_btn.config(state="disabled")

    def select_choice(self, choice):
        for child in self.choice_frame.winfo_children():
            child.config(state="disabled")

        clicked = choice[1]
        correct = self.current_q["correct"]

        if clicked == correct:
            self.score += 1
            messagebox.showinfo("Correct", "Correct!\n\n" + choice[2])
        else:
            correct_text = next(c[0] for c in self.current_q["choices"] if c[1] == correct)
            correct_expl = next(c[2] for c in self.current_q["choices"] if c[1] == correct)
            messagebox.showinfo("Incorrect",
                                f"Incorrect.\n\nCorrect answer: {correct_text}\n\n{correct_expl}")

        self.q_index += 1
        self.update_score_label()
        self.next_btn.config(state="normal")

    def next_question(self):
        self.ask_question()
        self.next_btn.config(state="disabled")

    def finish_quiz(self):
        msg = f"You finished the level!\nScore: {self.score}/{self.total}"
        if self.score == self.total:
            msg += "\nExcellent — perfect score!"
        elif self.score >= self.total * 0.7:
            msg += "\nGreat job!"
        elif self.score >= self.total * 0.4:
            msg += "\nGood effort!"
        else:
            msg += "\nTry again!"

        messagebox.showinfo("Level Complete", msg)
        self.score = 0
        self.total = 0
        self.q_index = 0
        self.update_score_label()
        self.clear_question_area()
        self.next_btn.config(state="disabled")

    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.score}/{self.total}")