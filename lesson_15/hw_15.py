"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

    сторона_а (довжина сторони a).
    кут_а (кут між сторонами a і b).
    кут_б (суміжний з кутом кут_а).

Необхідно реалізувати наступні вимоги:

    Значення сторони сторона_а повинно бути більше 0.
    Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
    Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення
    кут_б обчислюється автоматично.
    Для встановлення значень атрибутів використовуйте метод __setattr__.
"""

class Rhombus:
    def __init__(self, side_a=None, angle_a=None):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a
        self.angle_d = (360 - angle_a*2)/2

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Значення сторони сторони 'a' повинно бути більше 0 !")
            object.__setattr__(self, name, value)
        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Значення кута має бути в діапазоні 180 градусів !")
            object.__setattr__(self, name, value)
        else:
            object.__setattr__(self, name, value)

    def __str__(self):
        return f'Side a = {self.side_a}, angle a = {self.angle_a}, angle b = {self.angle_b}, angle d = {self.angle_d}'
   
romb = Rhombus(8,60)
print(romb) # Side a = 8, angle a = 50, angle b = 130, angle d = 130.0