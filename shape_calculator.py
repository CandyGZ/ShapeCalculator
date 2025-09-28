class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        # return area (width * height)
        area = self.width * self.height
        print(area)
        return area

    def get_perimeter(self):
        # 2 * width + 2 * height
        perimeter = (2 * self.width) + (2 * self.height)
        print(perimeter)
        return perimeter

    def get_diagonal(self):
        # (width ** 2 + height ** 2) ** .5
        diagonal = (self.width**2 + self.height**2) ** 0.5
        print(diagonal)
        return diagonal

    def get_picture(self):
        # Returns a string that represents the shape using lines of "*".
        # The number of lines should be equal to the height and the number of "*" in each line should be equal to the width.
        # There should be a new line (\n) at the end of each line.
        # If the width or height is larger than 50, this should return the string: "Too big for picture.".
        lines = int(self.width)
        grosor = int(self.height)
        if lines > 50 or grosor > 50:
            return "Too big for picture."
        lines = lines * "*"
        picture = ""
        for sign in range(grosor):
            picture += f"{lines}\n"
        print(picture)
        return picture

    def get_amount_inside(self, shape):
        # Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        # For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
        # shape = super().__init__(width, height)
        in_width = 0
        in_height = 0
        if shape.width <= self.width and shape.height <= self.height:
            in_width = self.width // shape.width
            in_height = self.height // shape.height
        tot = in_width * in_height
        print(tot)
        return tot

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# Additionally, if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)

class Square(Rectangle):
    # The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in.
    # The __init__ method should store the side length in both the width and height attributes from the Rectangle class.
    # The Square class should be able to access the Rectangle class methods but should also contain a set_side method.
    # If an instance of a Square is represented as a string, it should look like: Square(side=9)
    # Additionally, the set_width and set_height methods on the Square class should set both the width and height.
    def __init__(self, side) -> None:
        # Rectangle.width = side    <--- Esta forma funciona pero no es muy eficiente, lo mejor es usar el método super para acceder a atributos del padre
        # Rectangle.height = side       si la clase Rectangle  agregara nuevos argumentos tendríamos que reescribir el código en la clase Square
        super().__init__(
            side, side
        )  # llmáma al metodo init de la clase Rectangle y establece side en lugar de width y side en lugar de height

    def set_width(self, side):
        # Rectangle.width = side
        # Rectangle.height = side
        super().__init__(side, side)

    def set_height(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().__init__(side, side)

    def __repr__(self):
        return f"Square(side={self.width})"


# rect = Rectangle(4, 8)
# # rect.get_area()
# # rect.get_perimeter()
# # rect.get_diagonal()
# rect.get_picture()
# sq = Square(2)
# # sq.get_picture()
# # print(rect)
# # print(sq)
# # # rect.set_width(8)
# # print(rect)
# rect2 = Rectangle(3, 7)
# # rect.get_amount_inside(sq)
# rect.get_amount_inside(rect2)

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

