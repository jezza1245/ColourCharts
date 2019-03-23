from tkinter import *
import random

window = Tk()
window.geometry('900x600')
window.title("Colour Palette")
window.configure(bg="#E0E0E0")


#Save colours to stop if from changing, On/Off



class ColourArea:

    def __init__(self, colour, x):
        self.hex = colour
        self.x = x
        self.widget = Frame(colours, borderwidth=1, relief=GROOVE)
        self.colour = Label(self.widget, bg=self.hex)
        self.hex_text = Label(self.widget, text=self.hex, bg = "#D0D0D0")
        self.rgb_text = Label(self.widget, text=hexToRgb(self.hex), bg="#D0D0D0")
        self.keep = False

    def toggleKeep(self):
        print(self.keep)
        if self.keep:
            self.keep = False
            self.render()
        else:
            self.keep = True
            self.render()

    def render(self):
        self.widget.place(relx = self.x, rely = 0.2, relwidth = 0.18, relheight=0.6)
        self.colour.place(relx = 0, rely = 0, relwidth = 1, relheight=0.8)
        self.colour.bind('<Button-1>', lambda x:self.toggleKeep())
        if self.keep:
            self.colour.configure(highlightbackground = 'white', borderwidth=3, relief=SUNKEN)
        else:
            self.colour.configure(highlightbackground = 'white', borderwidth=3, relief=RAISED)
        self.hex_text.place(relx = 0, rely = 0.8, relwidth = 1, relheight=0.1)
        self.rgb_text.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

def getRandomColour():
    r = lambda: random.randint(0, 255)
    print('#%02X%02X%02X' % (r(), r(), r()))
    colour = '#{:02x}{:02x}{:02x}'.format(r(), r(), r())
    return colour

def hexToRgb(hex):
    hex = hex.lstrip('#')
    length=len(hex)

    return tuple(int(hex[i:i+length//3], 16)
    for i in range(0,length,length//3))


def renderColours():
    for c in blocks:
        if not c.keep:

            c.colour.destroy()
            c.hex_text.destroy()
            c.rgb_text.destroy()

            c.hex = getRandomColour()
            c.colour = Label(c.widget, bg=c.hex)
            c.hex_text = Label(c.widget, text=c.hex, bg="#D0D0D0")
            c.rgb_text = Label(c.widget, text=hexToRgb(c.hex), bg="#D0D0D0")

            c.render()


# Draw colour blocks
colours = Frame(window, bg="#D0D0D0").place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight=0.6)
c1 = ColourArea(colour = getRandomColour() , x = 0.1)
c2 = ColourArea(colour = getRandomColour(), x=0.26)
c3 = ColourArea(colour = getRandomColour(), x=0.42)
c4 = ColourArea(colour = getRandomColour(), x=0.58)
c5 = ColourArea(colour = getRandomColour(), x=0.74)

blocks = [c1,c2,c3,c4,c5]
renderColours()

randomButton = Button(window, text="New Colours", command= lambda: renderColours())\
    .place(relx = 0.45, rely = 0.9, relwidth=0.1, relheight= 0.05)

window.mainloop()