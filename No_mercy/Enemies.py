import sys
import pygame
from random import randrange,choice
from pygame import *


height = 800
width = 600
pos_x = 100
pos_y = 380


tela = pygame.display.set_mode((height, width))
#Escolha inimigo
choice_enemy = choice([1,2])
number_bullets = 3
#Sprites
sprites_player = pygame.image.load('img/john/persona001.png')
sprites_enemy = pygame.image.load('img/enemy/monster01.png')
sprites_enemy01 = pygame.image.load('img/enemy/monster02.png')
sprite_enemy02 = pygame.image.load('img/enemy/monster_contra.png')
sprite_enemy03 = pygame.image.load('img/enemy/monster_fly.png')

pontos = 0
veloc_jogo = 4

class Enemy01(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_monster = []
        for i in range(4):
         img = sprites_enemy.subsurface((i * 72, 0), (70,80))
         self.sprites_monster.append(img)
         self.image_atual = 0
         self.escolha = choice_enemy
         self.image = self.sprites_monster[self.image_atual]
         self.rect = self.image.get_rect()
         self.rect.y = pos_y - 10
         self.rect.x = width


    def update(self):

      if self.escolha == 1:
         self.rect.x -= veloc_jogo
         self.image_atual = (self.image_atual + 0.25) % 4
         self.image = self.sprites_monster[int(self.image_atual)]
         self.image = pygame.transform.scale(self.image, (80, 80))
         if self.rect.topright[0] <= 0:
             self.rect.x = randrange(800, 1200, 90)

    def draw(self):
        self.rect.x = randrange(800, 1200, 90)

class Enemy_lagarto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_monster = []
        for i in range(4):
            img = sprites_enemy01.subsurface((i * 48,00),(40,24))
            self.sprite_monster.append(img)
            self.image_atual = 0
            self.escolha = choice_enemy
            self.image = self.sprite_monster[self.image_atual]
            self.rect = self.image.get_rect()
            self.rect.y = pos_y + 20
            self.rect.x = pos_x - 120
            self.image = pygame.transform.scale(self.image, (80, 48))

    def update(self):

      if self.escolha == 2:
          self.rect.x += veloc_jogo
          self.image_atual = (self.image_atual + 0.25) % 4
          self.image = self.sprite_monster[int(self.image_atual)]
          self.image = pygame.transform.scale(self.image, (80, 48))
          self.image = pygame.transform.flip(self.image, True, False)
          if self.rect.topleft[0] >= 800:
            self.rect.x = randrange(-400, -100, 100)

    def draw(self):
        self.rect.x = randrange(-400, -100, 100)



class Monster_contra(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_monster = []
        for i in range(3):
          img = sprite_enemy02.subsurface((i * 50,00),(60,80))
          self.sprite_monster.append(img)
          self.image_atual = 0
          self.escolha = choice_enemy
          self.image = self.sprite_monster[self.image_atual]
          self.rect = self.image.get_rect()
          self.rect.y = pos_y - 30
          self.rect.x =  width

    def update(self):
     if self.escolha == 3:
        self.rect.x -= veloc_jogo
        self.image_atual = (self.image_atual + 0.25) % 3
        self.image = self.sprite_monster[int(self.image_atual)]
        self.image = pygame.transform.scale(self.image, (110, 110))
        if self.rect.topright[0] <= 0:
            self.rect.x = randrange(800, 1200, 90)

    def draw(self):
        self.image = pygame.transform.scale(self.image, (210, 110))
        self.rect.x = randrange(800, 1200, 90)

class Monster_fly(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_monster = []
        for i in range(3):
         img = sprite_enemy03 .subsurface((i * 32, 0), (30,30))
         self.sprite_monster.append(img)
         self.image_atual = 0
         self.escolha = choice_enemy
         self.image = self.sprite_monster[self.image_atual]
         self.rect = self.image.get_rect()
         self.rect.y = pos_y + 20
         self.rect.x = pos_x - 120
         self.image = pygame.transform.flip(self.image, True, False)


    def update(self):
     if self.escolha == 4:
        self.rect.x += veloc_jogo
        self.image_atual = (self.image_atual + 0.25) % 3
        self.image = self.sprite_monster[int(self.image_atual)]
        self.image = pygame.transform.scale(self.image, (70,70))
        self.image = pygame.transform.flip(self.image, True, False)
        if self.rect.topleft[0] >= 800:
           self.rect.x = randrange(-400, -100, 100)

    def draw(self):
        self.rect.x = randrange(-400, -100, 100)