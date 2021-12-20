import pygame
import sys



tela = pygame.display.set_mode((800,400))

pygame.init()

Game_over = True
Start = False
Timer = 0




Sprite_road  = pygame.image.load('img/road1.png')
Sprite_road1 =  pygame.image.load('img/car01.png')
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

           self.image_atual = (self.image_atual + 0.10) % 4
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


Car_group = pygame.sprite.Group()
car = Car()
Car_group.add(car)

Road_group = pygame.sprite.Group()
road = Road()
Road_group.add(road)

while True:
     tela.fill((0,0,0))
     for event in pygame.event.get():
         if event.type == "Exit":
             pygame.quit()
             sys.exit()

     key = pygame.key.get_pressed()
     if key[pygame.K_UP]:
        car.rect.y = 301
        road.moverr()

     if key[pygame.K_LEFT]:
         car.rect.x -= 1
         if car.rect.x <= 100:
             car.rect.x = 100
     if key[pygame.K_RIGHT]:
         car.rect.x += 1
         if car.rect.x  >= 600:
             car.rect.x = 600


     Road_group.draw(tela)
     Road_group.update()

     Car_group.draw(tela)
     Road_group.update()

     pygame.display.update()
