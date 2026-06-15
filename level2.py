import pygame
import sys
import classes

pygame.init()

#window settings
pygame.display.set_caption("Lol's adventure")
screen = pygame.display.set_mode((3000, 1050))
screen.fill((0, 0, 0))

#music
wow_audio = pygame.mixer.Sound("wow.mp3")
doyouloveme_audio = pygame.mixer.Sound("doyouloveme.mp3")
miau = pygame.mixer.Sound("miau!.mp3")

#play area
play_area = pygame.image.load('level2.png')
play_area = pygame.transform.scale(play_area, (10800, 1080))
inf_img = pygame.image.load('informative_img.png')
inf_img = pygame.transform.scale(inf_img, (300, 300))
nums = [pygame.image.load('0.png'), pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png'),
        pygame.image.load('4.png'), pygame.image.load('5.png'), pygame.image.load('6.png'),
        pygame.image.load('7.png'), pygame.image.load('8.png'), pygame.image.load('9.png')]

#clock
clock = pygame.time.Clock()

#platforms
platforms = []
points = [(9, 900, 444, 91), (470, 775, 137, 126), (619, 900, 640, 87), (1263, 772, 97, 125), (1367, 634, 126, 131), (1495, 590, 96, 50), (1596, 594, 149, 33),
          (1857, 893, 821, 98), (2692, 752, 118, 147), (2816, 651, 124, 94), (2613, 578, 128, 24), (2370, 451, 154, 35), (2145, 356, 166, 47), (2223, 224, 93, 35),
          (2385, 128, 312, 35), (2960, 197, 114, 454), (3089, 327, 25, 71), (3117, 340, 30, 62), (3150, 351, 24, 55), (3182, 360, 15, 54), (3206, 373, 18, 39),
          (3233, 382, 191, 37), (3427, 393, 89, 32), (3648, 513, 304, 34), (3785, 414, 90, 29), (3889, 313, 129, 30), (4029, 236, 170, 27), (4300, 693, 91, 34),
          (4862, 833, 79, 30), (5084, 902, 129, 32), (5224, 758, 122, 25), (5401, 676, 130, 24), (5586, 761, 136, 33), (6294, 896, 128, 50), (6644, 894, 64, 174),
          (6719, 888, 337, 77), (7068, 886, 363, 66), (7435, 881, 436, 50), (7880, 890, 682, 58), (9106, 875, 143, 192), (9405, 869, 143, 204), (10298, 857, 497, 221)]
for i in range(0, len(points)):
    platforms.append(pygame.Rect(points[i]))

#lifts
lifts = [pygame.transform.scale(pygame.image.load("lift.png"), (200, 75)).get_rect(midbottom=(8175, 888))]
lift_direction = "right"
lift_image = pygame.transform.scale(pygame.image.load("lift.png"), (200, 75))

#holes
hole = [pygame.Rect(4390, 628, 61, 68), pygame.Rect(4754, 920, 86, 84), pygame.Rect(5783, 676, 82, 102), pygame.Rect(6129, 648, 56, 97)]

#chicken
chicks_coords = [(1748, 654, 33, 46), (2853, 545, 40, 60), (2842, 115, 35, 44)]
chicks_surf = []
chicks_rect = []
chicks_num = 0
for i in range(0, len(chicks_coords)):
    surf = pygame.image.load("chicken.png")
    surf = pygame.transform.scale(surf, (50, 50))
    chicks_surf.append(surf)
    surf_rect = surf.get_rect(topleft = (chicks_coords[i][0], chicks_coords[i][1]))
    chicks_rect.append(surf_rect)

#player
player = classes.Player(25,  100, 50, 50, "None", False, False)

#enemies
enemies = [classes.cricket(720, 910, "left", 1173, 583),
           classes.cricket(2040, 894, "right", 2600, 1840),
           classes.cricket(2000, 894, "left", 2600, 1840),
           classes.cricket(3050 + 150, 388, "right", 3450, 3160)]

