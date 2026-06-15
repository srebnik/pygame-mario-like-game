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
play_area = pygame.image.load('level14.png')
play_area = pygame.transform.scale(play_area, (10800, 1080))
inf_img = pygame.image.load('informative_img.png')
inf_img = pygame.transform.scale(inf_img, (300, 300))
nums = [pygame.image.load('0.png'), pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png'),
        pygame.image.load('4.png'), pygame.image.load('5.png'), pygame.image.load('6.png'),
        pygame.image.load('7.png'), pygame.image.load('8.png'), pygame.image.load('9.png')]

#clock
clock = pygame.time.Clock()

#platforms
platforms = [pygame.Rect(0, 750, 710, 50), pygame.Rect(830, 750, 1015-830, 50),
             pygame.Rect(1013, 625, 50, 750-625), pygame.Rect(1015, 625, 206, 50), pygame.Rect(1293, 625, 41, 50),
             pygame.Rect(1334, 660, 42, 50), pygame.Rect(1376, 700, 213,50),
             pygame.Rect(1708, 685, 1790-1708, 100), pygame.Rect(1790, 740, 2060-1790, 50),
             pygame.Rect(2065, 530, 2262-2065, 50), pygame.Rect(2252, 530, 10, 2262-530),
             pygame.Rect(2262, 921, 2434-2262,50), pygame.Rect(2600, 895, 300, 100),
             pygame.Rect(3081, 950, 319, 120), pygame.Rect(3400, 1070, 384, 50),
             pygame.Rect(3784, 1035, 3824-3784, 60), pygame.Rect(3824, 996, 3930-3824, 60), pygame.Rect(3923, 791, 50, 996-791),
             pygame.Rect(3927, 791, 4060-3927, 60), pygame.Rect(4060, 791, 8, 954-791), pygame.Rect(4060, 954, 4109-4060, 50),
             pygame.Rect(4109, 994, 4150-4109, 50), pygame.Rect(4150, 1036, 4387-4150, 50), pygame.Rect(4475, 996, 4724-4475, 50),
             pygame.Rect(4725, 805, 5044-4725, 200), pygame.Rect(5140, 845, 5176-5140, 50), pygame.Rect(5272, 910, 5967-5272, 50),
             pygame.Rect(5967, 797, 6314-5967, 50), pygame.Rect(5967, 797, 50, 100)]
#w tym momenaaaacie dopiero uznałem, że mam dość ręcznego przepisywania współrzędnych z obrazka
points = [(6724, 588, 259, 93), (7102, 495, 266, 97), (6584, 831, 1523, 65), (8316, 858, 101, 68), (8595, 873, 97, 69), (8880, 871, 103, 63), (8020, 233, 104, 401), (6328, 693, 252, 111),
          (3485, 755, 328, 74), (3486, 845, 292, 33), (3553, 884, 185, 29), (3507, 891, 23, 20), (3515, 923, 19, 8), (3541, 936, 20, 10), (3556, 950, 141, 18), (3692, 890, 47, 34), (4195, 676, 380, 151),
          (4238, 824, 339, 45), (9189, 816, 1602, 149), (8038, 212, 1335, 60), (2065, 580, 15, 199), (9088, 212, 441, 81), (9454, 38, 110, 221)]
for i in range(0, len(points)):
    platforms.append(pygame.Rect(points[i]))

#ladders
ladders = [pygame.Rect(2037, 540, 2065-2037, 740-540), pygame.Rect(3914, 792, 13, 995-727), pygame.Rect(4697, 805, 27, 996-805), pygame.Rect((7979, 226, 53, 427))]

#flames
flames = [pygame.Rect(6758, 732, 209, 135), pygame.Rect(7146, 647, 204, 187)]

#chicken
chicks_coords = [(1458, 543, 39, 31), (1736, 634, 36, 40), (2132, 368, 53, 34), (2693, 778, 44, 38),
                 (3604, 1024, 34, 37), (3533, 698, 38, 29), (4381, 514, 86, 52), (5143, 777, 42, 52),
                 (6437, 497, 52, 56), (7567, 370, 63, 56)]
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
player = classes.Player(25, 100, 50, 50, "None", False, False)

