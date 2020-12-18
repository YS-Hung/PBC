# 參數命名
calories_quota = 1500
typeList = ["全穀根莖類", "蔬菜類", "水果類", "油脂與堅果種子類", "蛋豆魚肉類(高脂)", "蛋豆魚肉類(中脂)", "蛋豆魚肉類(低脂)", "奶類(全脂)", "奶類(低脂)", "奶類(脫脂)"]
unit_cal_list = [70, 25, 60, 45, 120, 75, 55, 150, 120, 80]



import tkinter as tk


class Page2(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):

# 調整字體
        import tkinter.font as tkFont
        f1 = tkFont.Font(size = 16, family = "微軟正黑體")

#  標題
        self.Calories_quota_label = tk.Label(self, text = "本人今日熱量攝取上限為" + str(calories_quota) + "大卡", font = f1)
        self.Calories_quota_label.grid(row = 0, column = 0)

# 食物類別選單
        self.type = tk.StringVar()
        self.type.set("食物類別")
        self.optionmenu = tk.OptionMenu(self, self.type, *typeList)
        self.optionmenu.grid(row = 1, column = 0, sticky = tk.N + tk.W)
        self.optionmenu.config(font = f1)

# 單位選擇
        self.unit = tk.Spinbox(self, from_=0, to=10, increment = 0.5, font = f1)
        self.unit.grid(row = 2, column = 0, sticky = tk.N + tk.W)
        unit_label = tk.Label(self, text = "份", font = f1)
        unit_label.grid(row = 2, column = 1)

# 下一個食物
        nxt_foodbtn = tk.Button(self, text = "輸入下一份食物", font = f1)
        nxt_foodbtn.grid(row = 4, column = 0, sticky = tk.W)
# 此餐統計
        end_inputbtn = tk.Button(self, text = "此餐統計", font = f1, command = self.Calories_consume)
        end_inputbtn.grid(row = 4, column = 1, sticky = tk.W)





### 運算part


    def Calories_consume(self):
        unit_cal_consume = unit_cal_list[typeList.index(self.type.get())]
        unit = float(self.unit.get())
        calories_consume = unit_cal_consume*unit
        import tkinter.font as tkFont
        f1 = tkFont.Font(size = 16, family = "微軟正黑體")
        consumption_label = tk.Label(self, text = "此餐攝取" + str(calories_consume) +"大卡", font = f1)
        consumption_label.grid(row = 5, columnspan = 3)




p2 = Page2()
p2.master.title("page2")
p2.mainloop()


































