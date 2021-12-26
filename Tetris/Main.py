import pygame,sys,os,random

from pygame.locals import *

level = 1
lines_to_clear = 1

colores = [ (10,10,10),
          (30,30,30),
          (40,40,40),
          (50,50,50),
          (60,60,70),
          (70,70,70),
          (80,80,80),
]

class Jogo():
    #config
    lines_clear = 0
    field  = []
    start_x  = 100
    start_y = 50
    zoom = 20
    figure = None
    state =  "start"
    pontos = 0

    def __init__(self,altura,largura):
        self.field = []
        self.fgure = None
        self.altura = altura
        self.largura = largura

        for i in range(altura):
            new_line = []
            for j in range(largura):
                new_line.append(0)

    def create_picture(self):
       self.figure = Picture(3,0)

    def colision(self):
       colision = False
       for i in range(4):
           for j in range(4):
               if (i * 4) + j in self.figure.get_img():
                   if ( i + self.figure.y)>(self.altura - 1) or \
                           (j + self.figure.x) > (self.largura - 1) or \
                           (j + self.figure.x) < 0 or self.field[i + self.figure.y][j + self.figure.x] > 0:
                            colision = True
       return colision
    def stop_figure(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.get_img():
                 self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_line()
        self.create_picture()
        if self.colision():
            self.state = 'gameover'
    def break_line(self):
        lines = 0
        for i in range(1, self.altura):
            zero = 0
            for j in range(0,self.largura):
                if self.field[i][j] == 0:
                    zero +=1
            if zero == 0:
                lines +=1
                for i1 in range(i,1,-1):
                    for j in range(self.largura):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.pontos += lines * 2
        self.lines_clear += 1
        self.check_level()

    def check_level(self):
       global  level
       global lines_to_clear
       if self.lines_clear >= level:
           level += 1
           lines_to_clear = level
           self.lines_clear = 0
    def go_space(self):
      while not self.colision():
          self.figure += 1
      self.figure -= 1
      self.stop_figure()
    def down(self):
        if self.colision():
            self.figure.y -= 1
            self.stop_figure()

    def sideway(self,dx):
        posicion_x = self.figure.x
        self.figure.x += dx
        if self.colision():
          self.figure.x = posicion_x

    def rotate(self):
       posicion_rotate = self.figure.rotate()
       self.figure.rotate()
       if self.colision():
          self.figure.rotate = posicion_rotate


class Picture:

        """indice  utilizado para formar os objetos
          | 0 | 1 | 2 | 3 |
          | 4 | 5 | 6 | 7 |
          | 8 | 9 | 10 | 11 |
          | 12 | 13 | 14 | 15 |"""

        Figures = [ [[4,5,6,7],[1,5,9,13]],  #Linha
                 [[1,4,5,6],[1,4,5,9],[4,5,6,9],[1,5,6,9]], #Piramide
                 [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 8, 9], [4, 5, 6, 10]], #Left tetromino
                 [[1, 2, 6, 10], [3, 5, 6, 7], [2, 6, 10, 11], [5, 6, 7, 9]], #Right tetromino
                 [[5,6,9,10]], #quadrado
                 [[1, 2, 4, 5], [0, 4, 5, 6], [1, 5, 8, 9], [4, 5, 6, 10]],
                 [[1, 2, 6, 7], [3, 6, 7, 10], [5, 6, 10, 11], [2, 5, 6, 9]],

        ]

        def __init__(self,x,y):
          self.x = x
          self.y = y
          self.type  = random.randint(0,(len(self.Figures) -1))
          self.color = random.randint(0,(len(colores) -1))
          self.rotation = 0

        def get_img(self):
            return self.Figures[self.type][self.rotation]
        def rotate(self):
            self.rotation = (self.rotation + 1) % (len(self.Figures[self.type]))

def main():
  pass


if __name__ == '__main__':
    main()