import tkinter as tk
from tkinter import ttk, messagebox
import math
import random

from quiz_frame import QuizFrame
from utils import sleep


class WaveSimulator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.running = False
        self.t = 0.0

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

        ttk.Button(control_frame, text="Add Wave", command=self.add_wave_ui).grid(row=0, column=0, padx=4, pady=4)
        ttk.Checkbutton(control_frame, text="Show grid/axes",
                        variable=self.show_grid, command=self.draw_static_elements).grid(row=0, column=1, padx=4)

        ttk.Label(control_frame, text="Speed:").grid(row=1, column=2)
        ttk.Scale(control_frame, from_=0.2, to=4.0, variable=self.speed,
                  orient="horizontal").grid(row=1, column=3, sticky="ew", padx=(4, 10))
        ttk.Label(control_frame, textvariable=self.speed).grid(row=1, column=4)

        control_frame.columnconfigure(3, weight=1)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(side="top", fill="x", padx=8, pady=(0, 8))
        self.start_btn = ttk.Button(btn_frame, text="Start", command=self.toggle_run)
        self.start_btn.pack(side="left")
        ttk.Button(btn_frame, text="Clear Waves", command=self.clear_waves).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Reset Time", command=self.reset_time).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Show/Hide Quiz", command=self.toggle_quiz).pack(side="right")

        self.canvas = tk.Canvas(self, bg="black", height=280)
        self.canvas.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        info_frame = ttk.Frame(self)
        info_frame.pack(side="top", fill="x", padx=8, pady=(0, 8))
        self.info_var = tk.StringVar(value="Press Start to animate waves.")
        ttk.Label(info_frame, textvariable=self.info_var).pack(side="left")

        self.quiz_frame = QuizFrame(self)
        self.quiz_frame.pack(fill="x", padx=8, pady=8)
        self.quiz_frame.pack_forget()

    def add_wave_ui(self):
        win = tk.Toplevel(self)
        win.title("Add Wave")

        ttk.Label(win, text="Frequency:").grid(row=0, column=0)
        freq_var = tk.DoubleVar(value=2.0)
        ttk.Scale(win, from_=0.5, to=20, variable=freq_var,
                  orient="horizontal").grid(row=0, column=1)
        ttk.Label(win, textvariable=freq_var).grid(row=0, column=2)

        ttk.Label(win, text="Amplitude:").grid(row=1, column=0)
        amp_var = tk.DoubleVar(value=60.0)
        ttk.Scale(win, from_=10, to=120, variable=amp_var,
                  orient="horizontal").grid(row=1, column=1)
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
            self.draw_all_waves()
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
            self.canvas.create_line(0, mid_y, w, mid_y, fill="#3CCA45", width=1)
            for x in range(0, w, 50):
                self.canvas.create_line(x, mid_y - 6, x, mid_y + 6, fill="#434040")
                self.canvas.create_line(x, 0, x, h, fill="#434040")
            for y in range(0, h, 50):
                self.canvas.create_line(0, y, w, y, fill="#434040")
        else:
            self.canvas.create_line(0, mid_y, w, mid_y, fill="#3CCA45", width=1)

        for idx, wave in enumerate(self.waves):
            self.canvas.create_text(
                60, 12 + idx*14, anchor="nw",
                text=f"Wave {idx+1}: {wave['wave_type'].get().capitalize()}  |  Freq: {wave['freq'].get():.2f} Hz  |  Amp: {wave['amp'].get():.0f}px",
                fill=wave['color'], font=("Segoe UI", 9, "bold")
            )

    def generate_wave_y(self, x, t, wave):
        w = self.canvas.winfo_width() or self.canvas.winfo_reqwidth()
        freq = wave["freq"].get()
        amp = wave["amp"].get()
        cycles_on_screen = 3
        k = 2 * math.pi * cycles_on_screen / max(1, w)

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

        dt = 0.1 * self.speed.get()
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
            points = [(x, self.generate_wave_y(x, self.t, wave))
                      for x in range(0, w + 1, step)]
            flat = [coord for point in points for coord in point]
            self.canvas.create_line(*flat, fill=wave["color"],
                                    width=2, tags="wave", smooth=True)
