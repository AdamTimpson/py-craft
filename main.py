from __future__ import annotations
import tkinter as tk

WINDOW_TITLE: str = "PyCraft"
WINDOW_WIDTH: int = 1920
WINDOW_HEIGHT: int = 1080

FPS: int= 60
FRAME_TIME: int = int(1000 / FPS)

X_TILE_COUNT: int = 48
Y_TILE_COUNT: int = 27

tiles: list[Tile] = []

root: tk.Tk = tk.Tk()
canvas: tk.Canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")

class Tile: 
    id: int = 0
    xpos: int = 0
    ypos: int = 0
    width: int = int(WINDOW_WIDTH / X_TILE_COUNT)
    height: int = int(WINDOW_HEIGHT / Y_TILE_COUNT)
    fill_colour: str = "white"

    def __init__(self, xpos: int, ypos: int, fill_colour="white") -> None:
        self.id = Tile.id + 1 # Static?? 
        Tile.id = Tile.id + 1 # I don't like this but I don't like largest_tile_id either...
        self.xpos = xpos
        self.ypos = ypos 
        self.fill_colour = fill_colour

    def __str__(self) -> str:
        return f"{self.id}: ({self.xpos}, {self.ypos})"

def update() -> None:
    root.after(FPS, update)

def init_window() -> None: 
    root.title(WINDOW_TITLE)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    canvas.pack()
    
    update()

def draw_grid() -> None:
    for i in range(0, X_TILE_COUNT):
        for j in range(0, Y_TILE_COUNT):
            tile = Tile(i * Tile.width, j * Tile.height)
            print(tile)
            
            tiles.append(tile)
            fill: str = "black"
    
            if tile.id % 10 == 0 and tile.id % 2 == 0:
                fill="green"

            canvas.create_rectangle(
                    tile.xpos, 
                    tile.ypos, 
                    tile.xpos + tile.width, 
                    tile.ypos + tile.height, 
                    fill=fill)
            
def init_game() -> None:
    draw_grid()

def main() -> None:
    init_window()

    init_game()

    root.mainloop()

if __name__ == "__main__": 
    main()
