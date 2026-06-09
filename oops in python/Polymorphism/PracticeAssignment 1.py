# Base Class: Shape
class Shape:
    def __init__(self, shape_id, color):
        self._shape_id = shape_id   # Protected attribute
        self._color = color

    # Virtual method for drawing
    def draw(self):
        print(f"Drawing a generic shape with ID {self._shape_id} and color {self._color}")

    # Virtual method for displaying details
    def display_details(self):
        print(f"Shape ID: {self._shape_id}")
        print(f"Color: {self._color}")


# Derived Class: Circle
class Circle(Shape):
    def __init__(self, shape_id, color, radius):
        super().__init__(shape_id, color)
        self._radius = radius

    def draw(self):
        print(f"Drawing a Circle with radius {self._radius} and color {self._color}")

    def display_details(self):
        super().display_details()
        print(f"Radius: {self._radius}")
        print("--------------------------")


# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, shape_id, color, width, height):
        super().__init__(shape_id, color)
        self._width = width
        self._height = height

    def draw(self):
        print(f"Drawing a Rectangle with width {self._width}, height {self._height}, color {self._color}")

    def display_details(self):
        super().display_details()
        print(f"Width: {self._width}")
        print(f"Height: {self._height}")
        print("--------------------------")


# Demonstration of Polymorphism
if __name__ == "__main__":
    # Create a collection of Shape references
    shapes = [
        Circle(1, "Red", 10.5),
        Rectangle(2, "Blue", 15, 20),
        Circle(3, "Green", 7)
    ]

    # Draw all shapes using polymorphism
    print("=== Drawing Shapes ===")
    for shape in shapes:
        shape.draw()

    # Display details of all shapes
    print("\n=== Shape Details ===")
    for shape in shapes:
        shape.display_details()
