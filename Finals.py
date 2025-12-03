import tkinter as tk
from tkinter import ttk, messagebox
import math
import random

# ------------------------------------------------------------
# WAVE SIMULATOR
# ------------------------------------------------------------
class WaveSimulator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.running = False
        self.t = 0.0

        # List of waves (each is a dict with its own parameters)
        self.waves = []
        self.add_wave(freq=2.0, amp=60.0, wave_type="sine", color="#e81ad7")

        self.speed = tk.DoubleVar(value=1.0)
        self.show_grid = tk.BooleanVar(value=True)

        self.create_widgets()
        self.draw_static_elements()

    def add_wave(self, freq=2.0, amp=60.0, wave_type="sine", color="#e81ad7"):
        wave = {
            "freq": tk.DoubleVar(value=freq),
            "amp": tk.DoubleVar(value=amp),
            "wave_type": tk.StringVar(value=wave_type),
            "color": color
        }
        self.waves.append(wave)
    
    def clear_waves(self):
        if messagebox.askyesno("Clear Waves", "Are you sure you want to remove all waves?"):
            self.waves.clear()
            self.t = 0.0
            self.draw_static_elements()
            self.canvas.delete("wave")
            self.info_var.set("All waves cleared.")

    def create_widgets(self):
        control_frame = ttk.Frame(self)
        control_frame.pack(side="top", fill="x", padx=8, pady=8)

        ttk.Button(control_frame, text="Add Wave", command=self.add_wave_ui).grid(row=0, column=0, padx=4, pady=4, sticky="w")
        ttk.Checkbutton(control_frame, text="Show grid/axes",
                        variable=self.show_grid, command=self.draw_static_elements).grid(row=0, column=1, sticky="w", padx=4)

        ttk.Label(control_frame, text="Speed:").grid(row=1, column=2, sticky="w")
        ttk.Scale(control_frame, from_=0.2, to=4.0, variable=self.speed, orient="horizontal").grid(row=1, column=3, sticky="ew", padx=(4, 10))
        ttk.Label(control_frame, textvariable=self.speed).grid(row=1, column=4, sticky="w")
        control_frame.columnconfigure(3, weight=1)

        # Buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(side="top", fill="x", padx=8, pady=(0, 8))
        self.start_btn = ttk.Button(btn_frame, text="Start", command=self.toggle_run)
        self.start_btn.pack(side="left")
        ttk.Button(btn_frame, text="Clear Waves", command=self.clear_waves).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Reset Time", command=self.reset_time).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Show/Hide Quiz", command=self.toggle_quiz).pack(side="right")

        # Canvas
        self.canvas = tk.Canvas(self, bg="black", height=280)
        self.canvas.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        # Info label
        info_frame = ttk.Frame(self)
        info_frame.pack(side="top", fill="x", padx=8, pady=(0, 8))
        self.info_var = tk.StringVar(value="Press Start to animate waves.")
        ttk.Label(info_frame, textvariable=self.info_var).pack(side="left", anchor="w")

        # Quiz panel
        self.quiz_frame = QuizFrame(self)
        self.quiz_frame.pack(fill="x", padx=8, pady=8)
        self.quiz_frame.pack_forget()

    def add_wave_ui(self):
        win = tk.Toplevel(self)
        win.title("Add Wave")

        ttk.Label(win, text="Frequency:").grid(row=0, column=0)
        freq_var = tk.DoubleVar(value=2.0)
        ttk.Scale(win, from_=0.5, to=20, variable=freq_var, orient="horizontal").grid(row=0, column=1)
        ttk.Label(win, textvariable=freq_var).grid(row=0, column=2)

        ttk.Label(win, text="Amplitude:").grid(row=1, column=0)
        amp_var = tk.DoubleVar(value=60.0)
        ttk.Scale(win, from_=10, to=120, variable=amp_var, orient="horizontal").grid(row=1, column=1)
        ttk.Label(win, textvariable=amp_var).grid(row=1, column=2)

        ttk.Label(win, text="Wave Type:").grid(row=2, column=0)
        wave_var = tk.StringVar(value="sine")
        ttk.OptionMenu(win, wave_var, "sine", "sine", "square", "saw").grid(row=2, column=1)

        ttk.Label(win, text="Color:").grid(row=3, column=0)
        color_var = tk.StringVar(value="#%06x" % random.randint(0, 0xFFFFFF))
        ttk.Entry(win, textvariable=color_var).grid(row=3, column=1)

        def add_and_close():
            self.add_wave(freq_var.get(), amp_var.get(), wave_var.get(), color_var.get())
            self.draw_static_elements()
            self.draw_all_waves()  # show new wave immediately
            win.destroy()

        ttk.Button(win, text="Add Wave", command=add_and_close).grid(row=4, column=0, columnspan=3, pady=8)

    def toggle_quiz(self):
        if self.quiz_frame.winfo_ismapped():
            self.quiz_frame.pack_forget()
        else:
            self.quiz_frame.pack(fill="x", padx=8, pady=8)

    def draw_static_elements(self):
        self.canvas.delete("all")
        w = self.canvas.winfo_width() or self.canvas.winfo_reqwidth()
        h = self.canvas.winfo_height() or 280
        mid_y = h // 2

        if self.show_grid.get():
            self.canvas.create_line(0, mid_y, w, mid_y, fill="#444", width=1)
            for x in range(0, w, 50):
                self.canvas.create_line(x, mid_y - 6, x, mid_y + 6, fill="#434040")
                self.canvas.create_line(x, 0, x, h, fill="#434040")
            for y in range(0, h, 50):
                self.canvas.create_line(0, y, w, y, fill="#434040")
        else:
            self.canvas.create_line(0, mid_y, w, mid_y, fill="#444", width=1)

        # Draw info for each wave
        for idx, wave in enumerate(self.waves):
            self.canvas.create_text(
                60, 12 + idx*14, anchor="nw",
                text=f"Wave {idx+1}: {wave['wave_type'].get().capitalize()}  |  Freq: {wave['freq'].get():.2f} Hz  |  Amp: {wave['amp'].get():.0f}px",
                fill=wave['color'], font=("Segoe UI", 9, "bold")
            )

    def generate_wave_y(self, x, t, wave):
        w = self.canvas.winfo_width() or self.canvas.winfo_reqwidth()
        freq = wave["freq"].get()  # how fast it oscillates vertically
        amp = wave["amp"].get()
        cycles_on_screen = 3
        k = 2 * math.pi * cycles_on_screen / max(1, w)  # spatial frequency

    # Phase determines horizontal movement over time
        phase = k * x - 2 * math.pi * freq * t

        wt = wave["wave_type"].get()
        if wt == "sine":
            val = math.sin(phase)
        elif wt == "square":
            val = 1.0 if math.sin(phase) >= 0 else -1.0
        elif wt == "saw":
            p = (phase / (2 * math.pi)) % 1.0
            val = 2 * (p - 0.5)
        else:
            val = math.sin(phase)
        
        return (self.canvas.winfo_height() // 2) - amp * val


    def animate(self):
        if not self.running:
            return

    # Make dt larger so movement is visible
        dt = 0.1 * self.speed.get()  # base time step multiplied by speed
        self.t += dt

        self.draw_all_waves()
        self.after(30, self.animate)

    def toggle_run(self):
        if not self.running:
            self.running = True
            self.start_btn.config(text="Stop")
            self.animate()
        else:
            self.running = False
            self.start_btn.config(text="Start")

    def reset_time(self):
        self.t = 0.0
        self.info_var.set("Time reset to zero.")
        self.draw_static_elements()
        self.draw_all_waves()

    def draw_all_waves(self):
        self.canvas.delete("wave")
        w = self.canvas.winfo_width() or self.canvas.winfo_reqwidth()
        step = max(2, w // 400)

        for wave in self.waves:
            points = []
            for x in range(0, w + 1, step):
                y = self.generate_wave_y(x, self.t, wave)
                points.append((x, y))
            flat = [coord for point in points for coord in point]
            self.canvas.create_line(*flat, fill=wave["color"], width=2, tags="wave", smooth=True)




# ------------------------------------------------------------
# QUIZ PANEL (Simulation-related)
# ------------------------------------------------------------
class QuizFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.levels = ["Easy", "Medium", "Hard"]
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
                             ("Amplitude", "B", "Amplitude controls the height of the wave.")],
                 "correct": "B"},
                {"text": "Which wave type is smooth and periodic?",
                 "choices": [("Sine", "A", "Sine wave is smooth and periodic."),
                             ("Square", "B", "Square wave is not smooth.")],
                 "correct": "A"}
            ],
            "Medium": [
                {"text": "Increasing the frequency will make the wave?",
                 "choices": [("Oscillate faster", "A", "Higher frequency means faster oscillation."),
                             ("Grow taller", "B", "Amplitude controls height, not frequency.")],
                 "correct": "A"},
                {"text": "Which wave type has abrupt jumps between max and min?",
                 "choices": [("Saw", "A", "Saw wave has ramp shape."),
                             ("Square", "B", "Square wave jumps abruptly.")],
                 "correct": "B"}
            ],
            "Hard": [
                {"text": "If amplitude is doubled, the wave height?",
                 "choices": [("Remains same", "A", "Amplitude defines height."),
                             ("Doubles", "B", "Doubling amplitude doubles wave height.")],
                 "correct": "B"},
                {"text": "If speed slider is increased, animation?",
                 "choices": [("Slows down", "A", "Higher speed value speeds up animation."),
                             ("Speeds up", "B", "Correct, higher speed accelerates animation.")],
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

        self.q_text = tk.Text(self, height=4, wrap="word", font=("Segoe UI", 11),
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


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    root = tk.Tk()
    root.title("Wave Simulator + Quiz")
    root.geometry("900x650")
    try:
        root.option_add("*Font", ("Segoe UI", 10))
    except:
        pass

    sim = WaveSimulator(root)

    def on_resize(event):
        sim.draw_static_elements()
        sim.draw_all_waves()

    root.bind("<Configure>", on_resize)
    root.mainloop()


if __name__ == "__main__":
    main()

