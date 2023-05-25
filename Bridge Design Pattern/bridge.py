class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def draw(self):
        if self.shape_type == 'circle':
            self.draw_circle()
        elif self.shape_type == 'square':
            self.draw_square()

    def draw_circle(self):
        raise NotImplementedError("Subclasses must implement draw_circle method")

    def draw_square(self):
        raise NotImplementedError("Subclasses must implement draw_square method")


class DrawingEngine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def draw_circle(self):
        if self.engine_type == 'raster':
            self.draw_circle_raster()
        elif self.engine_type == 'vector':
            self.draw_circle_vector()

    def draw_square(self):
        if self.engine_type == 'raster':
            self.draw_square_raster()
        elif self.engine_type == 'vector':
            self.draw_square_vector()

    def draw_circle_raster(self):
        print("Drawing circle using raster graphics")

    def draw_circle_vector(self):
        print("Drawing circle using vector graphics")

    def draw_square_raster(self):
        print("Drawing square using raster graphics")

    def draw_square_vector(self):
        print("Drawing square using vector graphics")


# Usage
def main():
    shape1 = Shape('circle')
    shape1.draw()

    shape2 = Shape('square')
    shape2.draw()

    engine1 = DrawingEngine('raster')
    engine1.draw_circle()

    engine2 = DrawingEngine('vector')
    engine2.draw_square()


if __name__ == '__main__':
    main()
