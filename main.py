import pygame
import random
from bird import Bird
pygame.init()


WIDTH, HEIGHT = 500, 500
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

flappy = Bird(50, HEIGHT/2)

running = True
while running:
    clock.tick(FPS)
    flappy.move(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flappy.jump()
    
    
    pygame.display.update()
    screen.fill((0,0,0))
pygame.quit()
