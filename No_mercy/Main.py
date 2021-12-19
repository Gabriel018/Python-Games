import sys
import time

from time import  sleep
import pygame
from random import randrange,choice
from pygame import *
from Enemies import  *

height = 800
width = 560
pos_x = 100
pos_y = 380

tela = pygame.display.set_mode((height, width))
#Escolha inimigo
choice_enemy = choice([1,2,3,4])
number_bullets = 3
#Sprites
sprites_player = pygame.image.load('img/john/persona001.png')
sprites_enemy = pygame.image.load('img/enemy/monster01.png')
sprites_enemy01 = pygame.image.load('img/enemy/monster02.png')

pontos = 0

game_over = False
boss = False
Mgs_Boss = False
game_timer = 0

#Menssenger
def Mgs_Game(msg,size,color):
    font =  pygame.font.SysFont('Arial',40)
    mensagem = f'Pontos {msg}'
    txt_format = font.render(mensagem,True,color)
    return  txt_format

def Boss_msg():
 if  Mgs_Boss == True:
     font = pygame.font.SysFont('Lobster', 80)
     Boss_txt = font.render('The Boss 01', True, (255, 69, 0))
     tela.blit(Boss_txt, (250, 100))

     Boss_txt = font.render('Prepara-te', True, (255, 69, 0))
     tela.blit(Boss_txt, (260, 200))

def Game_over():
 if game_over == True:
    font = pygame.font.SysFont('Lobster', 70)
    Game_over_txt = font.render('Game Over',False,(0,128,128))
    tela.blit(Game_over_txt,(250,100))

    font = pygame.font.SysFont('Lobster', 50)
    Game_over_txt = font.render('Aperte R para reiniciar...', False, (0,128,128))
    tela.blit(Game_over_txt, ( 200, 200))

