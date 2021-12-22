import pygame
import sys
from random import randrange,choice,random,randint

altura = 800
largura = 400

tela = pygame.display.set_mode((altura,largura))

pygame.init()
#Config
Pontos = 0
game_over = False
Ready = False

Timer = 0
choice_car = choice([1,2])

vel_jogo = 3

fundo = pygame.image.load('img/fundo.png')
fundo = pygame.transform.scale(fundo,(351 * 3,37 * 3))

Sprite_road  = pygame.image.load('img/road1.png')
Sprite_road1 =  pygame.image.load('img/car01.png')
Sprite_road2 = pygame.image.load('img/car_blue.png')
Sprite_road3 = pygame.image.load('img/car_yellow.png')

Sprite_Veloc = pygame.image.load('img/velocimetro.png')

def Start():
 if Ready == False:
    font = pygame.font.SysFont('Lobster', 100)
    Game_over_txt = font.render('The Run', False, (139,0,0))
    tela.fill((0,0,0))
    tela.blit(Game_over_txt, (250, 80))

    font1 = pygame.font.SysFont('Lobster', 40)
    Game_over_Enter = font1.render('Press Space to start', False, (139,0,0))
    tela.blit(Game_over_Enter, (250, 160))

    Game_over_Sair = font1.render('Press up arrow to acelerate', False, (139, 0, 0))
    tela.blit(Game_over_Sair, (250, 200))

    Game_over_Sair = font1.render('Press Q to get out', False, (139,0,0))
    tela.blit(Game_over_Sair, (250, 240))

def Mgs_Game(msg,size,color):
    font =  pygame.font.SysFont('Arial',30)
    mensagem = f'Score {msg}'
    txt_format = font.render(mensagem,True,color)
    return  txt_format

def Game_over():
 if game_over == True:
    Pontos = 0
    pygame.mixer.music.stop()
    game_over_sounde.play()
    font = pygame.font.SysFont('Lobster', 90)
    Game_over_txt = font.render('Game Over',False,(255,255,255))
    tela.blit(Game_over_txt,(250,110))

    font = pygame.font.SysFont('Lobster', 50)
    Game_over_txt = font.render('Press R to restart...', False, (255,255,255))
    tela.blit(Game_over_txt, ( 250, 200))

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
         #if self.mover == True:
           self.image_atual = (self.image_atual + 0.1) % 4
           self.image = self.sprites_road[int(self.image_atual)]
           self.image = pygame.transform.scale(self.image, (800, 400))
           if   key[pygame.K_UP]:
               self.image_atual = (self.image_atual + 1) % 4

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
         self.rect.y += vel_jogo
         if self.rect.y >= 410 or self.rect.x <= 100:
            self.rect.y = 100
            self.rect.x = randrange(330, 360, 1)
         if self.rect.y >= 200:
            self.rect.x = randrange(330,400,300)
            self.image = pygame.transform.scale(self.image, (48*2, 36*2))
         else:
            self.rect.x = 360


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
         self.rect.y +=  vel_jogo
         if self.rect.y >= 410 or self.rect.x <= 100:
            self.rect.x = randrange(320, 350, 1)
            self.rect.y = 100
         if self.rect.y >= 200:
           self.rect.x  = 420
           self.image=   pygame.transform.scale(self.image,(50*2,40*2))
         else:
             self.image = self.sprites_road[self.image_atual]


class speedometer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_veloc = []
        for i in range(0,30):
         img = Sprite_Veloc.subsurface((i * 440, 00), (461, 550))
         self.sprites_veloc.append(img)
         self.image_atual = 0
         self.image = self.sprites_veloc[self.image_atual]
         self.rect = self.image.get_rect()
         self.rect.x = 0
         self.rect.y = 270
         self.image = pygame.transform.scale(self.image, (461 / 3, 550 / 3))

    def update(self):
     if key[pygame.K_UP] and self.image_atual <= 27:
         self.image_atual = (self.image_atual + 1) % 30
         self.image = self.sprites_veloc[int(self.image_atual)]
         self.image = pygame.transform.scale(self.image, (461 / 3, 550 / 3))
     if not key[pygame.K_UP]:
         self.image_atual = 0
         print(self.image_atual)


#Groups
Car_group = pygame.sprite.Group()
car_player = Car()
Car_group.add(car_player)

Veloc_group = pygame.sprite.Group()
veloc = speedometer()
Veloc_group.add(veloc)


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
ready_sound = pygame.mixer.Sound('music/ready.wav')
game_over_sounde = pygame.mixer.Sound('music/game_over.wav')
crash_sound = pygame.mixer.Sound('music/crash.wav')
intro = pygame.mixer.music.load('music/intro.ogg')
pygame.mixer.music.play(-1)
motor_car_red = pygame.mixer.Sound('music/motor.wav')
motor_car_red.set_volume(0.6)

while True:

     relogio.tick(30)
     tela.fill((0,0,0))
     for event in pygame.event.get():
         if event.type == "Exit":
             pygame.quit()
             sys.exit()

     #choice
     if  car_blue.rect.top >=400  or car_yellow.rect.top >=400 :
         choice_car = choice([1,2])
         car_yellow.rect.y = 100
         car_blue.rect.y = 100
         car_blue.escolha = choice_car
         car_yellow.escolha = choice_car
     # collision
     colision = pygame.sprite.spritecollide(car_player,Car_group01,False)
     colision1 = pygame.sprite.spritecollide(car_player,Car_group02,False)

     if colision or colision1 :
        Pontos = 0
        game_over = True

     #Controls
     key = pygame.key.get_pressed()
     if key[pygame.K_UP]:
         motor_car_red.play()
         road.moverr()
         car_player.rect.y = 301
         vel_jogo = 4
     if not  key[pygame.K_UP]:
         vel_jogo = 1

     if key[pygame.K_LEFT]:
         car_player.rect.x -= 5
         if car_player.rect.x <= 120:
             car_player.rect.x = 120

     if key[pygame.K_RIGHT]:
         car_player.rect.x += 5
         if car_player.rect.x  >= 620:
             car_player.rect.x = 620

     if key[pygame.K_r]:
         game_over = False
         choice_car = choice([1, 2])
         car_yellow.rect.y = 100
         car_blue.rect.y = 100
         car_blue.escolha = choice_car
         car_yellow.escolha = choice_car

     if key[pygame.K_SPACE ]:
        Ready = True
        ready_sound.play()

     if key[pygame.K_q]:
         quit()

     Road_group.draw(tela)
     Road_group.update()

     Car_group.draw(tela)
     Car_group.update()

     Veloc_group.draw(tela)
     Veloc_group.update()

     if choice_car == 1 and game_over == False and Ready == True:
      Car_group01.draw(tela)
      Car_group01.update()


     if choice_car == 2 and game_over == False and Ready == True :
       Car_group02.draw(tela)
       Car_group02.update()


     Start()
     Game_over()
     Pontos += 1
     #Score
     if Ready == True:
         txt_pontos = Mgs_Game(Pontos, 100, (255, 255, 0))
         tela.blit(txt_pontos, (0, 250))
         txt_pontos = Mgs_Game(Pontos, 100, (255, 255, 0))
         tela.blit(txt_pontos, (0, 250))
         tela.blit(fundo, (0, 0))
     pygame.display.update()
