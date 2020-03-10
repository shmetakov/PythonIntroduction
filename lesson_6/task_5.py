class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки! {self.title} Pen")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки! {self.title} Pencil")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки! {self.title} Handle")


stationery = Stationery("палец")
stationery.draw()

pen = Pen("Mister Parker")
pen.draw()

pencil = Pencil("Stabilo Schwan Art")
pencil.draw()

handle = Handle("Centropen")
handle.draw()
