import tkinter as tk
from wave_sim import WaveSimulator

def main():
    root = tk.Tk()
    root.title("WaveLab: A Simulation-Based Learning Tool for Sound Waves")
    # Set initial size
    window_width = 900
    window_height = 650
    root.geometry(f"{window_width}x{window_height}")

    # Force update before centering
    root.update_idletasks()

    # Calculate center position
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Apply centered geometry
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # -------------------------------------------
    # CYBERPUNK NEON TITLE BANNER (AUTO-CENTER)
    # -------------------------------------------
    title_canvas = tk.Canvas(root, height=85, bg="#0a0a0f",
                             highlightthickness=0, bd=0)
    title_canvas.pack(fill="x")

    neon1 = "#ff00ff"
    neon2 = "#00e5ff"
    neon3 = "#8f00ff"

    # Graphic elements
    round_left = title_canvas.create_oval(0, 0, 0, 0, fill="#11111a", outline="")
    round_right = title_canvas.create_oval(0, 0, 0, 0, fill="#11111a", outline="")
    rect_mid = title_canvas.create_rectangle(0, 0, 0, 0, fill="#11111a", outline="")

    title = title_canvas.create_text(
        0, 0,
        text="W A V E L A B",
        fill=neon1,
        font=("Orbitron", 27, "bold"),
        anchor="center"
    )

    def resize_banner(event=None):
        w = root.winfo_width()
        h = title_canvas.winfo_height()

        # Resize shapes
        title_canvas.coords(round_left, 10, 10, 90, h - 10)
        title_canvas.coords(round_right, w - 90, 10, w - 10, h - 10)
        title_canvas.coords(rect_mid, 50, 10, w - 50, h - 10)

        # Measure text width and adjust centering
        bbox = title_canvas.bbox(title)
        if bbox:
            text_width = bbox[2] - bbox[0]
            title_canvas.coords(title, (w // 2), h // 2)

    # Run once after window loads
    root.after(100, resize_banner)

    # Neon glow cycle
    def glow():
        current = title_canvas.itemcget(title, "fill")
        next_color = neon2 if current == neon1 else neon3 if current == neon2 else neon1
        title_canvas.itemconfig(title, fill=next_color)
        root.after(320, glow)

    glow()
    # -------------------------------------------

    try:
        root.option_add("*Font", ("Segoe UI", 10))
    except:
        pass

    sim = WaveSimulator(root)

    def on_resize(event):
        resize_banner()
        sim.draw_static_elements()
        sim.draw_all_waves()

    root.bind("<Configure>", on_resize)
    root.mainloop()

if __name__ == "__main__":
    main()
