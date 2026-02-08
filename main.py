import tkinter as tk

WINDOW_TITLE = "PyCraft"
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

def main():
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    root.mainloop()

if __name__ == "__main__": 
    main()