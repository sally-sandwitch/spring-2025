import assignments.pair.p2.graphics as g

def main():
    width=400
    height=400
    win=g.GraphWin('Bouncing Ball', width, height)
    win.setBackground("#581845")

    x=50.0
    y=50.0
    radius=10.0
    dx=1.0
    dy=0.5

    c=g.Circle(g.Point(x,y), radius)
    c.setFill("#FF5733")
    c.draw(win)

    while win.checkMouse() is None:
        x+=dx
        y+=dy
        c.move(dx,dy)


    win.getMouse()
    win.close()

if __name__=="__main__":
    main()