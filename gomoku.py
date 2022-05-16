from audioop import mul
import pygame
import sys
import random
import time

LENGTH = 760

background_yor = (255,255,255)
line_yor = (0,0,0)
line_width = 2
offset = 20

BLACK = (0,0,0)
WHITE = (255,255,255)
BOARD_COLOR = (222,185,135)

pygame.init()
screen = pygame.display.set_mode((LENGTH, LENGTH))
pygame.display.set_caption("Python Gomoku")
screen.fill(BOARD_COLOR)

board = []
turn = 'Black'

def create_board():
    global board
    board = []
    
    for i in range(19):
        board.append([0]* 19)
        
    line = 0
    
    screen.fill(BOARD_COLOR)
    while line < 19:
        pygame.draw.line(screen, line_yor, (line*offset*2+offset,offset), (line*offset*2+offset,LENGTH-offset), line_width) 
        pygame.draw.line(screen, line_yor, (offset, line*offset*2+offset), (LENGTH-offset, line*offset*2+offset), line_width) 
        line += 1
        
    pygame.draw.line(screen, line_yor, (offset, offset), (offset, LENGTH-offset), line_width) 
    pygame.draw.line(screen, line_yor, (offset, offset), (LENGTH-offset,offset), line_width) 
    pygame.draw.line(screen, line_yor, (LENGTH-offset,LENGTH-offset), (LENGTH-offset,offset), line_width) 
    pygame.draw.line(screen, line_yor, (LENGTH-offset,LENGTH-offset), (offset, LENGTH-offset), line_width)
    SAM_CHUN_WON()

# ??????: 꿀발라줘라
# 조수현: ?
def SAM_CHUN_WON():
    pygame.draw.circle(screen, BLACK, (181,181),5,5)
    pygame.draw.circle(screen, BLACK, (581,581),5,5)
    pygame.draw.circle(screen, BLACK, (181,581),5,5)
    pygame.draw.circle(screen, BLACK, (581,181),5,5)
    pygame.draw.circle(screen, BLACK, (181,LENGTH/2),5,5)
    pygame.draw.circle(screen, BLACK, (581,LENGTH/2),5,5)
    pygame.draw.circle(screen, BLACK, (LENGTH/2,581),5,5)
    pygame.draw.circle(screen, BLACK, (LENGTH/2,181),5,5)
    pygame.draw.circle(screen, BLACK, (LENGTH/2,LENGTH/2),5,5)
    
def switch_turn():
    global turn
    if turn == 'Black': turn = 'White'
    else: turn = 'Black'
    
def move(x, y):
    global turn
    if board[x][y] == 0:
        if turn == 'Black':
            board[x][y] = 1
            pygame.draw.circle(screen, BLACK, (x*40+20,y*40+20),15,15)
            switch_turn()
        else: 
            board[x][y] = 2
            pygame.draw.circle(screen, WHITE, (x*40+20,y*40+20),15,15)
            switch_turn()
            
def check_vertical(x, y):
    if y >= 4 and board[x][y] == board[x][y-1] == board[x][y-2] == board[x][y-3] == board[x][y-4]: 
        return True
    elif y >= 3 and y < 18 and board[x][y+1] == board[x][y] == board[x][y-1] == board[x][y-2] == board[x][y-3]: 
        return True
    elif y >= 2 and y < 17 and board[x][y+2] == board[x][y+1] == board[x][y] == board[x][y-1] == board[x][y-2]: 
        return True
    elif y >= 1 and y < 16 and board[x][y+3] == board[x][y+2] == board[x][y+1] == board[x][y] == board[x][y-1]: 
        return True
    elif y < 15 and board[x][y+4] == board[x][y+3] == board[x][y+2] == board[x][y+1] == board[x][y]: 
        return True
    else:
        return False

def check_horizontal(x, y):
    if x >= 4 and board[x][y] == board[x-1][y] == board[x-2][y] == board[x-3][y] == board[x-4][y]:
        return True
    elif x >= 3 and x < 18 and board[x+1][y] == board[x][y] == board[x-1][y] == board[x-2][y] == board[x-3][y]:
        return True
    elif x >= 2 and x < 17 and board[x+2][y] == board[x+1][y] == board[x][y] == board[x-1][y] == board[x-2][y]:
        return True
    elif x >= 1 and x < 16 and board[x+3][y] == board[x+2][y] == board[x+1][y] == board[x][y] == board[x-1][y]:
        return True
    elif x < 15 and board[x+4][y] == board[x+3][y] == board[x+2][y] == board[x+1][y] == board[x][y]:
        return True
    else:
        return False

