class Point:
    def __new__(cls,*args,**kwargs):
        print("__new__ "+str(cls))
        return super().__new__(cls)
    def __init__(self,x,y):
        print("__init__ "+str(self))
        self.x = x
        self.y = y
pt = Point(1,3)