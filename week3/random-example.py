import pygame
pygame.init()
dis=pygame.display.set_mode ((600,400))
end=False
while not end:
    for event in pygame.event.get():
        if event.type==pygame.Quit:
            end=True

    disfill=("white")
    pygame.draw.circle(dis,"black")