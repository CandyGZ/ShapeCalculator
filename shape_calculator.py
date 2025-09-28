class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
       
        return self.width * self.height

    def get_perimeter(self):
        # 2 * width + 2 * height
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        # (width ** 2 + height ** 2) ** .5
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        # Returns a string that represents the shape using lines of "*".
        # The number of lines should be equal to the height and the number of "*" in each line should be equal to the width.
        # There should be a new line (\n) at the end of each line.
        # If the width or height is larger than 50, this should return the string: "Too big for picture.".
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        line = "*" * self.width + "\n"
        return line * self.height

    def get_amount_inside(self, shape):
        # Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        # For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        in_width = self.width // shape.width
        in_height = self.height // shape.height
        return in_width * in_height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    # The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in.
    # The __init__ method should store the side length in both the width and height attributes from the Rectangle class.
    # The Square class should be able to access the Rectangle class methods but should also contain a set_side method.
    # If an instance of a Square is represented as a string, it should look like: Square(side=9)
    # Additionally, the set_width and set_height methods on the Square class should set both the width and height.
    def __init__(self, side) -> None:
        super().__init__(
            side, side
        )  # llmáma al metodo init de la clase Rectangle y establece side en lugar de width y side en lugar de height

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.width})"

# Usage example:
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
