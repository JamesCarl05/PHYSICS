import tkinter as tk
from tkinter import ttk, messagebox
import math
import random
import time

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

        ttk.Label(control_frame, text="Speed (type any positive value):").grid(row=1, column=2)
        self.speed_entry = ttk.Entry(control_frame, textvariable=self.speed)
        self.speed_entry.grid(row=1, column=3, sticky="ew", padx=(4, 10))
        self.speed_entry.bind("<Return>", lambda e: self.validate_speed())

        control_frame.columnconfigure(3, weight=1)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(side="top", fill="x", padx=8, pady=(0, 8))
        self.start_btn = ttk.Button(btn_frame, text="Start", command=self.toggle_run)
        self.start_btn.pack(side="left")
        ttk.Button(btn_frame, text="Clear Waves", command=self.clear_waves).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Reset Time", command=self.reset_time).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Start/End Quiz", command=self.toggle_quiz).pack(side="right")

        self.canvas = tk.Canvas(self, bg="black", height=280)
        self.canvas.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        info_frame = ttk.Frame(self)
        info_frame.pack(side="top", fill="x", padx=8, pady=(0, 8))
        self.info_var = tk.StringVar(value="Press Start to animate waves.")
        ttk.Label(info_frame, textvariable=self.info_var).pack(side="left")

        self.quiz_frame = QuizFrame(self)
        self.quiz_frame.pack(fill="x", padx=8, pady=8)
        self.quiz_frame.pack_forget()

    def validate_speed(self):
        try:
            val = float(self.speed.get())
            if val <= 0:
                raise ValueError
            if val > 100:
                val = 100
                self.speed.set(val)
                messagebox.showinfo("Capped Speed", "Speed capped at 100 for stability.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Speed must be a positive number. Resetting to 1.0.")
            self.speed.set(1.0)

    def add_wave_ui(self):
        win = tk.Toplevel(self)
        win.title("Add Wave")

        ttk.Label(win, text="Frequency (Hz, any positive value):").grid(row=0, column=0)
        freq_var = tk.DoubleVar(value=2.0)
        freq_entry = ttk.Entry(win, textvariable=freq_var)
        freq_entry.grid(row=0, column=1)
        freq_entry.bind("<Return>", lambda e: self.validate_freq(freq_var))

        ttk.Label(win, text="Amplitude (pixels, any positive value):").grid(row=1, column=0)
        amp_var = tk.DoubleVar(value=60.0)
        amp_entry = ttk.Entry(win, textvariable=amp_var)
        amp_entry.grid(row=1, column=1)
        amp_entry.bind("<Return>", lambda e: self.validate_amp(amp_var))

        ttk.Label(win, text="Wave Type:").grid(row=2, column=0)
        wave_var = tk.StringVar(value="sine")
        ttk.OptionMenu(win, wave_var, "sine", "sine", "square", "saw").grid(row=2, column=1)

        ttk.Label(win, text="Color (hex, e.g., #ff0000):").grid(row=3, column=0)
        color_var = tk.StringVar(value="#%06x" % random.randint(0, 0xFFFFFF))
        ttk.Entry(win, textvariable=color_var).grid(row=3, column=1)

        def add_and_close():
            self.validate_freq(freq_var)
            self.validate_amp(amp_var)
            self.add_wave(freq_var.get(), amp_var.get(), wave_var.get(), color_var.get())
            self.draw_static_elements()
            self.draw_all_waves()
            win.destroy()

        ttk.Button(win, text="Add Wave", command=add_and_close).grid(row=4, column=0, columnspan=2, pady=8)

    def validate_freq(self, var):
        try:
            val = float(var.get())
            if val <= 0:
                raise ValueError
            var.set(val)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Frequency must be a positive number. Resetting to 2.0.")
            var.set(2.0)

    def validate_amp(self, var):
        try:
            val = float(var.get())
            if val <= 0:
                raise ValueError
            var.set(val)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Amplitude must be a positive number. Resetting to 60.0.")
            var.set(60.0)

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
        freq = max(wave["freq"].get(), 0.001)
        amp = wave["amp"].get()
        
        base_speed = 200
        # Higher cap for better movement visibility
        wave_speed = min(base_speed * (freq / 1.0), 1000)  # Max 1000 px/s
        
        wavelength = wave_speed / freq
        k = 2 * math.pi / wavelength if wavelength > 0 else 0
        
        phase = k * (x - wave_speed * t)
        
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

        # Consistent dt without freq scaling for smooth movement
        dt = 0.016 * self.speed.get()
        self.t += dt

        self.draw_all_waves()
        self.after(16, self.animate)

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
        # Ultra-fine step to capture all oscillations
        step = 1  # Plot every pixel for maximum detail

        for wave in self.waves:
            points = [(x, self.generate_wave_y(x, self.t, wave))
                      for x in range(0, w + 1, step)]
            flat = [coord for point in points for coord in point]
            self.canvas.create_line(*flat, fill=wave["color"],
                                    width=2, tags="wave", smooth=True)