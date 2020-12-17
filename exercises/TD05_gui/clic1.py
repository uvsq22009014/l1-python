import tkinter as tk

def draw_pixel(i, j, color="red"):
    """ affiche le pixel de coordonnées (i,j) dans le canevas avec la couleur color """
    canvas.create_line((i, j), (i+1, j), fill=color)

def affiche_pixel(event):
    draw_pixel(event.x, event.y)

racine = tk.Tk()
canvas = tk.Canvas(racine, width=500, height=500, bg="black")
canvas.grid()
canvas.bind("<Button-1>", affiche_pixel)


racine.mainloop()