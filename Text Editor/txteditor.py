from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
import os

class TextEditor:
    counter = 1

    def donothing(self):
        filewin = Toplevel(self.root)
        button = Button(filewin, text="Do not do anything")
        button.pack()

    def open_file(self):
        self.file = askopenfile(mode='r')
        if self.file:
            self.text.delete(1.0, "end-1c")
            content = self.file.read()
            self.filename = self.file.name
            self.text.insert(INSERT, content)
            self.root.title(f"{os.path.basename(self.filename)} - TryCatch Text Editor")

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as f:
                self.text_data = self.text.get(1.0, "end-1c")
                f.write(self.text_data)
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file = asksaveasfile()
        if self.file:
            self.filename = self.file.name
            with open(self.filename, "w") as f:
                self.text_data = self.text.get(1.0, "end-1c")
                f.write(self.text_data)
            self.root.title(f"{os.path.basename(self.filename)} - TryCatch Text Editor")

    def close_file(self):
        self.text.delete(1.0, "end-1c")
        self.root.title("Untitled - TryCatch Text Editor")
        self.file = None
        self.filename = None

    def new(self):
        TextEditor.counter += 1
        TextEditor()

    def dark(self):
        self.text.config(foreground="white", background="black", insertbackground="white")

    def light(self):
        self.text.config(foreground="black", background="white", insertbackground="black")

    def __init__(self):
        self.root = Tk()
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.root.title("Untitled - TryCatch Text Editor")

        self.file = None
        self.filename = None

        # Menu Bar
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As", command=self.save_as_file)
        filemenu.add_command(label="Close", command=self.close_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Dark", command=self.dark)
        editmenu.add_command(label="Light", command=self.light)
        menubar.add_cascade(label="Theme", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

        # Text Field
        self.text = Text(self.root)
        self.text.pack()
        self.text.config(insertbackground="black")

        # Load Icon
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "edit-text.png")
        if os.path.exists(image_path):
            self.photo = PhotoImage(file=image_path)
            self.root.iconphoto(False, self.photo)

        self.root.mainloop()

# Start Application
TextEditor()
