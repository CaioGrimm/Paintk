import tkinter as tk

class Paintk():

    def __init__(self) -> None:

        self.window = tk.Tk()
        self.window.title("Paintk")
        self.window.minsize(width=1000, height=500)
        self.window.resizable(0, 0) # type: ignore

        self.img_eraser = tk.PhotoImage(file="icons/eraser.png")
        self.img_line = tk.PhotoImage(file="icons/line.png")
        self.img_new = tk.PhotoImage(file="icons/new.png")
        self.img_oval = tk.PhotoImage(file="icons/oval.png")
        self.img_save = tk.PhotoImage(file="icons/save.png")
        self.img_square = tk.PhotoImage(file="icons/square.png")

        self.colors = ("black","white","yellow","green","orange","blue","purple","pink","red")

        self.bar_menu = tk.Frame(self.window, bg="#3b3b3b",height=30)
        self.bar_menu.pack(fill="x")

        self.text_color = tk.Label(self.bar_menu, text="Colors: ", fg="white", bg="#3b3b3b")
        self.text_color.pack(side="left")

        for i in self.colors:
            self.button_color = tk.Button(self.bar_menu, bg=i, width=5, height=2)
            self.button_color.pack(side="left")

        self.text_brushs = tk.Label(self.bar_menu, text="  Brushs:  ", fg="white", bg="#3b3b3b")
        self.text_brushs.pack(side="left")

        self.pen_size = tk.Spinbox(self.bar_menu, from_=1, to=50)
        self.pen_size.pack(side="left")

        self.text_brushs = tk.Label(self.bar_menu, text="  Brushs:  ", fg="white", bg="#3b3b3b")
        self.text_brushs.pack(side="left")

        self.button_line = tk.Button(self.bar_menu, image=self.img_line, bd=0)
        self.button_line.pack(side="left")
        
        self.button_oval = tk.Button(self.bar_menu, image=self.img_oval, bd=0)
        self.button_oval.pack(side="left")

        self.button_eraser = tk.Button(self.bar_menu, image=self.img_eraser, bd=0)
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

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Paintk()
    app.run()