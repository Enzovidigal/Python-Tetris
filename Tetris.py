# -*- coding: utf-8 -*-
"""
Spyder Editor
Este é um arquivo de script temporário.
"""


import pygame
import random
from os import path 

 
pygame.font.init()
 
# Variáveis globais
s_WIDTH = 1500
s_HEIGHT = 700
play_WIDTH = 300  # meaning 300 // 10 = 30 width per block
play_HEIGHT = 600  # meaning 600 // 20 = 20 height per blo ck
block_SIZE = 30
last_score1=0
last_score2=0
 
   
top_LEFT_X = (s_WIDTH - play_WIDTH) // 2
top_LEFT_X1 = (s_WIDTH - play_WIDTH) // 2 -400 
top_LEFT_X2 = (s_WIDTH - play_WIDTH) // 2 +400
top_LEFT_Y = s_HEIGHT - play_HEIGHT
 
snd_dir = path.join(path.dirname(__file__), 'snd')
# Formas
 
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

K = [['.....',
      '.0...',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.....',
      '.....'],
     ['..0..',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
     
E = [['.....',
      '..0..',
      '.000.',
      '..0.',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '..0..',
      '.....']]
     
M = [['.....',
      '.0...',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '.00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '..0..'],
     ['.....',
      '..0..',
      '.00..',
      '..000',
      '.....']]

T = [['.....',
      '.....',
      '.000.',
      '...0.',
      '...0.'],
     ['.....',
      '.00..',
      '..0.',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.000.',
      '..0..',
      '..0..'],
     ['.....',
      '.....',
      '.00..',
      '..00.',
      '.....']]
      
Q = [['.....',
      '.....',
      '.000.',
      '.0.0.',
      '.000.'],
     ['.....',
      '.000.',
      '.0.0.',
      '.000.',
      '.....'],
     ['.....',
      '.000.',
      '.0.0.',
      '.000.',
      '.....'],
     ['.....',
      '.000.',
      '.0.0.',
      '.000.',
      '.....']]
      
 
shapes = [S, Z, I, O, J, K, E, M, T, Q]
shape_colors = [(255, 216, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0), (255, 0, 0),(255 , 255 , 255),(255, 0, 255),(255 , 255 , 255), (255 , 255 , 255),(255,165,0)]
# index 0 - 6 representa a forma

 
class Piece(object):
    rows = 20  # y
    columns = 10  # x
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # número de 0-3

def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

 
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
 
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
    return positions
 
 
def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)
 
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
 
    return True
 
 
def check_lost(positions, SCORE):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
 
 
def get_shape(buraco):
    global shapes, shape_colors
    if buraco:
        return Piece(5,0,Q)
    else:
        return Piece(5,0, random.choice(shapes[:-1]))
 
 
def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_LEFT_X + play_WIDTH/2 - (label.get_width() / 2), top_LEFT_Y + play_HEIGHT/2 - label.get_height()/2))

def draw_text_RIGHT(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_LEFT_X + 400 + play_WIDTH/2 - (label.get_width()/2), top_LEFT_Y - 350 + play_HEIGHT/2 - label.get_height()/2))

def draw_text_LEFT(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_LEFT_X - 400 + play_WIDTH/2 - (label.get_width()/2), top_LEFT_Y - 350 + play_HEIGHT/2 - label.get_height()/2))
 
def draw_text_up_right(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_LEFT_X +550 + play_WIDTH/2 - (label.get_width()/2), top_LEFT_Y - 350 + play_HEIGHT/2 - label.get_height()/2))

def draw_text_down_left(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_LEFT_X - 550 + play_WIDTH/2 - (label.get_width() / 2), top_LEFT_Y+250 + play_HEIGHT/2 - label.get_height()/2))

def draw_text_up_left(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_LEFT_X -530 + play_WIDTH/2 - (label.get_width() / 2), top_LEFT_Y -350 + play_HEIGHT/2 - label.get_height()/2))

def draw_text_down_right(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_LEFT_X + 600 + play_WIDTH/2 - (label.get_width() / 2), top_LEFT_Y+250 + play_HEIGHT/2 - label.get_height()/2))

def draw_text_legend(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_LEFT_X + play_WIDTH/2 - (label.get_width() / 2), top_LEFT_Y+100 + play_HEIGHT/2 - label.get_height()/2))

def draw_grid(surface, row, col, sx, sy):
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_WIDTH, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_HEIGHT))  # vertical lines
 