#characters
postac1 = classes.Character(9270, 216, img = "postac1.png", width=100, height=200)
pizor = classes.Character(6195, 788, "pizor.png", width=100, height=200)
pizor2 = classes.Character(6195, 788, "pizor2.png", width=160, height=200)
pizor_h1_image = classes.pygame.image.load("pizor_h1.png").convert_alpha()
pizor_h1_image = pygame.transform.scale(pizor_h1_image, (100, 200))
pizor_h1_image = pygame.transform.flip(pizor_h1_image, True, False)
pizor_h2_image = pygame.image.load("pizor_h2.png").convert_alpha()
pizor_h2_image = pygame.transform.scale(pizor_h2_image, (100, 200))
pizor_h2_image = pygame.transform.flip(pizor_h2_image, True, False)
catdrug = pygame.image.load("kocimietka.png").convert_alpha()
catdrug = pygame.transform.scale(catdrug, (30, 30))
catdrug_rect = catdrug.get_rect(midbottom=(6180, 680))

#dialogs
dialogs = ["Witaj!", ]
font = pygame.font.Font(None, 40)

#chicken animation
def chicken_animation(frames, chicken):
    if frames % 30 == 0:
        return pygame.transform.flip(chicken, True, False)
    else:
        return chicken

#lift motion
def lift_motion(lift, direction):
    if direction == "left":
        lift.x -= 4
        return lift.x
    elif direction == "right":
        lift.x += 4
        return lift.x

