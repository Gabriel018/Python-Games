import pygame,sys,os,random

from pygame.locals import *

level = 1
lines_to_clear = 1
GREY = (128, 128, 128)
colors = [ (10,10,10),
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
    Altura = 0
    Largura = 0
    figure = None
    state =  "start"
    pontos = 0

    def __init__(self,altura,largura):
        self.field = []
        self.figure = None
        self.altura = altura
        self.largura = largura

        for i in range(altura):
            new_line = []
            for j in range(largura):
                new_line.append(0)
            self.field.append(new_line)

    def create_picture(self):
       self.figure = Picture(3,0)

    def colision(self):
       colision = False
       for i in range(4):
           for j in range(4):
               if (i * 4) + j in self.figure.get_img():  # making sure tiles containing figure are not 0
                   if (i + self.figure.y) > (self.altura - 1) or \
                           (j + self.figure.x) > (self.largura - 1) or \
                           (j + self.figure.x) < 0 or \
                           self.field[i + self.figure.y][j + self.figure.x] > 0:
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
                    zero += 1
            if zero == 0:
                lines += 1
                for i1 in range(i,1,-1):
                    for j in range(self.largura):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.pontos += lines * 2
        self.lines_clear += lines
        self.check_level()

    def check_level(self):
       global  level
       global lines_to_clear
       if self.lines_clear >= level:
           level += 1
           lines_to_clear = level
           self.lines_clear = 0
           return True
       else:
         lines_to_clear = level - self.lines_clear
         return False

    def go_space(self):
      while not self.colision():
          self.figure.y += 1
      self.figure.y -= 1
      self.stop_figure()

    def down(self):
        self.figure.y += 1
        if self.colision():
            self.figure.y -= 1
            self.colision()
            self.stop_figure()

    def sideway(self,dx):
        posicion_x = self.figure.x
        self.figure.x += dx
        if self.colision():
          self.figure.x = posicion_x

    def rotate(self):
       posicion_rotate = self.figure.rotate
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
          self.color = random.randint(0,(len(colors) -1))
          self.rotation = 0

        def get_img(self):
            return self.Figures[self.type][self.rotation]

        # increments to the next rotation of any type of figure
        def rotate(self):
            self.rotation = (self.rotation + 1) % (len(self.Figures[self.type]))
def main():
  global  level
  global lines_to_clear
  altura = 400
  largura = 500
  game_altura = 20
  game_largura = 10
  press_down = False
  gameover = False
  counter = 0
  fps = 30


  pygame.init()
  janela = pygame.display.set_mode((altura,largura))
  relogio = pygame.time.Clock()
  game = Jogo(game_altura,game_largura)

  while not gameover:
      if game.figure is None:
          game.create_picture()
      counter += 1
      if counter > 100000:
          counter = 0

      if counter % (fps // level // 2) == 0 or press_down:
          if game.state == "start":
              game.down()

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              gameover = True
              pygame.quit()
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RIGHT:
                  game.sideway(1)
              if event.key == pygame.K_LEFT:
                  game.sideway(-1)
              if event.key == pygame.K_UP:
                  game.rotate()
              if event.key == pygame.K_DOWN:
                  press_down = True
              if event.key == pygame.K_SPACE:
                  game.go_space()
              if event.key == pygame.K_ESCAPE:
                  pygame.quit()
                  sys.exit(0)

      if event.type == pygame.KEYUP:  # event is saved in memory so we can access event outside the for loop
            if event.key == pygame.K_DOWN:
                    press_down = False

      janela.fill((255,255,255))

      # this is used to draw grey grid on window
      for i in range(game.altura):
            for j in range(game.largura):
                  pygame.draw.rect(janela,GREY,[game.start_x + game.zoom * j, game.start_y + game.zoom * i, game.zoom, game.zoom],
                                   1)  # last arg is for line thickness
                  if game.field[i][j] > 0:
                      pygame.draw.rect(janela, colors[game.field[i][j]],
                            [game.start_x + game.zoom * j, game.start_y + game.zoom * i, game.zoom - 2,
                                game.zoom - 1])

          # this is used to draw current figure on a 4x4 matrix in game grid
      if game.figure is not None:
              for i in range(4):
                  for j in range(4):
                      p = i * 4 + j
                      if p in game.figure.get_img():
                          pygame.draw.rect(janela, colors[game.figure.color],
                                           [
                                               game.start_x + game.zoom * (j + game.figure.x) + 1,
                                               game.start_y + game.zoom * (i + game.figure.y) + 1,
                                               game.zoom - 2,
                                               game.zoom - 2
                                           ])

      font2 = pygame.font.SysFont('Consolas', 11, bold=True)
      font1 = pygame.font.SysFont('Comic Sans MS', 11, bold=True)
      text_score = font1.render("Score: " + str(game.pontos), True,(0,0,0))
      text_level = font1.render("Level: " + str(level), True, (0,0,0))
      text_lines_to_clear = font1.render("Lines to clear: " + str(lines_to_clear), True, (0,0,0))
      text_game_over1 = font1.render("Game Over", True, (0,0,0))
      text_game_over2 = font1.render("Press ESC", True,(0,0,0))

      janela.blit(text_score, [100, 20])  # second arg is represents dest where [top, left]
      janela.blit(text_lines_to_clear, [250, 20])
      janela.blit(text_level, [250, 5])
      if game.check_level():
              main()
      if game.state == "gameover":
              janela.blit(text_game_over1, [20, 220])
              janela.blit(text_game_over2, [20, 275])
      pygame.display.flip()
      relogio.tick(fps)  # paces the game to a slower fall speed


if __name__ == '__main__':
    main()
