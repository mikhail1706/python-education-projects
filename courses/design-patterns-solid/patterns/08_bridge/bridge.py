"""
    Bridge
"""

# circle square
# vector raster
from abc import ABC


class Render(ABC):
    def render_circle(self, radius):
        pass

    # render_square


class VectorRenderer(Render):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Render):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self):
        pass
    
    def resize(self, factor):
        pass
    

class Circle(Shape):
    def __init__(self, renderer, radius):
        super(Circle, self).__init__(renderer)
        self.radius = radius
        
    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()