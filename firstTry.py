from tkinter import *
from PIL import ImageTk, Image
from colorutils import Color, ArithmeticModel, rgb_to_hex, hex_to_rgb

from colors import colorme

black = "#000000"
white = "#FFFFFF"
blue = "#0047ab"
green = "#00B500"
yellow = "#FFED00"
red = "#FF0000"
red1 = "#FF6666"
red2 = "#FF9999"
red3 = "#FFCCCC"
violet = "#FF00AB"
orange = "#FF7700"
purple = "#800080"
gray = "#808080"
gold = "#FFD700"

colors = {'r': red,
          'r1': red1,
          'r2': red2,
          'r3': red3,
          'o': orange,
          'y': yellow,
          'g': green,
          'b': blue,
          'p': purple,
          'v': violet
          }


class MyCanvas:

    def __init__(self, top):
        self.buttons = {}
        self.triangles = {}
        self.blocks = {}
        self.ovals = {}
        self.present = {}
        self.top = top
        self.canvas = Canvas(top, bg=gray, height=1000, width=1000)

    def rectangle(self, points, color):
        self.canvas.create_rectangle(points, fill=color)

    def triangle(self, points, color):
        if color[0] is not 's':
            self.present[color[0]] = colors[color[0]]
            self.triangles[color] = self.canvas.create_polygon(points, fill=colors[color[0]])

        else:
            self.triangles[color] = self.canvas.create_polygon(points, fill='silver')

    def oval(self, a, b, c, d, color, name):
        self.ovals[name] = self.canvas.create_oval(a, b, c, d, fill=color)

    def done(self):
        self.canvas.pack(fill=BOTH, expand=1)

    def button(self, x, y, name):
        self.buttons[name] = [Button(self.top, height=100, bg=white, command=lambda: self.callback(name)), 'w']
        self.blocks[name[0]] = 4
        self.buttons[name][0].pack()
        self.buttons[name][0].place(bordermode=OUTSIDE, height=30, width=40, x=x, y=y)

    def callback(self, name):
        if self.buttons[name][1] == 'b':
            self.buttons[name][0].configure(bg=white)
            self.buttons[name][1] = 'w'
            self.blocks[name[0]] += 1
        else:
            self.buttons[name][0].configure(bg=black)
            self.buttons[name][1] = 'b'
            self.blocks[name[0]] -= 1

        self.calc(name[0])

    def calc(self, name):
        if self.blocks[name] == 0:
            self.canvas.itemconfig(self.triangles[name + "2"], fill=gray, stipple='')
            self.present[name] = black
        if self.blocks[name] == 1:
            self.canvas.itemconfig(self.triangles[name + "2"], fill=colors[name], stipple="gray25")
            # self.canvas.itemconfig(self.triangles[name + "2"], fill=colors[name+'3'])#, stipple="gray25")
        if self.blocks[name] == 2:
            self.canvas.itemconfig(self.triangles[name + "2"], fill=colors[name], stipple="gray50")
            # self.canvas.itemconfig(self.triangles[name + "2"], fill=colors[name+'2'])#, stipple="gray50")
        if self.blocks[name] == 3:
            self.canvas.itemconfig(self.triangles[name + "2"], fill=colors[name], stipple="gray75")
            # self.canvas.itemconfig(self.triangles[name + "2"], fill=colors[name+'1'])#, stipple="gray75")
            # self.present[name] = colors[name+'1']
        if self.blocks[name] == 4:
            self.canvas.itemconfig(self.triangles[name + "2"], fill=colors[name], stipple='')
            self.present[name] = colors[name]

        out = black
        my_list = []
        for key, color in self.present.items():
            hex_color = hex_to_rgb(color)
            item = hex_color + (0.5, 0)
            my_list.append(item)
            out = rgb_to_hex((Color(hex=color) + Color(hex=out)))

        # r_mix, g_mix, b_mix = colorme(list)
        #
        # Color((r_mix, g_mix, b_mix))
        self.canvas.itemconfig(self.ovals['o'], fill=out)


def main():
    top = Tk()

    canvas = MyCanvas(top)

    img = ImageTk.PhotoImage(Image.open("/home/eran/projects/PycharmProjects/newton/photos/img0.png"))
    panel = Label(top, image=img)
    panel.place(x=0, y=0)
    # label = tk.Label(frame, text="Hello Python Programmer!")
    # label.place(x=20, y=30)

    canvas.rectangle((750, 1000, 200, 0), gray)  # tray
    canvas.rectangle((0, 0, 200, 1000), gold)  # side left
    canvas.rectangle((750, 0, 1000, 1000), gold)  # side right

    canvas.rectangle((450, 10, 550, 50), black)  # window

    canvas.oval(480, 850, 520, 980, white, 'o')  # light out
    canvas.triangle((450, 820, 550, 820, 500, 900), 's2')  # prism 2

    canvas.oval(480, 20, 520, 150, "white", 'i')  # light in
    canvas.triangle((450, 180, 550, 180, 500, 100), 's1')  # prism 1

    canvas.triangle((500, 150, 600, 400, 650, 400), 'r1')
    canvas.triangle((500, 150, 550, 400, 600, 400), "o1")
    canvas.triangle((500, 150, 500, 400, 550, 400), "y1")
    canvas.triangle((500, 150, 450, 400, 500, 400), "g1")
    canvas.triangle((500, 150, 400, 400, 450, 400), "b1")
    canvas.triangle((500, 150, 350, 400, 400, 400), "p1")
    canvas.triangle((500, 150, 300, 400, 350, 400), "v1")

    canvas.triangle((500, 850, 600, 500, 650, 500), "r2")
    canvas.triangle((500, 850, 550, 500, 600, 500), "o2")
    canvas.triangle((500, 850, 500, 500, 550, 500), "y2")
    canvas.triangle((500, 850, 450, 500, 500, 500), "g2")
    canvas.triangle((500, 850, 400, 500, 450, 500), "b2")
    canvas.triangle((500, 850, 350, 500, 400, 500), "p2")
    canvas.triangle((500, 850, 300, 500, 350, 500), "v2")

    canvas.oval(250, 350, 700, 550, "silver", 'm')  # middle

    canvas.button(310, 390, "v1")
    canvas.button(310, 420, "v2")
    canvas.button(310, 450, "v3")
    canvas.button(310, 480, "v4")

    canvas.button(360, 390, "p1")
    canvas.button(360, 420, "p2")
    canvas.button(360, 450, "p3")
    canvas.button(360, 480, "p4")

    canvas.button(410, 390, "b1")
    canvas.button(410, 420, "b2")
    canvas.button(410, 450, "b3")
    canvas.button(410, 480, "b4")

    canvas.button(460, 390, "g1")
    canvas.button(460, 420, "g2")
    canvas.button(460, 450, "g3")
    canvas.button(460, 480, "g4")

    canvas.button(510, 390, "y1")
    canvas.button(510, 420, "y2")
    canvas.button(510, 450, "y3")
    canvas.button(510, 480, "y4")

    canvas.button(560, 390, "o1")
    canvas.button(560, 420, "o2")
    canvas.button(560, 450, "o3")
    canvas.button(560, 480, "o4")

    canvas.button(610, 390, "r1")
    canvas.button(610, 420, "r2")
    canvas.button(610, 450, "r3")
    canvas.button(610, 480, "r4")

    canvas.done()

    top.mainloop()


if __name__ == '__main__':
    main()
