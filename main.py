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

    # Create frames
    start_frame = tk.Frame(root, bg="#0a0a0f")
    main_frame = tk.Frame(root, bg="#0a0a0f")

    # Initially show start frame
    start_frame.pack(fill="both", expand=True)

    # -------------------------------------------
    # START PAGE (WELCOME SCREEN)
    # -------------------------------------------
    welcome_canvas = tk.Canvas(start_frame, bg="#0a0a0f", highlightthickness=0, bd=0)
    welcome_canvas.pack(fill="both", expand=True)

    neon1 = "#ff00ff"
    neon2 = "#00e5ff"
    neon3 = "#8f00ff"

    # Welcome title
    welcome_title = welcome_canvas.create_text(
        0, 0,
        text="WELCOME TO WAVELAB!",
        fill=neon1,
        font=("Orbitron", 32, "bold"),
        anchor="center"
    )

    # Subtitle
    subtitle = welcome_canvas.create_text(
        0, 0,
        text="A Simulation-Based Learning Tool for Sound Waves",
        fill=neon2,
        font=("Orbitron", 18),
        anchor="center"
    )

    # Description
    description = welcome_canvas.create_text(
        0, 0,
        text="Explore the fascinating world of sound waves through interactive simulations.\nLearn about frequency, amplitude, interference, and more!",
        fill="#ffffff",
        font=("Segoe UI", 12),
        anchor="center",
        justify="center"
    )

    # Start button
    start_button = tk.Button(
        start_frame,
        text="START SIMULATION",
        command=lambda: switch_to_main(),
        bg="#11111a",
        fg=neon1,
        font=("Orbitron", 14, "bold"),
        relief="flat",
        bd=0,
        padx=20,
        pady=10,
        activebackground="#222233",
        activeforeground=neon2
    )
    start_button.pack(side="bottom", pady=50)

    def resize_welcome(event=None):
        w = welcome_canvas.winfo_width()
        h = welcome_canvas.winfo_height()
        if w > 1 and h > 1:  # Ensure canvas is rendered
            welcome_canvas.coords(welcome_title, w // 2, h // 4)
            welcome_canvas.coords(subtitle, w // 2, h // 4 + 60)
            welcome_canvas.coords(description, w // 2, h // 2 + 50)

    # Bind resize to the canvas itself for better responsiveness
    welcome_canvas.bind("<Configure>", resize_welcome)
    # Initial call after a short delay
    root.after(200, lambda: resize_welcome() if welcome_canvas.winfo_width() > 1 else None)

    # Neon glow for title
    def glow_welcome():
        current = welcome_canvas.itemcget(welcome_title, "fill")
        next_color = neon2 if current == neon1 else neon3 if current == neon2 else neon1
        welcome_canvas.itemconfig(welcome_title, fill=next_color)
        root.after(320, glow_welcome)

    glow_welcome()

    # -------------------------------------------
    # MAIN SIMULATION FRAME
    # -------------------------------------------
    # CYBERPUNK NEON TITLE BANNER (AUTO-CENTER)
    title_canvas = tk.Canvas(main_frame, height=100, bg="#0a0a0f",  # Increased height for better visibility
                             highlightthickness=0, bd=0)
    title_canvas.pack(fill="x")

    # Graphic elements
    round_left = title_canvas.create_oval(0, 0, 0, 0, fill="#11111a", outline="")
    round_right = title_canvas.create_oval(0, 0, 0, 0, fill="#11111a", outline="")
    rect_mid = title_canvas.create_rectangle(0, 0, 0, 0, fill="#11111a", outline="")

    title = title_canvas.create_text(
        0, 0,
        text="WAVELAB",
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

        # Center the title vertically in the canvas
        title_canvas.coords(title, w // 2, h // 2)

    # Neon glow cycle for main title
    def glow():
        current = title_canvas.itemcget(title, "fill")
        next_color = neon2 if current == neon1 else neon3 if current == neon2 else neon1
        title_canvas.itemconfig(title, fill=next_color)
        root.after(320, glow)

    try:
        root.option_add("*Font", ("Segoe UI", 10))
    except:
        pass

    sim = WaveSimulator(main_frame)  # Pass main_frame instead of root

    def switch_to_main():
        start_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        resize_banner()
        sim.draw_static_elements()
        # Removed draw_all_waves from here to prevent initial lag; assume WaveSimulator handles its own animation
        glow()  # Start glow for main title

    def on_resize(event):
        resize_banner()
        sim.draw_static_elements()
        # Removed draw_all_waves from resize to reduce lag; if WaveSimulator needs it, add back with throttling

    main_frame.bind("<Configure>", on_resize)

    root.mainloop()

if __name__ == "__main__":
    main()