#main game loop
jump_speed = 13
velocity = 4
camera_x = 0
frames = 0
k = 0
pizor_t = 0
pizor_r = 0
jajo_t = 0
jajo_r = 0
start = 0
start_enemy = 0
while True:
    #checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.direction = "left"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.direction = "right"
            elif event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                player.jump = True

            if event.key == pygame.K_e and jajo_r == 0 and player.rect.colliderect(postac1.rect):
                jajo_r += 1
            elif event.key == pygame.K_n and jajo_r == 0 and player.rect.colliderect(postac1.rect):
                jajo_r = -1
            if event.key == pygame.K_q:
                if chicks_num > 0:
                    player.health += 1
                    chicks_num -= 1
                    print(player.health)
                else:
                    print("nie masz kurczaków")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if player.direction == "left":
                    player.direction = "None"
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if player.direction == "right":
                    player.direction = "None"

    #animating these guys
    player.image = player.animation(frames, k)
    for i in range(0, len(chicks_surf)):
        chicks_surf[i] = chicken_animation(frames, chicks_surf[i])
    for enemy in enemies:
        enemy.image = enemy.animation(frames, k)

    # updating coordinates
    if player.jump == True:
        jump_speed -= 0.5
    if player.on_ground == False:
        velocity += 0.5
    player.rect.x = player.move_x()
    player.rect.y = player.move_y(jump_speed, velocity)
    camera_x = player.rect.x - 300

    #checking if on ground
    player.on_ground = False
    for platform in platforms:
        if player.rect.y + player.rect.height > platform.top and player.rect.bottom <= platform.top + 20 and platform.right > player.rect.x and player.rect.x + player.rect.width > platform.left:
            player.on_ground = True
            player.jump = False
            jump_speed = 13
            velocity = 4
            player.rect.bottom = platform.top
            player.y = player.rect.y
        elif player.rect.colliderect(platform) and player.rect.top <= platform.bottom and player.rect.top >= platform.bottom - 10 and platform.right > player.rect.x and player.rect.x + player.rect.width > platform.left:
            player.on_ground = False
            player.jump = False
            jump_speed = 13
            velocity = 4
            player.rect.top += 5
            player.y = player.rect.y

        if player.rect.colliderect(platform) and player.direction == "right" and player.rect.right > platform.left and player.rect.right < platform.left + 10:
            player.direction = "None"
            player.rect.right -= 5
            player.x = player.rect.left
        elif player.rect.colliderect(platform) and player.direction == "left" and player.rect.left < platform.right and player.rect.left > platform.right - 10:
            player.direction = "None"
            player.rect.left += 5
            player.x = player.rect.left

    #enemies movement
    for i in range(0, len(enemies)):
        enemies[i].rect.x = enemies[i].move_x()

    #lift motion
    lifts[0].x = lift_motion(lift = lifts[0], direction = lift_direction)
    if lifts[0].centerx > 9070:
        lift_direction = "left"
    elif lifts[0].centerx < 8570:
        lift_direction = "right"

    # checking collision with objects
    for lift in lifts:
        if player.rect.colliderect(lift):
            player.direction = lift_direction
            player.on_ground = True
    for i in range(0, len(chicks_rect)):
        if player.rect.colliderect(chicks_rect[i]):
            chicks_rect.pop(i)
            chicks_surf.pop(i)
            chicks_num += 1
            break
        else:
            pass


    #interaction with pizor
    if player.rect.colliderect(pizor.rect) and pizor_t == 0:
        print("chcesz jakies kocimietki")
        pizor_t += 1
    if pizor_t > 0 and player.rect.x > 6445 and pizor_r == 2:
        pizor.direction = "left"

    #interaction with jajo
    if player.rect.colliderect(postac1.rect) and jajo_t == 0:
        jajo_t += 1

    #collision with enemies
    for Enemy in enemies:
        if player.rect.colliderect(Enemy) and frames - start > 90:
            start = frames
            pygame.mixer.Sound.play(miau)
            player.health -= 1
            player.hurt_animation()
            print("zdrowie: ", player.health)
            if player.health == 0:
                print("game over")
                pygame.quit()
                sys.exit()

    #collision with holes
    if player.rect.colliderect(hole[0]) and frames - start > 30:
        start = frames
        player.direction = None
        player.jump = True
        player.on_ground = False
        jump_speed = 20
        player.rect.x = hole[1].centerx
        player.rect.y = hole[1].centery
        player.x = player.rect.x
        player.y = player.rect.y
    elif player.rect.colliderect(hole[1]) and frames - start > 30:
        start = frames
        player.direction = None
        player.jump = True
        player.on_ground = False
        jump_speed = 13
        player.rect.x = hole[0].centerx
        player.rect.y = hole[0].centery
        player.x = player.rect.x
        player.y = player.rect.y
    elif player.rect.colliderect(hole[2]) and frames - start > 30:
        start = frames
        player.direction = "right"
        player.jump = True
        player.on_ground = False
        jump_speed = 13
        player.rect.x = hole[3].centerx
        player.rect.y = hole[3].centery
        player.x = player.rect.x
        player.y = player.rect.y
    elif player.rect.colliderect(hole[3]) and frames - start > 30:
        start = frames
        player.direction = "left"
        player.jump = True
        player.on_ground = False
        jump_speed = 13
        player.rect.x = hole[2].centerx
        player.rect.y = hole[2].centery
        player.x = player.rect.x
        player.y = player.rect.y

    if player.y > 1080:
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    #bliting images
    screen.blit(play_area, (-camera_x, 0))
    screen.blit(postac1.image, (postac1.rect.x - camera_x, postac1.rect.y))
    screen.blit(inf_img, (0, 0))
    screen.blit(nums[chicks_num], (150, 150))
    screen.blit(player.image, (0 + 300, player.rect.y))
    for i in range(0 , len(enemies)):
        screen.blit(enemies[i].image, (enemies[i].rect.x - camera_x, enemies[i].rect.y))

    for i in range(0, len(chicks_rect)):
        screen.blit(chicks_surf[i], (chicks_rect[i].x - camera_x, chicks_rect[i].y))

    screen.blit(lift_image, (lifts[0].x - camera_x, lifts[0].y))

    #for platform in platforms:
        #pygame.draw.rect(screen, "red", (platform.x - camera_x, platform.y, platform.width, platform.height))
    #pygame.draw.rect(screen, "red", (hole[0].x - camera_x, hole[0].y, hole[0].width, hole[0].height))
    #pygame.draw.rect(screen, "red", (hole[1].x - camera_x, hole[1].y, hole[1].width, hole[1].height))
    #pygame.draw.rect(screen, "red", (lifts[0].x - camera_x, lifts[0].y, lifts[0].width, lifts[0].height))

    #music robing
    if pizor_r == 2:
        pygame.mixer.Sound.play(doyouloveme_audio)

    pygame.display.update()
    clock.tick(60)

    frames += 1
    if frames % 10 == 0:
        k += 1
