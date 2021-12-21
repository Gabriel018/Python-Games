import pygame
import sys
from random import randrange,choice


tela = pygame.display.set_mode((800,400))

pygame.init()
#Config
Game_over = True
Ready = False
Start = False
Timer = 0
choice_car = choice([1,2])


Sprite_road  = pygame.image.load('img/road1.png')
Sprite_road1 =  pygame.image.load('img/car01.png')
Sprite_road2 = pygame.image.load('img/car_blue.png')
Sprite_road3 = pygame.image.load('img/car_yellow.png')
class Road(pygame.sprite.Sprite):

       def __init__(self):
           pygame.sprite.Sprite.__init__(self)
           self.sprites_road = []
           for i in range(4):
            img = Sprite_road.subsurface((i * 350,00),(358,132))
            self.sprites_road.append(img)
            self.image_atual = 0
            self.image = self.sprites_road[self.image_atual]
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0
            self.image = pygame.transform.scale(self.image, (800, 400))
            self.mover = False

       def moverr(self):
           self.mover = True


       def update(self):
         if self.mover == True:
           self.image_atual = (self.image_atual + 1) % 4
           self.image = self.sprites_road[int(self.image_atual)]
           self.image = pygame.transform.scale(self.image, (800, 400))
         if not  key[pygame.K_UP]:
             self.mover = False

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_road = []
        img = Sprite_road1.subsurface(( 0, 00), (63, 45))
        self.sprites_road.append(img)
        self.image_atual = 0
        self.image = self.sprites_road[self.image_atual]
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 300
        self.image = pygame.transform.scale(self.image,(120,90))


class Car_blue(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_road = []
        img = Sprite_road2.subsurface(( 0, 00), (58, 46))
        self.sprites_road.append(img)
        self.image_atual = 0
        self.escolha = choice_car
        self.image = self.sprites_road[self.image_atual]
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 100

    def update(self):
      if self.escolha == 1:
         self.rect.y += randrange(1, 3, 1)
         if self.rect.y >= 410 or self.rect.x <= 100:
            self.escolha = choice_car
            self.rect.y = 100
         if self.rect.y >= 200:
            self.image = pygame.transform.scale(self.image, (58*2, 46*2))
         else:
            self.image = pygame.transform.scale(self.image, (58,46))

    def draw(self):
        self.rect.x = randrange(320, 360, 1)


class Car_yellow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_road = []
        img = Sprite_road3.subsurface(( 0, 00), (64, 36))
        self.sprites_road.append(img)
        self.image_atual = 0
        self.escolha = choice_car
        self.image = self.sprites_road[self.image_atual]
        self.rect = self.image.get_rect()
        self.rect.x = 390
        self.rect.y = 100

    def update(self):
      if self.escolha == 2:
         self.rect.y +=  randrange(1, 4, 1)
         if self.rect.y >= 450 or self.rect.x <= 100:
            self.escolha = choice_car
            self.rect.x = randrange(320, 360, 1)
            self.rect.y = 100
         if self.rect.y >= 290:
           self.rect.x  = 390
           self.image=   pygame.transform.scale(self.image,(40*2,30*2))
         else:
            self.image = pygame.transform.scale(self.image, (58,46))

    def draw(self):
        self.rect.x = randrange(320, 360, 1)


Car_group = pygame.sprite.Group()
car_player = Car()
Car_group.add(car_player)


Car_group01 = pygame.sprite.Group()
car_blue = Car_blue()
Car_group01.add(car_blue)

Car_group02 = pygame.sprite.Group()
car_yellow = Car_yellow()
Car_group02.add(car_yellow)



Road_group = pygame.sprite.Group()
road = Road()
Road_group.add(road)


All_Cars_Group = pygame.sprite.Group()
All_Cars_Group.add(car_yellow,car_blue)



FPS = 60
relogio = pygame.time.Clock()
#Sounds
intro = pygame.mixer.music.load('music/intro.ogg')
pygame.mixer.music.play(-1)
motor_car_red = pygame.mixer.Sound('music/motor.wav')
motor_car_red.set_volume(0.4)

while True:
     relogio.tick(30)
     tela.fill((0,0,0))
     for event in pygame.event.get():
         if event.type == "Exit":
             pygame.quit()
             sys.exit()

     colision = pygame.sprite.spritecollide(car_player,Car_group01,False)


     #collision
     if colision:
         break

     key = pygame.key.get_pressed()
     if key[pygame.K_UP]:
        car_player.rect.y = 301
        motor_car_red.play()
        road.moverr()
     else:
         motor_car_red.stop()
     if key[pygame.K_LEFT]:
         car_player.rect.x -= 5
         if car_player.rect.x <= 100:
             car_player.rect.x = 100
     if key[pygame.K_RIGHT]:
         car_player.rect.x += 5
         if car_player.rect.x  >= 600:
             car_player.rect.x = 600


     Road_group.draw(tela)
     Road_group.update()

     Car_group.draw(tela)
     Car_group.update()

     if choice_car == 1:
      Car_group01.draw(tela)
      Car_group01.update()
     if choice_car == 2:
      Car_group02.draw(tela)
      Car_group02.update()


     pygame.display.update()
