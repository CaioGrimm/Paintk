import tkinter as tk

class Paintk():

    def __init__(self) -> None:

        self.window = tk.Tk()
        self.window.title("Paintk")
        self.window.minsize(width=1000, height=500)
        self.window.resizable(0, 0) # type: ignore

        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

        self.img_eraser = tk.PhotoImage(file="icons/eraser.png")
        self.img_line = tk.PhotoImage(file="icons/line.png")
        self.img_new = tk.PhotoImage(file="icons/new.png")
        self.img_oval = tk.PhotoImage(file="icons/oval.png")
        self.img_save = tk.PhotoImage(file="icons/save.png")
        self.img_square = tk.PhotoImage(file="icons/square.png")

        self.colors = ("black","white","yellow","green","orange","blue","purple","pink","red")

        self.pick_colors = "black"

        self.bar_menu = tk.Frame(self.window, bg="#3b3b3b",height=30)
        self.bar_menu.pack(fill="x")

        self.text_color = tk.Label(self.bar_menu, text="Colors: ", fg="white", bg="#3b3b3b")
        self.text_color.pack(side="left")

        for i in self.colors:
            self.button_color = tk.Button(self.bar_menu, bg=i, width=5, height=2, command=lambda col=i:self.select_colors(col))
            self.button_color.pack(side="left")

        self.text_brushs = tk.Label(self.bar_menu, text="  Brushs:  ", fg="white", bg="#3b3b3b")
        self.text_brushs.pack(side="left")

        self.pen_size = tk.Spinbox(self.bar_menu, from_=1, to=50)
        self.pen_size.pack(side="left")

        self.text_brushs = tk.Label(self.bar_menu, text="  Brushs:  ", fg="white", bg="#3b3b3b")
        self.text_brushs.pack(side="left")

        self.button_line = tk.Button(self.bar_menu, image=self.img_line, bd=0, command=self.brush_line)
        self.button_line.pack(side="left")
        
        self.button_oval = tk.Button(self.bar_menu, image=self.img_oval, bd=0, command=self.brush_oval)
        self.button_oval.pack(side="left")

        self.button_eraser = tk.Button(self.bar_menu, image=self.img_eraser, bd=0, command=self.brush_eraser)
        self.button_eraser.pack(side="left")

        self.button_square = tk.Button(self.bar_menu, image=self.img_square, bd=0)
        self.button_square.pack(side="left")

        self.text_options = tk.Label(self.bar_menu,  text="  Options:  ", fg="white", bg="#3b3b3b")
        self.text_options.pack(side="left")

        self.button_new = tk.Button(self.bar_menu, image=self.img_new, bd=0)
        self.button_new.pack(side="left")

        self.button_save = tk.Button(self.bar_menu, image=self.img_save, bd=0)
        self.button_save.pack(side="left")

        self.area_draw = tk.Canvas(self.window, height=470, bg="red")
        self.area_draw.pack(fill="both")
        self.area_draw.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        x1 = (event.x)
        x2 = (event.x)
        y1 = (event.y)
        y2 = (event.y)

        if self.oval_brush:
            self.area_draw.create_oval(x1, y1, x2, y2, fill=self.pick_colors, outline=self.pick_colors, width=self.pen_size.get())

        elif self.line_brush :
            self.area_draw.create_line(x1 - 10, y1 - 10, x2, y2, fill=self.pick_colors, width=self.pen_size.get())
        
        else:
            self.area_draw.create_oval(x1, y1, x2, y2, fill="red", outline="red", width=self.pen_size.get())

    def select_colors(self, color):
        self.pick_colors = color
    
    def brush_oval(self):
        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

    def brush_line(self):
        self.oval_brush = False
        self.line_brush = True
        self.eraser_brush = False

    def brush_eraser(self):
        self.oval_brush = False
        self.line_brush = False
        self.eraser_brush = False

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Paintk()
    app.run()