class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weight=15, thickness=3):
        return f"{self._length} m * {self._width} m * {weight} kg * {thickness} cm =" \
               f"{(self._length * self._width * weight * thickness) / 100} t"
road_1 = Road(12000, 30)
print(road_1.get_full_profit())
