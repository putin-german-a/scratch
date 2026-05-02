import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
pygame.quit()