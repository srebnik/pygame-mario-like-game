import pygame

pygame.init()

#player class
class Player:
    def __init__(self, x, y, width, height, direction, on_ground, jump):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = direction
        self.on_ground = on_ground
        self.jump = jump
        self.image_r = pygame.image.load('lolek2.png').convert_alpha()
        self.image_r = pygame.transform.scale(self.image_r, (60, 60))
        self.image = pygame.transform.scale(self.image_r, (60, 60))
        self.image_r2 = pygame.image.load('lolek4.png').convert_alpha()
        self.image_r2 = pygame.transform.scale(self.image_r2, (60, 60))
        self.image2 = pygame.transform.scale(self.image_r2, (60, 60))
        self.scared_image = pygame.image.load('scared_lol.png')
        self.scared_image = pygame.transform.scale(self.scared_image, (60, 60))
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.health = 3

    def move_x(self):
        velocity = 4
        if self.direction == "right":
            self.x += velocity
            return self.x
        elif self.direction == "left":
            self.x -= velocity
            return self.x
        else:
            return self.x

    def move_y(self, jump_speed, velocity):
        if self.on_ground == False and self.jump == False:
            self.y += velocity
            return self.y + velocity
        elif self.on_ground == True and self.jump == False:
            return self.y
        if self.jump == True:
            self.y -= jump_speed
            return self.y

    def animation(self, frames, k):
        if self.direction == "right" and frames % 2 == 0:
            if k % 2 == 0:
                self.image = self.image_r
                return self.image
            else:
                self.image = self.image_r2
                return self.image
        elif self.direction == "left" and frames % 2 == 0:
            if k % 2 == 0:
                self.image = pygame.transform.flip(self.image_r, True, False)
                return self.image
            else:
                self.image = pygame.transform.flip(self.image_r2, True, False)
                return self.image
        else:
            return self.image

    def hurt_animation(self):
        self.image = self.scared_image

#enemy class
class enemy:
    def __init__(self, x, y, direction, x_end_right, x_end_left):
        self.x = x
        self.y = y
        self.x_end_right = x_end_right
        self.x_end_left = x_end_left
        self.d = direction
        image1 = pygame.image.load("dog1.png").convert_alpha()
        self.image1 = pygame.transform.scale(image1, (75, 75))
        image2 = pygame.image.load("dog2.png").convert_alpha()
        self.image2 = pygame.transform.scale(image2, (75, 75))
        self.image = self.image1
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def move_x(self):
        velocity = 3
        if self.x >= self.x_end_right:
            self.d = "left"
        elif self.x <= self.x_end_left:
            self.d = "right"

        if self.d == "left":
            self.x -= velocity
            return self.x
        elif self.d == "right":
            self.x += velocity
            return self.x
        else:
            return self.x

    def animation(self, frames, k):
        if self.d == "right" and frames % 2 == 0:
            if k % 2 == 0:
                self.image = self.image2
                return self.image
            else:
                self.image = self.image1
                return self.image
        elif self.d == "left" and frames % 2 == 0:
            if k % 2 == 0:
                self.image = pygame.transform.flip(self.image2, True, False)
                return self.image
            else:
                self.image = pygame.transform.flip(self.image1, True, False)
                return self.image
        else:
            return self.image

#cricket class
class cricket(enemy):
    def __init__(self, x, y, direction, x_end_right, z_end_left):
        super().__init__(x, y, direction, x_end_right, z_end_left)
        self.image1 = pygame.transform.scale(pygame.image.load("cricket.png").convert_alpha(), (100, 100))
        self.image2 = pygame.transform.scale(pygame.image.load("cricket2.png").convert_alpha(), (100, 100))

    def animation(self, frames, k):
        if self.d == "right" and frames % 2 == 0:
            if k % 2 == 0:
                self.image = pygame.transform.flip(self.image1, True, False)
                return self.image
            else:
                self.image = pygame.transform.flip(self.image2, True, False)
                return self.image
        elif self.d == "left" and frames % 2 == 0:
            if k % 2 == 0:
                self.image = self.image1
                return self.image
            else:
                self.image = self.image2
                return self.image
        else:
            return self.image

#characters class
class Character:
    def __init__(self, x, y, img, width, height):
        self.x = x
        self.y = y
        image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
        self.animation_active = None
        self.direction = None

    def move_x(self):
        velocity = 3
        if self.direction == "left":
            self.rect.x -= velocity
            self.x = self.rect.x
            return self.rect.x
        elif self.direction == "right":
            self.rect.x += velocity
            self.x = self.rect.x
            return self.rect.x
        else:
            return self.rect.x

    def animation(self, frames, k, img1, img2):
        if frames % 10 == 0:
            if k % 2 == 0:
                self.image = img1
                return self.image
            else:
                self.image = img2
                return self.image
        else:
            return self.image

#pizor's class
class Pizor(Character):
    def __init__(self, x, y, img, width, height):
        super().__init__(x, y, img, width, height)
        pizor_img1 = pygame.image.load("pizorl2_1.png").convert_alpha()
        self.pizor_img1 = pygame.transform.scale(pizor_img1, (60, 60))
        self.pizor_img1_flipped = pygame.transform.flip(self.pizor_img1, True, False)
        pizor_img2 = pygame.image.load("pizorl2_2.png").convert_alpha()
        self.pizor_img2 = pygame.transform.scale(pizor_img2, (60, 60))
        self.pizor_img2_flipped = pygame.transform.flip(self.pizor_img2, True, False)
        pizor_imgs = pygame.image.load("pizorl2_s.png").convert_alpha()
        self.pizor_imgs = pygame.transform.scale(pizor_imgs, (60, 60))
        self.pizor_imgs_flipped = pygame.transform.flip(self.pizor_imgs, True, False)
        self.pizor_img = self.pizor_img1
        self.rect = self.pizor_img.get_rect(midbottom = (self.x, self.y))
        self.animation_active = None
        self.direction = None

    def animation(self, frames, k):
        if self.direction == "left":
            if frames % 10 == 0:
                if k % 4 == 0:
                    return self.pizor_img1
                elif k % 4 == 1:
                    return self.pizor_imgs
                elif k % 4 == 2:
                    return self.pizor_img2
                else:
                    return self.pizor_imgs
            else:
                return self.pizor_img
        elif self.direction == "right":
            if frames % 10 == 0:
                if k % 4 == 0:
                    return self.pizor_img1_flipped
                elif k % 4 == 1:
                    return self.pizor_imgs_flipped
                elif k % 4 == 2:
                    return self.pizor_img2_flipped
                else:
                    return self.pizor_imgs_flipped
            else:
                return self.pizor_img
        else:
            return self.pizor_img
