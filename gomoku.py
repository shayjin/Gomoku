import pygame, sys, random, time

LENGTH = 760

background_yor = (255,255,255)
line_yor = (0,0,0)
line_width = 2
offset = 20

BLACK = (0,0,0)
WHITE = (255,255,255)
board_yor = (170,100,50)

pygame.init()
screen = pygame.display.set_mode((LENGTH, LENGTH))
pygame.display.set_caption("Gomoku")
screen.fill(board_yor)

board = []
turn = 'Black'

def create_board():
    global board
    board = []
    for i in range(19):
        board.append([0]* 19)
        
    line = 0
    
    screen.fill(board_yor)
    while line < 19:
        pygame.draw.line(screen, line_yor, (line*offset*2+offset,offset), (line*offset*2+offset,LENGTH-offset), line_width) 
        pygame.draw.line(screen, line_yor, (offset, line*offset*2+offset), (LENGTH-offset, line*offset*2+offset), line_width) 
        line += 1
        
    pygame.draw.line(screen, line_yor, (offset, offset), (offset, LENGTH-offset), line_width) 
    pygame.draw.line(screen, line_yor, (offset, offset), (LENGTH-offset,offset), line_width) 
    pygame.draw.line(screen, line_yor, (LENGTH-offset,LENGTH-offset), (LENGTH-offset,offset), line_width) 
    pygame.draw.line(screen, line_yor, (LENGTH-offset,LENGTH-offset), (offset, LENGTH-offset), line_width)
    
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
    screen.fill(board_yor)
    
    gomoku_font = pygame.font.Font('freesansbold.ttf', 50)
    gomoku = gomoku_font.render('Python Gomoku', True, (128,85,33), (20,20,20))
    screen.blit(gomoku, (LENGTH / 2 - LENGTH / 4, LENGTH / 7))
    
    single_player_font = pygame.font.Font('freesansbold.ttf', 30)
    single_player_mode = single_player_font.render('Singleplayer Mode', True, (100,200,0), (0,50,120))
    screen.blit(single_player_mode, (LENGTH / 2 - LENGTH / 5.5 , LENGTH / 2.2))
    
    multi_player_font = pygame.font.Font('freesansbold.ttf', 30)
    multi_player_mode = multi_player_font.render('Play Against PC', True, (100,200,0), (0,50,120))
    screen.blit(multi_player_mode, (LENGTH / 2 - LENGTH / 6.4 , LENGTH / 1.7))
    

    
    
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
            x = event.pos[0]
            y = event.pos[1]
            print(x,y)
            if in_main_menu:
                x = event.pos[0]
                y = event.pos[1]
                if x >= 175 and x < 453 and y > 380 and y < 410:
                    in_main_menu = False
                    create_board()
                elif x >= 175 and x < 410 and y > 510 and y < 535:
                    in_main_menu = False
                    multiplayer = True
                    create_board()
            else:
                if not multiplayer:
                    if not needs_to_restart:
                        x = int(((event.pos[0]) / 40))
                        y = int(((event.pos[1]) / 40))
                        print(x, y)
                        move(x, y)
                        if (check_win(x, y)):
                            switch_turn()
                            display_win_message(turn)
                            needs_to_restart = True
                    else:
                        needs_to_restart = False
                        multiplayer = False
                        in_main_menu = True
                        turn = 'Black'
                        display_main_menu()
                else:
                    if not needs_to_restart:
                        x = int(((event.pos[0]) / 40))
                        y = int(((event.pos[1]) / 40))
                        
                        
                        if board[x][y] == 0:
                            move(x, y)
                            pygame.display.update()
                            pc_x = random.randint(0,18)
                            pc_y = random.randint(0,18)
                            while board[pc_x][pc_y] != 0:
                                pc_x = random.randint(0,18)
                                pc_y = random.randint(0,18)
                            time.sleep(0.5)
                            move(pc_x,pc_y)
                        
                        if (check_win(x, y)):
                            display_win_message("Black")
                            needs_to_restart = True
                        elif (check_win(pc_x, pc_y)):
                            display_win_message("White")
                            needs_to_restart = True
                    else:
                        needs_to_restart = False
                        multiplayer = False
                        in_main_menu = True
                        turn = 'Black'
                        display_main_menu()
                    
    pygame.display.update()