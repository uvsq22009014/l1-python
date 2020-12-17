import tkinter as tk

cpt = 0
cercles = []

def dessine_cercles(event) :
    global cpt
    global cercles
    cpt += 1
    if cpt < 9:
        new_cercle = canvas.create_oval((event.x-50, event.y-50), (event.x+50, event.y+50), fill="red")
        cercles.append(new_cercle)
    elif cpt == 9:
        for c in cercles:
            canvas.itemconfigure(c, fill="yellow")
    else:
        for c in cercles:
            canvas.delete(c)
        cercles = []
        cpt = 0




racine = tk.Tk()

canvas = tk.Canvas(racine, width=500, height=500, bg="black")
canvas.grid()
canvas.bind("<Button-1>", dessine_cercles)


racine.mainloop()