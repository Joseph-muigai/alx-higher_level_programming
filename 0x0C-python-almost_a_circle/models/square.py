#!/usr/bin/python3
"""
Defines a clsas Square that inherits from rectangle
"""
from rectangle import Rectangle
class Square(Rectangle):
    """
    class square
    """
    def __init__(self,size, x=0, y=0, id=None):
        """
        initalize the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns an objects representation as a string
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
            )
    @property
    def size(self):
        """
        getter function for size
        """
        return self.width
    @size.setter
    def size(self,value):
        """
        setter function for size
        """
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        *args 
        **kwargs
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size,self.x,self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a+=1
        
        elif kwargs and len(kwargs) != 0:
            for k,v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    def to_dictionary(self):
        """
        Returns s dictionary representation of a square
        """
        return{

            "id":self.id,
            "size":self.width,
            "x":self.x,
            "y":self.y
        }



r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]

Rectangle.save_to_file(list_rectangles_input)

list_rectangles_output = Rectangle.load_from_file()

for rect in list_rectangles_input:
    print("[{}] {}".format(id(rect), rect))

print("---")

for rect in list_rectangles_output:
    print("[{}] {}".format(id(rect), rect))

print("---")
print("---")

s1 = Square(5)
s2 = Square(7, 9, 1)
list_squares_input = [s1, s2]

Square.save_to_file(list_squares_input)

list_squares_output = Square.load_from_file()

for square in list_squares_input:
    print("[{}] {}".format(id(square), square))

print("---")

for square in list_squares_output:
    print("[{}] {}".format(id(square), square))
