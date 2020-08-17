from shape import Shape
import inspect


class Rectangle(Shape):
    PI = 3.14

    @classmethod
    def getPi(cls):
        return cls.PI

    def __init__(self, width, height, dimension=2):
        super().__init__(dimension)
        self.width = width
        self.height = height
        self.area = width * height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        print(w)
        if w < 0:
            raise ValueError
        self._width = w

    def desc(self):
        print('Describe')


r = Rectangle(10, 10)
print(r.area)
print(r.width)
print(r.PI)
print(r.getPi())
r.desc()

print(hasattr(r, 'getPi'))
print(inspect.getfullargspec(Rectangle))