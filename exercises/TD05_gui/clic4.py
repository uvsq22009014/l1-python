import tkinter as tk

cpt = 0
x,y = 0,0
def cree_line(event) :
    global cpt
    global x , y
    cpt += 1
    if cpt % 2 == 1 :
        x = event.x
        y= event.y
    else :
        if event.x > 250 and x > 250 :
            color = 'blue'
        elif event.x < 250 and x < 250 : 
            color = 'blue'
        else :
            color = 'red'
    
        canvas.create_line((x, y), (event.x, event.y), fill=color)




racine = tk.Tk()

canvas = tk.Canvas(racine, width=500, height=500, bg="black")
canvas.grid()
#canvas.bind("<Button-1>", cree_line)
canvas.create_rectangle((200, 200), (300, 300), fill = "black", outline = "white")
#canvas.create_line((250, 0), (250, 500), fill = "white")
racine.mainloop()