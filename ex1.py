class Point:
    color = 'red'
    circle = 2
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __del__(self):
        print(self.x, self.y)
    def set_coords (self,x,y):
        self.x = x
        self.y = y
    def get_coords(self):
        return (self.x,self.y)
pt = Point(1,3)
print(pt.__dict__)   