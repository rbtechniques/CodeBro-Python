#Property = decorator used to define a method as a property (it can be accessed like an attribute)
#           benefit: add additional logic when read, write , or delete attributes 
#           gives you getter, setter, deleter method

class rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width >0:
            self._width = new_width
        else:
            print("Width must be greater than zero!")

    @height.setter
    def height(self, new_height):
        if new_height >0:
            self._height = new_height
        else:
            print("Height must be greater than zero!")

    def area(self):
        return self.height*self.width

Rectangle = rectangle(10,12)

print(Rectangle.height)
print(Rectangle.width)