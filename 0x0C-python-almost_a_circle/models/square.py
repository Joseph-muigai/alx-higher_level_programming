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

s1 = Square(10, 2, 1)
print(s1)
s1_dictionary = s1.to_dictionary()
print(s1_dictionary)
print(type(s1_dictionary))

s2 = Square(1, 1)
print(s2)
s2.update(**s1_dictionary)
print(s2)
print(s1 == s2)