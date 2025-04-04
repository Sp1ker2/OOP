class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_coord(self, x, y):
        self.x = x
        self.y = y
    def __getattribute__(self, item):
        print("item")
        return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError("can't set attribute")
        return object.__setattr__(self, key, value)
    def __getattr__(self, item):
        print("item "+item)
        # return object.__getattribute__(self, item)
    def __delattr__(self, item):
        print("item "+item)
        object.__delattr__(self, item)
pt = Point(1,2)
# pt.set_bounds(1)

# print(pt.__dict__)
# update only in pt if use self but update on cls
# print(Point.__dict__)
# a = pt.x
# pt.y = 2





print(pt.yy)
del pt.y
print(pt.y)