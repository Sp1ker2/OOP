class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_coord(self, x, y):
        self.x = x
        self.y = y
    @classmethod
    def set_bounds(cls, left):
        cls.MIN_COORD = left
pt = Point(1,2)
pt.set_bounds(1)

print(pt.__dict__)
# update only in pt if use self but update on cls
print(Point.__dict__)
