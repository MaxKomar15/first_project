class Title:
    def __init__(self, title_text, x, y):
        self.x = x
        self.y = y
        self.appear = True

    def print_info(self):
        print("Кнопка", self.title)
        print("Розташування: (", self.x, self.y, ")")
        print("Видимість:", self.appear)

    def hide(self):
        self.apear = False
        print("Напис приховано")

t1 = Title("Ок", 200, 250)
t1.print_info()
t1.hide()