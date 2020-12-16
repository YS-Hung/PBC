import tkinter as tk
import tkinter.font as tkFont
import math

class Nutrition(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    


    def createWidgets(self):
        var = tk.StringVar()
        self.label = tk.Label(self, text="請問您的性別？", bg="yellow", width =15)
        self.label.pack()

        def print_selection():
            self.label.config(text="請問您的性別？"+ var.get())
        
        self.gender = tk.Radiobutton(self, text = "男", variable=var, value="男", command = print_selection)
        self.gender.pack()
        self.gender1 = tk.Radiobutton(self, text = "女", variable = var, value="女", command=print_selection)
        self.gender1.pack()
    


nutri = Nutrition()
nutri.master.title("My Nutrition Calculator")
nutri.mainloop()