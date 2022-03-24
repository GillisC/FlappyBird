from re import X
import numpy as np

class Vector2D():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def add(self, other):
        self.x += other.x
        self.y += other.y


    
