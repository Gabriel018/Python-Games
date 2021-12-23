import pygame
import sys
from pygame.sprite import Sprite
from random import randrange,choice,random,randint

ALTURA = 800
LARGURA = 400

tela = pygame.display.set_mode((ALTURA,LARGURA))
pygame.init()

#Config

carros = list()
for i in range(1,19):
    carros.append(i)

choice_car = choice(carros)

vel_jogo = 3

fundo = pygame.image.load('./img/fundo.png')
fundo = pygame.transform.scale(fundo,(351 * 3,37 * 3))

Sprite_road  = pygame.image.load('img/road1.png') # Estrada
Sprite_road1 =  pygame.image.load('img/player.png') # Player

# Criação de Lista de Carros Disponíveis
npc_sprites = list()
npc_sprites.append(pygame.image.load('img/npc_blue.png'))
npc_sprites.append(pygame.image.load('img/npc_yellow.png'))

"""
Sprite_road2 = pygame.image.load('img/car_blue.png')
Sprite_road3 = pygame.image.load('img/car_yellow.png')
"""
Sprite_Veloc = pygame.image.load('img/velocimetro.png')


def Start(Ready = False):
    if Ready == False:
        font = pygame.font.SysFont('Lobster', 100)
        GAME_OVER_txt = font.render('The Run', False, (139,0,0))
        tela.fill((0,0,0))
        tela.blit(GAME_OVER_txt, (250, 80))

        font1 = pygame.font.SysFont('Lobster', 40)
        GAME_OVER_Enter = font1.render('Press Space to start', False, (139,0,0))
        tela.blit(GAME_OVER_Enter, (250, 160))

        GAME_OVER_Sair = font1.render('Press up arrow to acelerate', False, (139, 0, 0))
        tela.blit(GAME_OVER_Sair, (250, 200))

        GAME_OVER_Sair = font1.render('Press Q to get out', False, (139,0,0))
        tela.blit(GAME_OVER_Sair, (250, 240))

def Mgs_Game(msg,size,color):
    font =  pygame.font.SysFont('Arial',30)
    mensagem = f'Score {msg}'
    txt_format = font.render(mensagem,True,color)
    return  txt_format

def Game_Over():
    if GAME_OVER == True:
        Pontos = 0
        pygame.mixer.music.stop()
        GAME_OVER_sounde.play()
        font = pygame.font.SysFont('Lobster', 90)
        GAME_OVER_txt = font.render('Game Over',False,(255,255,255))
        tela.blit(GAME_OVER_txt,(250,100))

        font = pygame.font.SysFont('Lobster', 50)
        GAME_OVER_txt = font.render('Press R to restart...', False, (255,255,255))
        tela.blit(GAME_OVER_txt, ( 200, 200))


class Road(Sprite):
    def __init__(self):
        Sprite.__init__(self)
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
        if key(key=pygame.K_UP):
           self.image_atual = (self.image_atual + 1) % 4

