import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300)) #flags=pygame.NOFRAME
pygame.display.set_caption("Моя первая игра")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
running = True
while running:

    #screen.fill((114,157,224))



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((114,127,124))
            elif event.key == pygame.K_SPACE:
                screen.fill((114,157,224))
            elif event.key == pygame.K_s:
                screen.fill((214,225,224))
            elif event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