def clear_rows(grid, SCORE, locked):
    # Confere se a linha está vazia e toda outra coluna abaixo dela, desce uma linha.
    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            # adiciona posições 
            ind = i
            draw_text_middle("+1", 100, (255,255,255), win)
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                    SCORE+=1


                except:
                    continue
        if (255, 216, 0) in row:
            inc += 1
            # adiciona posições 
            ind = i
            draw_text_middle("+1", 100, (255,255,255), win)
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                    SCORE+=1
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
    return SCORE

def high_score(SCORE, last_score):
    if SCORE>last_score:
        last_score=SCORE
    return last_score
    
    
 
 
def draw_next_shape(shape, surface, top_x):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))
 
    sx = top_x + play_WIDTH + 50
    sy = top_LEFT_Y + play_HEIGHT/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)
 
    surface.blit(label, (sx + 10, sy- 30))
 
def draw_window(surface, top_x, grid, SCORE, high_score, last_score):
    # Titulo Tetris 
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (0,0,0))
 
    surface.blit(label, (top_x + play_WIDTH / 2 - (label.get_width() / 2), 30))
    
    #score
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score:'+ str(SCORE), 1, (255,255,255))

    sx = top_x + play_WIDTH + 50
    sy = top_LEFT_Y + play_HEIGHT/2 - 100

    surface.blit(label, (sx + 20, sy + 160))
    
    #high score
    label = font.render('High Score: ' + str(high_score(SCORE, last_score)), 1, (255,255,255))
    

    sx = top_x - 200
    sy = top_LEFT_Y + 200

    surface.blit(label, (sx + 20, sy + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_x + j* 30, top_LEFT_Y + i * 30, 30, 30), 0)
 
    # draw grid and border
    draw_grid(surface, 20, 10, top_x, top_LEFT_Y)
    pygame.draw.rect(surface, (255, 0, 0), (top_x, top_LEFT_Y, play_WIDTH, play_HEIGHT), 5)
    # pygame.display.update()



 
