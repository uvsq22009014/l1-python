import tkinter as tk

RAYON = 50

def draw_pixel(i, j, color="red"):
    """ affiche le pixel de coordonnées (i,j) dans le canevas avec la couleur color """
    canvas.create_line((i, j), (i+1, j), fill=color)

def affiche_pixel(event):
    draw_pixel(event.x, event.y)

def cree_cercle(event):
    if event.x >= 250:
        col="blue"
    else:
        col="red"
    canvas.create_oval((event.x-RAYON, event.y-RAYON), (event.x+RAYON, event.y+RAYON), fill=col)

racine = tk.Tk()

canvas = tk.Canvas(racine, width=500, height=500, bg="black")
canvas.grid()
canvas.bind("<Button-1>", cree_cercle)

canvas.create_line((250, 0), (250, 500), fill = "white")

racine.mainloop()