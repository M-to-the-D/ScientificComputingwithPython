class Rectangle:
    def __init__(self, width,height):
        self.width=width
        self.height=height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self,x):
        self.width=x
    def set_height(self,x):
        self.height=x
    def get_area(self):
        return self.height*self.width
    def get_perimeter(self):
        return (2*self.height)+(2*self.width)
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        s=''
        if self.height==50 or self.width==50:
            return 'Too big for picture.'
        else:
            for i in range(self.height):
                for i in range(self.width):
                    s+='*'
                s+='\n'
            return s

    def get_amount_inside(self,other_shape):
       if not (isinstance(other_shape, Rectangle) or isinstance(other_shape, Square)):
            raise ValueError("Other_shape must be a Rectangle or Square")
       horizontal_fit = self.width // other_shape.width
       vertical_fit = self.height // other_shape.height
       return horizontal_fit * vertical_fit

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

    def __str__(self):
        return f"Square(side={self.width})"
    def set_side(self, x):
        self.height = x
        self.width=x
    def set_width(self, x):
        self.set_side(x)
    def set_heigth(self, x):
        self.set_side(x)

import shape_calculator.py
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