def restart():

    music_fundo = pygame.mixer.music.load('music/music-battle.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    #choice
    choice_enemy = choice([1, 2, 3, 4])
    enemy.rect.x = randrange(800, 1200, 90)
    enemy_lagarto.rect.x = randrange(-400, -100, 100)
    enemy_contra.rect.x = randrange(800, 1200, 90)
    enemy_fly.rect.x = randrange(-400, -100, 100)
    enemy.escolha = choice_enemy
    enemy_lagarto.escolha = choice_enemy
    enemy_contra.escolha = choice_enemy
    enemy_fly.escolha = choice_enemy



class Jogo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.display.set_caption("No Mercy")
        music_fundo = pygame.mixer.music.load('music/music-battle.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.pos_x = 100
        self.pos_y = 380
        self.position = 1
        self.direction = False

        self.Sprites = []
        for i  in range(6):
            img = sprites_player.subsurface((i * 32,0),(23,31))
            self.Sprites.append(img)
            self.image_atual = 0
            self.jump_init = 380
            self.image = self.Sprites[self.image_atual]
            self.rect = self.image.get_rect()
            self.rect.x = pos_x
            self.rect.y = pos_y  + 20
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
        self.rect.x -= 4
        if self.rect.x <= 10:
            self.rect.x = 10

    def update(self):

        # Jump
        if self.jump == True:
            self.rect.y -= 15
            if self.rect.y <= 270:
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

        if jogo.rect.x >= 5 and key[pygame.K_LEFT]:
            self.rect.x += 10
            # borda
        if self.rect.x >= 0 and jogo.rect.x >= 10:
            self.rect.x = 0

        if self.rect.x <= -5000  and jogo.rect.x >= 520:
            self.rect.x = -5000


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = 1
        self.direction = -1 if jogo.direction else 1  # DIRECTION OF JOGO WHEN BULLET FIRED
        self.bullets = []
        self.number_bullets = 2
        self.image = pygame.image.load('img/bullet.png')
        self.rect = self.image.get_rect()
        # bullet x: add to 53 to jogo position if jogo facing right (jogo.diredction = False) or add 0 to jogo position if jogo facing left
        self.rect.midright = jogo.rect.x if jogo.direction else jogo.rect.x + 53, jogo.rect.y + 40

    def update(self):
       self.rect.x  += 10
       self.rect.x += self.direction * 25
        # if bullet goes out of right or left side of screen
       if self.rect.x >= 800 or self.rect.x < 0:
            self.kill()



class Big_monster(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_monster = []
        for i in range(3):
         img = sprite_monster04.subsurface((i * 413, 0), (400,200))
         self.sprites_monster.append(img)
         self.image_atual = 0
         self.live = 100
         self.escolha = choice_enemy
         self.image = self.sprites_monster[self.image_atual]
         self.rect = self.image.get_rect()
         self.rect.y = pos_y - 90
         self.rect.x = pos_x + 2000

    def update(self):
        if boss == True:
            self.rect.x -= 2
            self.image_atual = (self.image_atual + 0.10) % 3
            self.image = self.sprites_monster[int(self.image_atual)]
            if self.rect.topright[0] <= 0:
                self.rect.x = randrange(width, 2200, 90)


pygame.init()

Player_Groups = pygame.sprite.Group()
jogo = Jogo()
Player_Groups.add(jogo)

Bullet_Group = pygame.sprite.Group()
bullet = Bullet()
Bullet_Group.add(bullet)

Enemy_Group = pygame.sprite.Group()
enemy = Enemy01()
Enemy_Group.add(enemy)


Enemy_Group02 = pygame.sprite.Group()
enemy_contra = Monster_contra()
Enemy_Group02.add(enemy_contra)


Enemy_Group03 = pygame.sprite.Group()
enemy_fly = Monster_fly()
Enemy_Group03.add(enemy_fly)

Enemy_Group01 = pygame.sprite.Group()
enemy_lagarto = Enemy_lagarto()
Enemy_Group01.add(enemy_lagarto)


Enemy_Group04 = pygame.sprite.Group()

big_monster = Big_monster()
Enemy_Group04.add(big_monster)

Fundo_Group = pygame.sprite.Group()
plano_fund = BackGround()
Fundo_Group.add(plano_fund)

Group_All_Enemy = pygame.sprite.Group()
Group_All_Enemy.add(enemy,enemy_contra,enemy_lagarto,enemy_fly)

relogio = pygame.time.Clock()

FPS = 60

while True:
    print(boss)
    print(big_monster.live)
    relogio.tick(30)
    relogio.get_time()
    colission = pygame.sprite.spritecollide(enemy,Bullet_Group,False)
    colission1 = pygame.sprite.spritecollide(enemy_contra,Bullet_Group,False)
    colission2 = pygame.sprite.spritecollide(enemy_lagarto,Bullet_Group,False)
    colission3 = pygame.sprite.spritecollide(enemy_fly,Bullet_Group,False)
    colission_player = pygame.sprite.spritecollide(jogo,Group_All_Enemy,True)

    colission_big = pygame.sprite.spritecollide(big_monster,Bullet_Group,False)

    #Sounds

    alarm_boss = pygame.mixer.Sound('music/alarm.ogg')
    big_monster_sound = pygame.mixer.Sound('music/big_monster.flac')
    enemy_fly_sound = pygame.mixer.Sound('music/enemy_fly.wav')
    enemy_contra_sound = pygame.mixer.Sound('music/enemy_contra.wav')
    enemy_lagarto_sound = pygame.mixer.Sound('music/enemy_lagarto.wav')
    to_die = pygame.mixer.Sound('music/dead.wav')
    enemy_kill = pygame.mixer.Sound('music/enemy_kill.wav')
    enemy_kill.set_volume(0.3)
    jump_sound = pygame.mixer.Sound('music/jump.flac')
    tiro_sound = pygame.mixer.Sound('music/bullet.wav')

    for event in pygame.event.get():
        if event.type == "Exit":
            pygame.quit()
            sys.exit()



    #colision
    if colission:
      pontos += 10
      enemy.draw()
      enemy_lagarto_sound.play()

    if colission1:
       pontos +=10
       enemy_contra.draw()
       enemy_kill.play()

    if colission2:
       pontos +=10
       enemy_lagarto.draw()
       enemy_contra_sound.play()

    if colission3:
        pontos +=10
        enemy_fly.draw()
        enemy_fly_sound.play()

    if colission_player:
          game_over = True
          pontos = 0
          jogo.rect.x = 0
          to_die.play()
          jogo.kill()
          game_over_soundd = pygame.mixer.music.load('music/game_over-sound.mp3')
          pygame.mixer.music.play(-1)


    if colission_big:
        big_monster.rect.x += 2
        big_monster.live -= 0.5
        bullet.kill()
        big_monster_sound.play()


    if big_monster.live <= 10:
        boss = False



    if pontos == 50:
       Mgs_Boss = True
       boss = True
       alarm_boss.play()
       game_timer = pygame.time.get_ticks()


    if game_timer > 13000:
        Mgs_Boss = False
        alarm_boss.stop()

    #choice
    if  colission or colission1 or colission2 or colission3:
        choice_enemy = choice([1,2,3,4])
        enemy.rect.x = randrange(800, 1200, 90)
        enemy_lagarto.rect.x = randrange(-400, -100, 100)
        enemy_contra.rect.x = randrange(800, 1200, 90)
        enemy_fly.rect.x = randrange(-400, -100, 100)
        #new choice
        enemy.escolha = choice_enemy
        enemy_lagarto.escolha = choice_enemy
        enemy_contra.escolha = choice_enemy
        enemy_fly.escolha = choice_enemy


    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:

        if jogo.rect.y != jogo.jump_init:
            pass
        else:
            jogo.jumper()
            jump_sound.play()
    # Restart
    if key[pygame.K_r] and game_over == True:
        game_over = False
        pygame.mixer.music.stop()
        restart()


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
    Enemy_Group04.draw(tela)
    Enemy_Group04.update()

    if  game_over == False and boss == False :
       Group_All_Enemy.draw(tela)
       Group_All_Enemy.update()

    Bullet_Group.draw(tela)
    Bullet_Group.update()


    jogo.draw()
    jogo.update()
    Game_over()
    Boss_msg()


    txt_pontos = Mgs_Game(pontos,100,(255,255,0))
    tela.blit(txt_pontos, (600, 30))
    pygame.display.update()