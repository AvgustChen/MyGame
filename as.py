import pygame
from random import randint as ri

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 400))  # flags=pygame.NOFRAME
pygame.display.set_caption("Моя первая игра")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)
bg = pygame.image.load('images/bg.jpg').convert()

player = pygame.image.load('images/1.png').convert_alpha()
walk_left = [
    pygame.image.load('images/move_left/1.png').convert_alpha(),
    pygame.image.load('images/move_left/2.png').convert_alpha(),
    pygame.image.load('images/move_left/3.png').convert_alpha(),
    pygame.image.load('images/move_left/4.png').convert_alpha()
]
walk_right = [
    pygame.image.load('images/move_right/1.png').convert_alpha(),
    pygame.image.load('images/move_right/2.png').convert_alpha(),
    pygame.image.load('images/move_right/3.png').convert_alpha(),
    pygame.image.load('images/move_right/4.png').convert_alpha()
]
vrag = [
    pygame.image.load('images/vrag/1.png').convert_alpha(),
    pygame.image.load('images/vrag/2.png').convert_alpha(),
    pygame.image.load('images/vrag/3.png').convert_alpha(),
    pygame.image.load('images/vrag/4.png').convert_alpha(),
    pygame.image.load('images/vrag/5.png').convert_alpha(),
    pygame.image.load('images/vrag/6.png').convert_alpha(),
    pygame.image.load('images/vrag/7.png').convert_alpha(),
    pygame.image.load('images/vrag/8.png').convert_alpha(),
    pygame.image.load('images/vrag/9.png').convert_alpha(),
    pygame.image.load('images/vrag/10.png').convert_alpha(),
    pygame.image.load('images/vrag/11.png').convert_alpha(),
    pygame.image.load('images/vrag/12.png').convert_alpha(),
    pygame.image.load('images/vrag/13.png').convert_alpha(),
    pygame.image.load('images/vrag/14.png').convert_alpha(),
    pygame.image.load('images/vrag/15.png').convert_alpha(),
    pygame.image.load('images/vrag/16.png').convert_alpha(),
    pygame.image.load('images/vrag/17.png').convert_alpha(),
    pygame.image.load('images/vrag/18.png').convert_alpha()

]
vrag_list = []
player_anim_count = 0
player_vrag_count = 0
bg_x = 0

player_speed = 10
player_x = 100
player_y = 245
player_live = 10

vrag_speed = 4
vistrel = []
labal_lose = pygame.font.Font('font/Old-Soviet.otf', 40)
labal = labal_lose.render('Вы проиграли', False, (193, 196, 199))
labal_life = labal_lose.render('Life {player_live}', False, (193, 196, 199))
is_jump = False
jump_count = 10

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
# bg_sound.play()
vrag_timer = pygame.USEREVENT + 1
new_for_vrag = 1000
pygame.time.set_timer(vrag_timer, new_for_vrag)


running = True
while running:
    keys = pygame.key.get_pressed()

    # screen.blit(labal_life, 10,10)
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 800, 0))
    screen.blit(bg, (bg_x - 800, 0))
    
    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

    if vrag_list:
        for el in vrag_list:
            screen.blit(vrag[player_vrag_count], el)  
            el.x -= 2

            if player_rect.colliderect(el):
                player_live -= 1
                player_x = 100
                vrag_list.pop(0)

    if player_live <= 0:
        screen.blit(labal, (180, 100))
       
    if keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
        bg_x += player_speed-2
        if bg_x == 800:
            bg_x = 0
    elif keys[pygame.K_d]:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
        bg_x -= player_speed-2
        if bg_x == -800:
            bg_x = 0
    else:
        screen.blit(player, (player_x, player_y))

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 2

        else:
            is_jump = False
            jump_count = 10

    if keys[pygame.K_a] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_d] and player_x < 750:
        player_x += player_speed

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    if player_vrag_count == 17:
        player_vrag_count = 0
    else:
        player_vrag_count += 1

    pygame.display.update()

    check = ri(0, 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == vrag_timer:
            if check == 2:
                vrag_list.append(vrag[player_vrag_count].get_rect(topleft=(801, 230)))



    clock.tick(10)
