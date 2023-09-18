import math


class MyMath:
    """Класс различных математических вычислений, связанных с фигурами."""

    @classmethod
    def circle_len(cls, radius: float) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, side: float) -> float:
        return side ** 3

    @classmethod
    def sphere_surface(cls, radius: float) -> float:
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(side=2.5)
res_4 = MyMath.sphere_surface(radius=4)
print(res_1)
print(res_2)
print(res_3)
print(res_4)

# зачтено
