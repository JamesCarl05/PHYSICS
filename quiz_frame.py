import tkinter as tk
from tkinter import ttk, messagebox
import random

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
                {"text": "Which wave type has abrupt jumps?",
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
                 "choices": [("Slows down", "A", "Higher speed speeds up animation."),
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