class Car(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.sprite_list = []
        img = Sprite_road1.subsurface(( 0, 00), (63, 45))
        self.sprite_list.append(img)
        self.image_atual = 0
        self.image = self.sprite_list[self.image_atual]
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 300
        self.image = pygame.transform.scale(self.image,(120,90))

class NPC(Sprite):
    def __init__(self,car=0):
        Sprite.__init__(self)
        self.escolha = car
        self.car = car
        self.largura = 62
        self.altura = 32

        self.margem_e = 120
        self.margem_d = 620

        self.topo = 100
        self.base = 410

        xzero = 360
        yzero = 100

        spt = choice(npc_sprites)
        self.image = spt.subsurface((0, 0), (self.largura, self.altura))
        self.rect = self.image.get_rect()

        self.rect.x = xzero # Esquerda direita
        self.rect.y = yzero # cima baixo


    def update(self):
        if self.escolha == self.car:
            posicao = ( self.rect.y - self.base ) * -1
            self.rect.y += vel_jogo

            if posicao < 161:
                self.largura = 62 * 2
                self.altura = 32 * 2

            elif posicao > 160:
                self.largura = 62
                self.altura = 32

            elif posicao > 260:
                self.largura = 31
                self.altura = 16

            self.image = pygame.transform.scale(
                self.image, (self.largura, self.altura))

            if self.rect.y >= 410 or self.rect.x <= 100:
                self.rect.y = 100
                self.rect.x = randrange(330, 360, 1)

            if self.rect.y >= 200:
                self.rect.x = randrange(330,400,300)
            else:
                self.rect.x = 360


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
        if key(key=pygame.K_UP) and self.image_atual <= 27:
            self.image_atual = (self.image_atual + 1) % 30
            self.image = self.sprites_veloc[int(self.image_atual)]
            self.image = pygame.transform.scale(self.image, (461 / 3, 550 / 3))

        if not key(key=pygame.K_UP):
            self.image_atual = 0
            print(self.image_atual)


def key(key=None):
    tecla = pygame.key.get_pressed()
    return (tecla[key])

def main():
    Ready = False
    Pontos = 0
    global GAME_OVER
    GAME_OVER = False
    Timer = 0

    #Player Group
    Player_group = pygame.sprite.Group()
    car_player = Car()
    Player_group.add(car_player)

    #NPC Group
    NPC_group = pygame.sprite.Group()
    npcs = list()
    npcs.append("")
    for car in carros:
        npc = NPC()  ### car é um numero inteiro pra saber se ele é o cara escolhido.
        npc.car = car
        if car == 1:
            npc.escolha = car
        else:
            npc.escolha = 0
        npcs.append(npc)
        NPC_group.add(npc)

    Veloc_group = pygame.sprite.Group()
    veloc = speedometer()
    Veloc_group.add(veloc)

    Road_group = pygame.sprite.Group()
    road = Road()
    Road_group.add(road)


    FPS = 60
    relogio = pygame.time.Clock()


    #Sounds
    ready_sound = pygame.mixer.Sound('music/ready.wav')
    global GAME_OVER_sounde
    GAME_OVER_sounde = pygame.mixer.Sound('music/GAME_OVER.wav')
    crash_sound = pygame.mixer.Sound('music/crash.wav')
    intro = pygame.mixer.music.load('music/intro.ogg')
    pygame.mixer.music.play(-1)
    motor_car_red = pygame.mixer.Sound('music/motor.wav')
    motor_car_red.set_volume(0.6)

    altera_car = True

    while True:
        relogio.tick(30)
        tela.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == "Exit":
                pygame.quit()
                sys.exit()
        #choice
        if altera_car: # True
            choice_car = choice(carros)
            npc_atual = npcs[choice_car]
            npc_atual.rect.y = 100
            npc_atual.escolha = choice_car
            altera_car = False


        if npc_atual.rect.top >= 400:
            npc_atual.escolha = 0
            altera_car = True

        if npc_atual.escolha == 0:
            NPC_group.remove(npc_atual)

        # collision
        colision = pygame.sprite.spritecollide(car_player, NPC_group, False)

        if colision:
            Pontos = 0
            GAME_OVER = True

        #Controls

        if key(key=pygame.K_UP):
            motor_car_red.play()
            road.moverr()
            car_player.rect.y = 301
            vel_jogo = 4

        if not key(key=pygame.K_UP):
            vel_jogo = 1

        if key(key=pygame.K_LEFT):
            car_player.rect.x -= 5
            if car_player.rect.x <= 120:
                car_player.rect.x = 120

        if key(key=pygame.K_RIGHT):
            car_player.rect.x += 5
            if car_player.rect.x  >= 620:
                car_player.rect.x = 620

        if key(key=pygame.K_r):
            GAME_OVER = False
            altera_car = True

        if key(key=pygame.K_SPACE):
            Ready = True
            ready_sound.play()

        if key(key=pygame.K_q):
            quit()

        Road_group.draw(tela)
        Road_group.update()

        Player_group.draw(tela)
        Player_group.update()

        Veloc_group.draw(tela)
        Veloc_group.update()

        if choice_car == npc_atual.car and not GAME_OVER and Ready:
            NPC_group.draw(tela)
            NPC_group.update()


        Start(Ready=Ready)
        Game_Over()
        Pontos += 1
        #Score
        if Ready == True:
            txt_pontos = Mgs_Game(Pontos, 100, (255, 255, 0))
            tela.blit(txt_pontos, (0, 250))
            txt_pontos = Mgs_Game(Pontos, 100, (255, 255, 0))
            tela.blit(txt_pontos, (0, 250))
            tela.blit(fundo, (0, 0))
        pygame.display.update()

if __name__ == "__main__":
    main()