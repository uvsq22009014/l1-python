import tkinter as tk
import random as rd

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def ecran_aleatoire():
    color = get_color(rd.randint(0, 255),rd.randint(0, 255), rd.randint(0, 255))



root = tk.Tk()

bouton_aleatoire = tk.button(root, text = "aléatoire", bg = "grey100", fg = "blue", padx = 20, font = ("Times", "20"), commad = ecran_aleatoire)
bouton_gris_deg = tk.button(root, text = "dégradé gris", bg = "grey100", fg = "blue", padx = 20, font = ("Times", "20"))
bouton_gris_2d = tk.button(root, text = "dégradé 2D", bg = "grey100", fg = "blue", padx = 20, font = ("Times", "20"))

canvas_height = 256
canvas_width = 256

canvas = tk.Canvas(root, width = canvas_width, height = canvas_height, bg = "black", bd = 10, relief = "raised")

bouton_aleatoire.grid(column = 0, row = 1)
bouton_gris_deg.grid(column = 0, row = 2)
bouton_gris_2d.grid(column = 0, row = 3)

canvas.grid(column = 1, row = 1, rowspan = 3)

def draw_pixel(i,j,color):
    canvas.create_line((i,j), (i + 1, j), fill = color)
    return

root.mainloop()