def main():
    locked_positions1 = {}  # (x,y):(255,0,0)
    locked_positions2 = {}
    grid1 = create_grid(locked_positions1)
    grid2 =create_grid(locked_positions2)


    SCORE1=0
    SCORE2=0

    change_piece1 = False
    change_piece2 = False
    run = True
    buraco1=False
    buraco2=False
    current_piece1 = get_shape(False)
    current_piece2 = get_shape(False)
    next_piece1 = get_shape(False)
    next_piece2 = get_shape(False)
    clock = pygame.time.Clock()
    fall_time = 0
    level_time=0 
    fall_speed = 0.27
    while run:
 
        grid1 = create_grid(locked_positions1)
        grid2 = create_grid(locked_positions2)
        fall_time += clock.get_rawtime()
        clock.tick()

        #score
        
        #feature que acelera o jogo
        level_time += clock.get_rawtime()
        if level_time/1000 > 1:
            level_time=0
            fall_speed-=0.002


        # PIECE FALLING CODE
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece1.y += 1
            current_piece2.y +=1
            if not (valid_space(current_piece1, grid1)) and current_piece1.y > 0:
                current_piece1.y -= 1
                change_piece1 = True
    
            if not (valid_space(current_piece2, grid2)) and current_piece2.y > 0:
                current_piece2.y -= 1
                change_piece2 = True    
            
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    current_piece1.x -= 1
                    if not valid_space(current_piece1, grid1):
                        current_piece1.x += 1
                if event.key == pygame.K_LEFT:
                    current_piece2.x -= 1
                    if not valid_space(current_piece2,grid2):
                        current_piece2.x +=1
                
                        
                elif event.key == pygame.K_d:
                    current_piece1.x += 1
                    if not valid_space(current_piece1, grid1):
                        current_piece1.x -= 1

                elif event.key == pygame.K_RIGHT:
                    current_piece2.x += 1
                    if not valid_space(current_piece2, grid2):
                        current_piece2.x -= 1

                elif event.key == pygame.K_w:
                    # rotate shape
                    current_piece1.rotation = current_piece1.rotation + 1 % len(current_piece1.shape)
                    if not valid_space(current_piece1, grid1):
                        current_piece1.rotation = current_piece1.rotation - 1 % len(current_piece1.shape)

                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece2.rotation = current_piece2.rotation + 1 % len(current_piece2.shape)
                    if not valid_space(current_piece2, grid1):
                        current_piece2.rotation = current_piece2.rotation - 1 % len(current_piece2.shape)
 
                if event.key == pygame.K_s:
                    # move shape down
                    current_piece1.y += 1
                    if not valid_space(current_piece1, grid1):
                        current_piece1.y -= 1

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece2.y += 1
                    if not valid_space(current_piece2, grid2):
                        current_piece2.y -= 1

                if event.key == pygame.K_f:
                   while valid_space(current_piece1, grid1):
                       current_piece1.y += 1
                   current_piece1.y -= 1
                   print(convert_shape_format(current_piece1))

                if event.key == pygame.K_SPACE:
                   while valid_space(current_piece2, grid2):
                       current_piece2.y += 1
                   current_piece2.y -= 1
                   print(convert_shape_format(current_piece2))
                   
        shape_pos1 = convert_shape_format(current_piece1)
        shape_pos2 = convert_shape_format(current_piece2)

        # add piece to the grid for drawing
        for i in range(len(shape_pos1)):
            x, y = shape_pos1[i]
            if y > -1:
                grid1[y][x] = current_piece1.color
    
        for e in range(len(shape_pos2)):
            x, y = shape_pos2[e]
            if y > -1:
                grid2[y][x] = current_piece2.color
       
 
        # IF PIECE HIT GROUND
        if change_piece1:
            for pos in shape_pos1:
                p = (pos[0], pos[1])
                locked_positions1[p] = current_piece1.color
            current_piece1 = next_piece1
            next_piece1 = get_shape(buraco1)
            change_piece1 = False
            buraco1 = False

            new_score1=clear_rows(grid1, SCORE1, locked_positions1)
            if new_score1!= SCORE1:
                buraco2=True
            SCORE1= new_score1
        
        if change_piece2:
            for pos in shape_pos2:
                p = (pos[0], pos[1])
                locked_positions2[p] = current_piece2.color
            current_piece2 = next_piece2
            next_piece2 = get_shape(buraco2)
            change_piece2 = False
            buraco2 = False
 
            # call four times to check for multiple clear rows
            new_score2=clear_rows(grid2, SCORE2, locked_positions2)
            if new_score2 != SCORE2:
                buraco1=True
            SCORE2= new_score2
        
        win.fill((0,0,0))
        draw_window(win, top_LEFT_X1, grid1, SCORE1, high_score, last_score1)
        draw_window(win, top_LEFT_X2, grid2, SCORE2, high_score, last_score2)
        draw_next_shape(next_piece1, win, top_LEFT_X1)
        draw_next_shape(next_piece2, win, top_LEFT_X2)
        pygame.display.update()
 
        # Check if user lost
        if check_lost(locked_positions1, SCORE1):
            run = False
            SCORE1=0
            SCORE2=0
            draw_text_LEFT("VOCÊ PERDEU:(", 50, (255,255,255), win)
            draw_text_RIGHT("VOCÊ GANHOU:)", 50, (255,255,255), win)
            pygame.display.update()
            pygame.time.delay(4000) 
        
        elif check_lost(locked_positions2, SCORE2):
            run = False
            SCORE1=0
            SCORE2=0
            draw_text_RIGHT("VOCÊ PERDEU:(", 50, (255,255,255), win)
            draw_text_LEFT("VOCÊ GANHOU:)", 50, (255,255,255), win)
            pygame.display.update()
            pygame.time.delay(2000)
    win.fill((0,0,0))
    draw_text_middle("GAME OVER", 100, (255,255,255), win)
    pygame.display.update()
    pygame.time.delay(4000)

def main_menu():
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle('TETRIS', 100, (255, 255, 255), win)
        draw_text_legend('Clique para começar', 25, (255, 255, 255), win)
        draw_text_up_right('AMARELA - Bomba', 50, (255, 216, 0), win)
        draw_text_up_left('VERMELHA - Regular', 50, (255, 0, 0), win)
        draw_text_down_right('ROSA - Fixa', 50, (255, 0, 255), win)
        draw_text_down_left('BRANCA - Variável', 50, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
            if event.type == pygame.KEYDOWN:
                main() 
            
    pygame.quit()
 
win = pygame.display.set_mode((s_WIDTH, s_HEIGHT))
pygame.display.set_caption('Tetris')
 
main_menu()  # começa o jogo 