def check_diagonal(x,y):
    if x >= 4 and y < 15 and board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3] == board[x-4][y+4]:
        return True
    elif x >= 3 and x < 18 and y >= 1 and y < 16 and board[x+1][y-1] == board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3]:
        return True
    elif x >= 2 and x < 17 and y >= 2 and y < 17 and board[x+2][y-2] == board[x+1][y-1] == board[x][y] == board[x-1][y+1] == board[x-2][y+2]:
        return True
    elif x >= 1 and x < 16 and y >= 3 and y < 18 and board[x+3][y-3] == board[x+2][y-2] == board[x+1][y-1] == board[x][y] == board[x-1][y+1]:
        return True
    elif x < 15 and y >= 4 and board[x+4][y-4] == board[x+3][y-3] == board[x+2][y-2] == board[x+1][y-1] == board[x][y]:
        return True
    elif x < 15 and y < 15 and board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] == board[x+4][y+4]:
        return True
    elif x >= 1 and x < 16 and y >= 1 and y < 16 and board[x-1][y-1] == board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3]:
        return True
    elif x >= 2 and x < 17 and y >= 2 and y < 17 and board[x-2][y-2] == board[x-1][y-1] == board[x][y] == board[x+1][y+1] == board[x+2][y+2]:
        return True
    elif x >= 3 and x < 18 and y >= 3 and y < 18 and board[x-3][y-3] == board[x-2][y-2] == board[x-1][y-1] == board[x][y] == board[x+1][y+1]:
        return True
    elif x >= 4 and y >= 4 and board[x-4][y-4] == board[x-3][y-3] == board[x-2][y-2] == board[x-1][y-1] == board[x][y]:
        return True
    else:
        return False
            
def check_win(x, y):
    if check_vertical(x, y): return True
    elif check_horizontal(x, y): return True
    elif check_diagonal(x, y): return True
    else: return False
    
def display_win_message(turn):
    message = turn + ' wins!!!!!!'
    font_size = int(LENGTH/(len(message))*1.75) # size responsive lol
    
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(message, True, (128,0,0), (0,0,128))
    screen.blit(text, (LENGTH / 2 - LENGTH / 2.5 , LENGTH / 2))
    

# menu
def display_main_menu():
    screen.fill(BOARD_COLOR)
    
    gomoku_font = pygame.font.Font('freesansbold.ttf', 50)
    gomoku = gomoku_font.render('Python Gomoku', True, (128,85,33), (20,20,20))
    screen.blit(gomoku, (LENGTH / 2 - LENGTH / 4, LENGTH / 7))
    
    single_player_font = pygame.font.Font('freesansbold.ttf', 30)
    single_player_mode = single_player_font.render('Singleplayer Mode', True, (100,200,0), (0,50,120))
    screen.blit(single_player_mode, (LENGTH / 2 - LENGTH / 5.5 , LENGTH / 2.2))
    
    multi_player_font = pygame.font.Font('freesansbold.ttf', 30)
    multi_player_mode = multi_player_font.render('Play Against PC', True, (100,200,0), (0,50,120))
    screen.blit(multi_player_mode, (LENGTH / 2 - LENGTH / 6.4 , LENGTH / 1.7))
    
def reset():
    global needs_to_restart
    global multiplayer
    global in_main_menu
    global turn
    
    needs_to_restart = False
    multiplayer = False
    in_main_menu = True
    turn = 'Black'
    
    display_main_menu()

# main method
in_main_menu = True
multiplayer = False
needs_to_restart = False
display_main_menu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:       
            if in_main_menu:
                x = event.pos[0]
                y = event.pos[1]
                print(x, y)
                if x >= 245 and x < 520 and y > 350 and y < 375:
                    in_main_menu = False
                    create_board()
                elif x >= 265 and x < 495 and y > 450 and y < 480:
                    in_main_menu = False
                    multiplayer = True
                    create_board()
            else:
                if not multiplayer:
                    if not needs_to_restart:
                        
                        x = int(((event.pos[0]) / 40))
                        y = int(((event.pos[1]) / 40))
                        
                        move(x, y)
                        
                        if (check_win(x, y)):
                            switch_turn()
                            display_win_message(turn)
                            needs_to_restart = True
                    else:
                       reset()
                else:
                    if not needs_to_restart:
                        x = int(((event.pos[0]) / 40))
                        y = int(((event.pos[1]) / 40))
                        
                        if board[x][y] == 0:
                            move(x, y)
                            pygame.display.update()
                            
                            rand = random.randint(0,1) # for randomness
                            
                            if rand == 1:
                                pc_x = random.randint(x,x+1)
                                pc_y = random.randint(y,y+1)
                                while pc_x >= 19 or pc_y >= 19 or board[pc_x][pc_y] != 0:
                                    
                                    pc_x = random.randint(x,x+2)
                                    pc_y = random.randint(y,y+2)
                                    
                                    if board[pc_x][pc_y] != 0:
                                        pc_x = 20
                                        pc_y = 20
                                        
                                time.sleep(0.5)
                                move(pc_x,pc_y)
                            else:
                                pc_x = random.randint(x-1,x)
                                pc_y = random.randint(y-1,y)
                                while pc_x < 0 or pc_y < 0 or board[pc_x][pc_y] != 0:
                                    
                                    pc_x = random.randint(x-2,x)
                                    pc_y = random.randint(y-2,y)
                                    
                                    if board[pc_x][pc_y] != 0:
                                        pc_x = -1
                                        pc_y = -1
                                
                                time.sleep(0.5)
                                move(pc_x,pc_y)
   
                        if (check_win(x, y)):
                            display_win_message("Black")
                            needs_to_restart = True
                        elif (check_win(pc_x, pc_y)):
                            display_win_message("White")
                            needs_to_restart = True
                    else:
                        print('hi')
                        reset()
                    
    pygame.display.update()