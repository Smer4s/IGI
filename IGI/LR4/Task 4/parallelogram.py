from shape import Shape
from color import Color
from math import sin

class Parallelogram(Shape):
    figure_name = "Regular Parallelogram"

    def __init__(self, d1:float, d2:float, alpha:float, color='red'):
        self.d1 = d1
        self.d2 = d2
        self.alpha = alpha
        self.color = Color(color)
    
    def calculate_area(self) -> float:
        """This method calculates area of a parallelogram using diagonals"""
        return self.d1 * self.d2 * sin(self.alpha) / 2
    
    def __str__(self):
        return "d1: {}, d2: {}, alpha: {}".format(self.d1,self.d2,self.alpha)