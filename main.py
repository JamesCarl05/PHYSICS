import tkinter as tk
from wave_sim import WaveSimulator

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
