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
