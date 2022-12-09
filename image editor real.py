from graphics import*
from button import*

def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red - 50
            green = green - 50
            blue = blue - 50

            if blue < 0:
                blue = 0
            if green < 0:
                green = 0
            if red < 0:
                red = 0

            #print([red, green, blue])
            c = color_rgb((red), (green), (blue))
            img.setPixel(i, j, c)

def lighten(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red + 50
            green = green + 50
            blue = blue + 50

            if blue > 255:
                blue = 255
            if green > 255:
                green = 255
            if red > 255:
                red = 255

            #print([red, green, blue])
            c = color_rgb(abs(red), abs(green), abs(blue))
            img.setPixel(i, j, c)

def grayScale(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]

            if((red == green) and (green == blue)):
                c = color_rgb(red, green, blue)
            else:
                x = (red+green+blue)/3
                c = color_rgb(int(x), int(x), int(x))
                img.setPixel(i, j, c)

def contrast(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]

            total = red + green + blue
            if total > 380:
                red = red + 25
                green = green + 25
                blue = blue + 25
                if red > 255:
                    red = 255
                if blue > 255:
                    blue = 255
                if green > 255:
                    green = 255
                
            else:
                red = red - 25
                green = green - 25
                blue = blue - 25
                if red < 0:
                    red = 0
                if blue < 0:
                    blue = 0
                if green < 0:
                    green = 0

            c = color_rgb((red), (green), (blue))
            img.setPixel(i, j, c)
            
def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("cyan")

    I = Image(Point(300, 300), "cats.png")
    I.draw(win)

    B = Button(win, Point(600, 10), Point(700, 75), "tomato", "Darken")
    B2 = Button(win, Point(600, 100), Point(700, 175), "tomato", "Lighten")
    B3 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Grayscale")
    B4 = Button(win, Point(600, 300), Point(700, 375), "tomato", "Contrast")

    Q = Button(win, Point(600, 400), Point(700, 475), "misty rose", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            

        if B2.isClicked(m):
            lighten(I)

        if B3.isClicked(m):
            grayScale(I)

        if B4.isClicked(m):
            contrast(I)
            

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
