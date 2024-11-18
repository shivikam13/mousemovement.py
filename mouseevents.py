import pgzrun

WIDTH=500
HEIGHT=500
points=[]
clicked=False


def draw():
    screen.clear()
    screen.fill("red")
    for i in range(len(points)-1):
        screen.draw.line(points[i], points[i + 1], "black")
        

def update():
    pass

def on_mouse_down():
    global clicked
    clicked=True
    points.clear()

def on_mouse_up():
    global clicked
    clicked=False

def on_mouse_move(pos):

    # if mouse is clicked, add positions to be drawn

    if clicked:

        points.append(pos)




pgzrun.go()