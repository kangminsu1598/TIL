# 파일명 변경 금지
# 아래에 클래스 Point와 Circle을 선언하세요.
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Circle:
    pi = 3.14
    def __init__(self, center, r):
        self.center = center
        self.r = r
    def get_area(self): 
        return (Circle.pi) * ((self.r)**2)

    def get_perimeter(self):
        return 2*self.pi*self.r

    def get_center(self):
        return (self.center.x, self.center.y)

    def print(self):
        print(f'Circle: {(self.center.x, self.center.y)}, r: {self.r}')

    def parameter_apply(self, a, b):
        return (self.r)**2 + a + b




# 아래의 코드는 수정하지마세요. 
p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.parameter_apply(3, 4))
print(type(c1.center))
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()
