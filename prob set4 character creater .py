from graphics import*
from button import*

def main():

    win = GraphWin("Create a Monster", 800, 600)
    win.setBackground("misty rose")

    Head = Circle(Point(300, 300), 250)
    Head.setFill("spring green")
    Head.draw(win)

    OneEye1 = Circle(Point(300, 200), 100)
    OnePupil1 = Circle(Point(300, 200), 50)
    OneEye1.setFill("misty rose")
    OnePupil1.setFill("blue")

    Eyes1 = Circle(Point(200, 250), 75)
    Eyes2 = Circle(Point(400, 250), 75)
    EyesP1 = Circle(Point(200, 250), 55)
    EyesP2 = Circle(Point(400, 250), 55)
    Eyes1.setFill("misty rose")
    Eyes2.setFill("misty rose")
    EyesP1.setFill("blue")
    EyesP2.setFill("blue")

    BigNose = Circle(Point(300, 325), 60)
    SmallNose = Circle(Point(300, 325), 30)
    BigNose.setFill("green")
    SmallNose.setFill("green")
    
    OpenMouth = Circle(Point(300, 450), 80)
    ClosedMouth = Line(Point(250, 450), Point(350, 450))
    OpenMouth.setFill("red")

    B1 = Button(win, Point(600, 10), Point(700, 75), "HotPink1", "One Eye")
    B2 = Button(win, Point(600, 100), Point(700, 175), "HotPink1", "Two Eyes")
    B3 = Button(win, Point(600, 200), Point(700, 275), "HotPink1", "Big Nose")
    B4 = Button(win, Point(600, 300), Point(700, 375), "HotPink1", "Small Nose")
    B5 = Button(win, Point(600, 400), Point(700, 475), "HotPink1", "Open Mouth")
    B6 = Button(win, Point(600, 500), Point(700, 575), "HotPink1", "Closed Mouth")
    B7 = Button(win, Point(500, 500), Point(550, 575), "HotPink2", "Quit")


    while True:
        m = win.getMouse()

        if B1.isClicked(m):
            Eyes1.undraw()
            Eyes2.undraw()
            
            OneEye1.undraw()
            OneEye1.draw(win)

            EyesP1.undraw()
            EyesP2.undraw()
            
            OnePupil1.undraw()
            OnePupil1.draw(win)

        if B2.isClicked(m):
            OneEye1.undraw()

            Eyes1.undraw()
            Eyes2.undraw()
            Eyes1.draw(win)
            Eyes2.draw(win)

            OnePupil1.undraw()

            EyesP1.undraw()
            EyesP2.undraw()
            EyesP1.draw(win)
            EyesP2.draw(win)

        if B3.isClicked(m):
            BigNose.undraw()

            SmallNose.undraw()

            BigNose.draw(win)

        if B4.isClicked(m):
            SmallNose.undraw()

            BigNose.undraw()

            SmallNose.draw(win)

        if B5.isClicked(m):
            OpenMouth.undraw()
            ClosedMouth.undraw()

            OpenMouth.draw(win)

        if B6.isClicked(m):
            ClosedMouth.undraw()
            OpenMouth.undraw()

            ClosedMouth.draw(win)

        if B7.isClicked(m):
            break







if __name__ == "__main__":
    main()
