import sys
import pygame
from pygame import *

height = 700
width = 500
pos_x = 100
pos_y = 380

tela = pygame.display.set_mode((height, width))

number_bullets = 3
#Sprites
sprites_player = pygame.image.load('img/john/persona001.png')
sprites_enemy = pygame.image.load('img/enemy/monster01.png')
class Jogo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        music_fundo = pygame.mixer.music.load('music/music-battle.mp3')
        pygame.mixer.music.set_volume(0.4)
        #pygame.mixer.music.play(-1)
        self.pos_x = 100
        self.pos_y = 370
        self.position = 1
        self.direction = False

        self.Sprites = []
        for i  in range(6):
            img = sprites_player.subsurface((i * 32,0),(23,31))
            self.Sprites.append(img)
            self.image_atual = 0
            self.jump_init = 370
            self.image = self.Sprites[self.image_atual]
            self.rect = self.image.get_rect()
            self.rect.topleft = pos_x  ,pos_y  - 30
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.mover = False
            self.jump = False

    def jumper(self):
        self.jump = True

    def move_front(self):
        self.mover = True
        self.rect.x += 10
        self.position = 1
        self.direction = False
        if self.rect.x >= 520:
            self.rect.x = 520
        if not key[pygame.K_RIGHT]:
            self.mover = False

    def mover_back(self):
        self.mover = True
        self.position = -1
        self.direction = True
        self.rect.x -= 10
        if self.rect.x <= 10:
            self.rect.x = 10

    def update(self):
        if self.rect.colliderect(enemy):
            self.kill()

        # Jump
        if self.jump == True:
            self.rect.y -= 30
            if self.rect.y <= 300:
                self.jump = False
        else:
            if self.rect.y < self.jump_init:
                self.rect.y += 10
            else:
                self.rect.y = self.jump_init
        # Animation
        if self.mover == True:
            self.image_atual = (self.image_atual + 0.5) % 6
            self.image = self.Sprites[int(self.image_atual)]
            self.image = pygame.transform.scale(self.image, (80, 80))
        if not key[pygame.K_RIGHT]:
            self.mover = False

    def draw(self):
        if self.direction == True:
            tela.blit(pygame.transform.flip(self.image, self.direction, False), self.rect)
            self.kill()
        if self.direction == False:
            tela.blit(self.image, self.rect)
            self.kill()


class BackGround(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/fundo01.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

    def update(self):
        # move map
        if jogo.rect.x >= 520 and key[pygame.K_RIGHT]:
            self.rect.x -= 10
        if jogo.rect.x >= 10 and key[pygame.K_LEFT]:
            self.rect.x += 10
            # borda
        if self.rect.x >= 0 and jogo.rect.x >= 10:
            self.rect.x = 0

        if self.rect.x <= -1700 and jogo.rect.x >= 520:
            self.rect.x = -1700


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = 1
        self.direction = -1 if jogo.direction else 1  # DIRECTION OF JOGO WHEN BULLET FIRED
        self.number_bullets = 1
        self.bullets = []
        self.image = pygame.image.load('img/bullet.png')
        self.rect = self.image.get_rect()
        # bullet x: add to 53 to jogo position if jogo facing right (jogo.diredction = False) or add 0 to jogo position if jogo facing left
        self.rect.topleft = jogo.rect.x if jogo.direction else jogo.rect.x + 53, jogo.rect.y + 32

    def update(self):
        self.rect.x += self.direction * 15
        # if bullet goes out of right or left side of screen
        if self.rect.x >= 700 or self.rect.x < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_monster = []
        for i in range(4):
         img = sprites_enemy.subsurface((i * 70, 0), (70, 80))
         self.sprites_monster.append(img)
         self.image_atual = 0
         self.image = self.sprites_monster[self.image_atual]
         self.rect = self.image.get_rect()
         self.rect.center = pos_x + 300 ,pos_y  + 30
         self.image = pygame.transform.scale(self.image, (200, 100))

    def update(self):
        self.image_atual = (self.image_atual + 0.5) % 4

        self.image = self.sprites_monster[int(self.image_atual)]
        self.image = pygame.transform.scale(self.image, (80, 80))
        if self.rect.colliderect(bullet):
            enemy_kill.play()




pygame.init()

Player_Groups = pygame.sprite.Group()
jogo = Jogo()
Player_Groups.add(jogo)

Bullet_Group = pygame.sprite.Group()
bullet = Bullet()
Bullet_Group.add(bullet)

Enemy_Group = pygame.sprite.Group()
enemy = Enemy()
Enemy_Group.add(enemy)


Fundo_Group = pygame.sprite.Group()
plano_fund = BackGround()
Fundo_Group.add(plano_fund)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    relogio.get_time()

    enemy_kill = pygame.mixer.Sound('music/enemy_kill.wav')
    jump_sound = pygame.mixer.Sound('music/jump.flac')
    tiro_sound = pygame.mixer.Sound('music/bullet.wav')
    tela.fill((0, 0, 0))




    for event in pygame.event.get():
        if event.type == "Exit":
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:

        if jogo.rect.y != jogo.jump_init:
            pass
        else:
            jogo.jumper()
            jump_sound.play()


    if key[pygame.K_RIGHT]:
        jogo.move_front()

    if key[pygame.K_LEFT]:
        jogo.mover_back()

    if key[pygame.K_q]:
        pygame.quit()

    if key[pygame.K_SPACE]:
        if len(Bullet_Group) < bullet.number_bullets:
            Bullet_Group.add(Bullet())
            tiro_sound.play()

    Fundo_Group.draw(tela)
    Fundo_Group.update()

    Player_Groups.draw(tela)
    Player_Groups.update()

    Enemy_Group.draw(tela)
    Enemy_Group.update()

    Bullet_Group.draw(tela)
    Bullet_Group.update()

    jogo.draw()
    jogo.update()

    pygame.display.update()