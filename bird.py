import pygame as pg
from vector import Vector2D

class Bird():

    def __init__(self, x, y) -> None:
        self.pos = Vector2D(x, y)
        self.vel = Vector2D(1, 0)
        self.color = (194, 180, 25)

    def show(self, screen):
        pg.draw.rect(screen, self.color, [self.pos.x, self.pos.y, 25, 25])

    def move(self, screen):
        self.pos.add(self.vel)
        self.vel.y += 0.2
        if self.pos.y >= 500:
            except Exception:
                
        
        self.show(screen)

    
    def jump(self):
        self.vel.y -= 10
    