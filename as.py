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
vistrel = [
    pygame.image.load('fire/1.png').convert_alpha(),
    pygame.image.load('fire/2.png').convert_alpha(),
    pygame.image.load('fire/3.png').convert_alpha(),
    pygame.image.load('fire/4.png').convert_alpha(),
    pygame.image.load('fire/5.png').convert_alpha(),
    pygame.image.load('fire/6.png').convert_alpha(),
    pygame.image.load('fire/7.png').convert_alpha(),
    pygame.image.load('fire/8.png').convert_alpha()
    ]
player_anim_count = 0
player_vrag_count = 0
vistrel_anim_count = 0
heart_count = 0
heart_x = 10
heart_y = 10
bg_x = 0

player_speed = 10
player_x = 100
player_y = 245
player_live = 10
zombi_rect_x = 801
vistrel_x = player
vrag_speed = 4
zombi_count = 0

labal_lose = pygame.font.Font('font/Old-Soviet.otf', 40)
labal = labal_lose.render('Вы проиграли', False, (193, 196, 199))
labal2 = labal_lose.render('Убито', False, (193, 196, 199))
heart = [
    pygame.image.load('images/heart/2.png').convert_alpha(),
    pygame.image.load('images/heart/2.png').convert_alpha(),
    pygame.image.load('images/heart/2.png').convert_alpha(),
    pygame.image.load('images/heart/2.png').convert_alpha(),
    pygame.image.load('images/heart/2.png').convert_alpha(),
    pygame.image.load('images/heart/5.png').convert_alpha(),
    pygame.image.load('images/heart/6.png').convert_alpha(),
    pygame.image.load('images/heart/5.png').convert_alpha(),
    pygame.image.load('images/heart/6.png').convert_alpha()
]
is_jump = False
jump_count = 10

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
bg_sound.play()
vrag_timer = pygame.USEREVENT + 1
new_for_vrag = 1000
pygame.time.set_timer(vrag_timer, new_for_vrag)

vistrel_fire = []
running = True
while running:
    labal_life = labal_lose.render(str(player_live), False, (193, 196, 199))
    zombi_count_print = labal_lose.render(str(zombi_count), False, (193, 196, 199))
    keys = pygame.key.get_pressed()

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 800, 0))
    screen.blit(bg, (bg_x - 800, 0))
    screen.blit(labal_life, (80, 10))
    screen.blit(heart[heart_count], (10, 10))
    screen.blit(labal2, (500, 10))
    screen.blit(zombi_count_print, (650, 10))

    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

     
    if vrag_list:
        for zombi in vrag_list:
            screen.blit(vrag[player_vrag_count], zombi)  
            zombi.x -= vrag_speed
            

            if player_rect.colliderect(zombi):
                player_live -= 1
                player_x = 100
                vrag_list.pop(0)
            

    if player_live <= 0:
        screen.blit(labal, (180, 100))

    if keys[pygame.K_e]:
         vistrel_fire.append(vistrel[vistrel_anim_count].get_rect(topleft=(player_x + 30, player_y)))
    
    if vistrel_fire:
        for fire in vistrel_fire:
            screen.blit(vistrel[vistrel_anim_count], (fire.x, fire.y))
            fire.x +=30

        if vistrel_fire:
            if vrag_list:
                if fire.colliderect(zombi):
                    zombi_count += 1
                    vrag_speed += 2
                    vistrel_fire.pop(0)
                    vrag_list.pop(0)
        if fire.x > 800:
            vistrel_fire.pop(0)
        
       
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
    
    elif heart_count == 8:
        heart_count = 0
    else:
        heart_count += 1 

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    if player_vrag_count == 17:
        player_vrag_count = 0
    else:
        player_vrag_count += 1

    if vistrel_anim_count == 7:
        vistrel_anim_count = 0
    else:
        vistrel_anim_count += 1
    
    pygame.display.update()

    check = ri(0, 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == vrag_timer:
            if check == 2:
                vrag_list.append(vrag[player_vrag_count].get_rect(topleft=(zombi_rect_x, 230)))
                zombi_rect_x -= 5



    clock.tick(10)
