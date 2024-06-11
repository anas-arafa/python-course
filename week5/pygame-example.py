import pygame

pygame.init()
blue=(0,0,200)
bord = pygame.display.set_mode((600, 400))
while True:
    pygame.draw.circle(bord,blue,[300,200],100,3)
    pygame.display.update()
    print("anas")
bord.fill(255,255,255)
pygame.quit()
quit()
