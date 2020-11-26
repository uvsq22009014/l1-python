import tkinter as tk
import random as rd

racine = tk.Tk()
racine.title("Mon dessin")

def cercle() :
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    canvas.create_oval((x, y), (x+100, y+100), fill = color)

def carre() :
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    canvas.create_rectangle((x, y), (x+100, y+100), fill = color)

def croix() :
    x = rd.randint(0, 400)
    y = rd.randint(0, 400)
    canvas.create_line((x, y), (x+100, y+100), fill = color)
    canvas.create_line((x+100, y), (x, y+100), fill = color)

def choisirCouleur() :
    global color
    color = input("choisir une couleur")


#création des widgets
bouton_couleur = tk.Button(racine, text = "Choisir une couleur", bg = "grey100", fg = "blue", padx = 20, font = ("Times", "20"))
bouton_cercle = tk.Button(racine, text = "Cercle", bg = "grey100", fg = "blue", padx = 20, font = ("Times", "20"), command = cercle)
bouton_carre = tk.Button(racine, text = "Carré", bg = "grey100", fg = "blue", padx = 20, font = ("Times", "20"), command=carre)
bouton_croix = tk.Button(racine, text = "Croix", bg = "grey100", fg = "blue", padx = 20, font = ("Times", "20"), command=croix)

canvas = tk.Canvas(racine, width = 500, height = 500, bg = "black", bd = 10, relief = "raised")

#placement des widgets
bouton_couleur.grid(column = 1, row = 0)
bouton_cercle.grid(column = 0, row = 1)
bouton_carre.grid(column = 0, row = 2)
bouton_croix.grid(column = 0, row = 3)

canvas.grid(column = 1, row = 1, rowspan = 3)

racine.mainloop()