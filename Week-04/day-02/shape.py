class Shape():
    name ='not set'
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Shape):
    def __init__(self,x,y,width,height):
        super().__init__(x,y)
        self.width = width
        self.height = height

        print('inited')

class Circle(Shape):
    def __init__(self,x,y,width,height):
        super().__init__(x,y)
        self.width = width
        self.height = height

        print('inited')
