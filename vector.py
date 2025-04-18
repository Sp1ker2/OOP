class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x =  self.y = 0
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y
    @staticmethod
    def norm2(x,y):
        return x*x + y*y

v = Vector(1, 2)
res = v.get_coord()
f = Vector.validate(10)
print(res)
print(Vector.norm2(5,4))