#enemies
enemies = [classes.enemy(1800, 750, "left", 2020, 1800),
           classes.enemy(2600, 895, "right", 2750, 2600),
           classes.enemy(3300, 950, "left", 3300, 3100),
           classes.enemy(3537, 755, "right", 3780, 3495),
           classes.enemy(4273, 677, "right", 4546, 4195),
           classes.enemy(6787, 573, "right", 6950, 6724)]

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
dialog1 = "mmm... chcesz jakieś kociemiętki przyjacielu?"
dialog2 = "Witaj! Chciałbyś może pomóc wydostać mi się z tej gry?"
dialog3 = "Spotkajmy się w następnym levelu, to wszystko ci opowiem"
dialog4 = "Zawiodłem sie"
font = pygame.font.Font(None, 40)

#chicken animation
def chicken_animation(frames, chicken):
    if frames % 30 == 0:
        return pygame.transform.flip(chicken, True, False)
    else:
        return chicken

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
music = pygame.mixer.Sound(wow_audio)
#music.play()
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
            if event.key == pygame.K_e and pizor_r == 0 and player.rect.colliderect(pizor.rect):
                pizor.image = pizor2.image
                pizor_r += 1
            elif event.key == pygame.K_e and pizor_r == 1 and player.rect.colliderect(pizor.rect):
                pizor_r += 1
                music.stop()
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
    if pizor.direction == "left":
        pizor.rect.x = pizor.move_x()
        pizor.image = pizor.animation(frames=frames, k=k, img1=pizor_h1_image, img2=pizor_h2_image)
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

    # checking collision with objects
    for ladder in ladders:
        if player.rect.colliderect(ladder):
            player.rect.y -= 3
            player.y = player.rect.y
            player.on_ground = True
    for i in range(0, len(chicks_rect)):
        if player.rect.colliderect(chicks_rect[i]):
            chicks_rect.pop(i)
            chicks_surf.pop(i)
            chicks_num += 1
            break
        else:
            pass

    text_surface1 = font.render(dialog1, True, "black")
    text_surface2 = font.render(dialog2, True, "black")
    text_surface3 = font.render("E: Tak/N: Nie", True, "black")
    text_surface4 = font.render(dialog3, True, "black")
    text_surface5 = font.render(dialog4, True, "black")
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

    #collision with flames
    for flame in flames:
        if player.rect.colliderect(flame) and frames - start_enemy > 90:
            start_enemy = frames
            pygame.mixer.Sound.play(miau)
            player.health -= 1
            print("zdrowie: ", player.health)
            if player.health == 0:
                print("game over")
                pygame.quit()
                sys.exit()

    if player.y > 1080:
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    #bliting images
    screen.blit(play_area, (-camera_x, 0))
    screen.blit(pizor.image, (pizor.rect.x - camera_x, pizor.rect.y))
    if pizor_r == 1 and pizor.direction == None:
        screen.blit(catdrug, (catdrug_rect.x - camera_x, catdrug_rect.y))
        screen.blit(catdrug, (catdrug_rect.x - camera_x + 95, catdrug_rect.y))
    screen.blit(postac1.image, (postac1.rect.x - camera_x, postac1.rect.y))
    screen.blit(inf_img, (0, 0))
    screen.blit(nums[chicks_num], (150, 150))
    screen.blit(player.image, (0 + 300, player.rect.y))
    if pizor_t == 1 and pizor_r < 2: screen.blit(text_surface1, (pizor.rect.x - camera_x, pizor.rect.y - 100))
    if jajo_t == 1 and jajo_r == 0:
        screen.blit(text_surface2, (postac1.rect.x - camera_x + 100, postac1.rect.y))
        screen.blit(text_surface3, (player.rect.x - camera_x, player.rect.y))
    if jajo_r == 1: screen.blit(text_surface4, (postac1.rect.x - camera_x + 100, postac1.rect.y))
    elif jajo_r == -1: screen.blit(text_surface5, (postac1.rect.x - camera_x + 100, postac1.rect.y))
    for i in range(0 , len(enemies)):
        screen.blit(enemies[i].image, (enemies[i].rect.x - camera_x, enemies[i].rect.y))

    for i in range(0, len(chicks_rect)):
        screen.blit(chicks_surf[i], (chicks_rect[i].x - camera_x, chicks_rect[i].y))

    #for platform in platforms:
        #pygame.draw.rect(screen, "red", (platform.x - camera_x, platform.y, platform.width, platform.height))

    #music robing
    if pizor_r == 2 and start == 0:
        start = frames
        pygame.mixer.Sound.play(doyouloveme_audio)

    pygame.display.update()
    clock.tick(60)

    frames += 1
    if frames % 10 == 0:
        k += 1


