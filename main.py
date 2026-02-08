from __future__ import annotations
import tkinter as tk

WINDOW_TITLE = "PyCraft"
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

FPS = 60
FRAME_TIME = int(1000 / FPS)

root: tk.Tk = None
canvas: tk.Canvas = None

class Entity:
    name: str = None
    xpos: int = None 
    ypos: int = None 
    width: int = None 
    height: int = None 
    xpos_end: int = None 
    ypos_end: int = None
    color: str = None

    def __init__(self, xpos: int, ypos: int, width: int, height: int):
        self.xpos = xpos 
        self.ypos = ypos
        self.width = width
        self.height = height
        self.xpos_end = self.xpos + self.width
        self.ypos_end = self.ypos + self.height

    def draw(self, canvas: tk.Canvas):
        print("Drawing... " + str(self))
        canvas.create_rectangle(self.xpos, self.ypos, self.xpos_end, self.ypos_end, fill=f"{self.color}")

    def __str__(self):
        return f"{self.name} ({self.xpos}, {self.ypos})"


class Player(Entity):
    def __init__(self, xpos: int, ypos: int):
        self.name = "Player"
        self.xpos = xpos 
        self.ypos = ypos
        self.width = 20
        self.height = 20
        self.color = "red"
        super().__init__(xpos, ypos, 20, 20)


def update():
    print("Running...")

    root.after(FPS, update)

def main():
    global root
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    global canvas
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
    player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    player.draw(canvas)

    canvas.pack()

    update()
    root.mainloop()

if __name__ == "__main__": 
    main()