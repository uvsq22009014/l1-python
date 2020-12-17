import tkinter as tk

cpt = 0

def remplit_vide(event) :
    global cpt
    cpt += 1
    if cpt == 10:
        racine.destroy()
    if cpt % 2 == 1:
        color = "red"
    else:
        color = "black"
    canvas.itemconfigure(carre, fill=color)



racine = tk.Tk()

canvas = tk.Canvas(racine, width=500, height=500, bg="black")
canvas.grid()
canvas.bind("<Button-1>", remplit_vide)

carre = canvas.create_rectangle((100, 100), (300, 300), fill="black", outline="red")

racine.mainloop()