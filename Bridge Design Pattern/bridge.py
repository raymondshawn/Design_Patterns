from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self):
        raise NotImplementedError("Subclasses must implement draw method")


class Square(Shape):
    def __str__(self):
        return "square"

    def draw(self):
        return "Drawing square"


class Circle(Shape):
    def __str__(self):
        return "circle"

    def draw(self):
        return "Drawing circle"


class DrawingEngine(ABC):

    @abstractmethod
    def draw(self):
        raise NotImplementedError("Subclasses must implement draw method")


class RasterEngine(DrawingEngine):
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        msg = self.shape.draw()
        msg += " using raster engine"
        print(msg)


class VectorEngine(DrawingEngine):
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        msg = self.shape.draw()
        msg += " using vector engine"
        print(msg)


# Usage
def main():
    circle = Circle()

    print(circle.draw())

    square = Square()
    print(square.draw())

    raster_engine = RasterEngine(shape_type=circle)
    raster_engine.draw()

    vector_engine = VectorEngine(shape_type=square)
    vector_engine.draw()


if __name__ == '__main__':
    main()
