class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_weight(self):
        return self._length * self._width * 0.025 * 5


road = Road(5000, 20)
print(f"Вес: {road.get_weight()}т")
