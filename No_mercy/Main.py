
import sys
import pygame
import self
from pygame import *

height = 700
width = 500
pos_x = 100
pos_y = 380

tela = pygame.display.set_mode((height, width))
number_bullets = 3

class Jogo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        music_fundo = pygame.mixer.music.load('music/music-battle.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

        self.pos_x = 100
        self.pos_y = 380
        self.position = 1
        self.direction = False

        self.Sprites = []
        self.Sprites.append(pygame.image.load('img/john/jonh1.png'))
        self.Sprites.append(pygame.image.load('img/john/jonh2.png'))
        self.Sprites.append(pygame.image.load('img/john/jonh3.png'))
        self.Sprites.append(pygame.image.load('img/john/jonh4.png'))
        self.image_atual = 0
        self.image = self.Sprites[self.image_atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos_x, self.pos_y
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.mover = False

    def mover_frente(self):
        self.mover = True
        self.rect.x += 10
        self.position = 1
        self.direction = False
        if self.rect.x >= 520:
            self.rect.x = 520
        if not key[pygame.K_RIGHT]:
            self.mover = False

    def mover_traz(self):
        self.mover = True
        self.position = -1
        self.direction = True
        self.rect.x -= 10
        if self.rect.x <= 10:
            self.rect.x = 10

    def update(self):
        if self.mover == True:
            self.image_atual = (self.image_atual + 1) % 4
            self.image = self.Sprites[self.image_atual]
            self.image = pygame.transform.scale(self.image, (80, 80))
        if not key[pygame.K_RIGHT]:
            self.mover = False

    def draw(self):
        if self.direction == True:
          tela.blit(pygame.transform.flip(self.image,self.direction,False),self.rect)
          self.kill()
        if self.direction == False:
          tela.blit(self.image,self.rect)
          self.kill()


class BackGround(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/fundo01.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

    def update(self):
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
        self.direction = False
        self.number_bullets = 3
        self.bullets = []
        self.image = pygame.image.load('img/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = jogo.rect.x + 52, jogo.rect.y + 32

    def update(self):
      self.rect.x += 10
      if self.rect.x >= 700:
          self.kill()



FPS = 6
pygame.init()

Player_Groups = pygame.sprite.Group()
jogo = Jogo()
Player_Groups.add(jogo)

Bullet_Group = pygame.sprite.Group()
bullet = Bullet()
Bullet_Group.add(bullet)

Fundo_Group = pygame.sprite.Group()
plano_fund = BackGround()
Fundo_Group.add(plano_fund)

relogio = pygame.time.Clock()

while True:


    tiro_sound = pygame.mixer.Sound('music/bullet.wav')
    tela.fill((0, 0, 0))
    relogio.tick(20)

    for event in pygame.event.get():
        if event.type == "Exit":
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        jogo.mover_frente()

    if key[pygame.K_LEFT]:
        jogo.mover_traz()

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

    Bullet_Group.draw(tela)
    Bullet_Group.update()

    jogo.draw()
    jogo.update()


    pygame.display.update()

