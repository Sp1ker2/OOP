from accessify import private,protected
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = self.y = 0
        if self.__check_value(x) and self.__check_value(x):

            self.__x = x
            self.__y = y
    @private
    @classmethod
    def __check_value(cls,x):
        return  type(x) in(int, float)

    def set_cord(self, x, y):
        if self.__check_value(x) and self.__check_value(x):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("error")
    def get_cord(self):
        return self.__x, self.__y
point = Point(1,110)
# print(point.get_cord())

point.set_cord(20,10)
print(point.get_cord())
