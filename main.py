import tkinter as tk

class Paintk():

    def __init__(self) -> None:

        self.window = tk.Tk()
        self.window.title("Paintk")
        self.window.minsize(width=720, height=500)
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

        self.area_draw = tk.Canvas(self.window, height=470, bg="red")
        self.area_draw.pack(fill="both")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Paintk()
    app.run()