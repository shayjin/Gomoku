
import pygame, sys

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
    for i in range(19):
        board.append([0]* 19)
    
    pygame.draw.line(screen, line_yor, (offset, offset), (offset, LENGTH-offset), line_width) 
    pygame.draw.line(screen, line_yor, (offset, offset), (LENGTH-offset,offset), line_width) 
    pygame.draw.line(screen, line_yor, (LENGTH-offset,LENGTH-offset), (LENGTH-offset,offset), line_width) 
    pygame.draw.line(screen, line_yor, (LENGTH-offset,LENGTH-offset), (offset, LENGTH-offset), line_width)

    line = 0
    
    while line < 19:
        pygame.draw.line(screen, line_yor, (line*offset*2+offset,offset), (line*offset*2+offset,LENGTH-offset), line_width) 
        pygame.draw.line(screen, line_yor, (offset, line*offset*2+offset), (LENGTH-offset, line*offset*2+offset), line_width) 
        line += 1
    
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
    if board[x][y] == board[x][y-1] == board[x][y-2] == board[x][y-3] == board[x][y-4]: 
        return True
    elif board[x][y+1] == board[x][y] == board[x][y-1] == board[x][y-2] == board[x][y-3]: 
        return True
    elif board[x][y+2] == board[x][y+1] == board[x][y] == board[x][y-1] == board[x][y-2]: 
        return True
    elif board[x][y+3] == board[x][y+2] == board[x][y+1] == board[x][y] == board[x][y-1]: 
        return True
    elif board[x][y+4] == board[x][y+3] == board[x][y+2] == board[x][y+1] == board[x][y]: 
        return True
    else:
        return False

def check_horizontal(x, y):
    if board[x][y] == board[x-1][y] == board[x-2][y] == board[x-3][y] == board[x-4][y]:
        return True
    elif board[x+1][y] == board[x][y] == board[x-1][y] == board[x-2][y] == board[x-3][y]:
        return True
    elif board[x+2][y] == board[x+1][y] == board[x][y] == board[x-1][y] == board[x-2][y]:
        return True
    elif board[x+3][y] == board[x+2][y] == board[x+1][y] == board[x][y] == board[x-1][y]:
        return True
    elif board[x+4][y] == board[x+3][y] == board[x+2][y] == board[x+1][y] == board[x][y]:
        return True
    else:
        return False

def check_diagonal(x,y):
    if board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3] == board[x-4][y+4]:
        return True
    elif board[x+1][y-1] == board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3]:
        return True
    elif board[x+2][y-2] == board[x+1][y-1] == board[x][y] == board[x-1][y+1] == board[x-2][y+2]:
        return True
    elif board[x+3][y-3] == board[x+2][y-2] == board[x+1][y-1] == board[x][y] == board[x-1][y+1]:
        return True
    elif board[x+4][y-4] == board[x+3][y-3] == board[x+2][y-2] == board[x+1][y-1] == board[x][y]:
        return True
    elif board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] == board[x+4][y+4]:
        return True
    elif board[x-1][y-1] == board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3]:
        return True
    elif board[x-2][y-2] == board[x-1][y-1] == board[x][y] == board[x+1][y+1] == board[x+2][y+2]:
        return True
    elif board[x-3][y-3] == board[x-2][y-2] == board[x-1][y-1] == board[x][y] == board[x+1][y+1]:
        return True
    elif board[x-4][y-4] == board[x-3][y-3] == board[x-2][y-2] == board[x-1][y-1] == board[x][y]:
        return True
    else:
        return False
            
def check_win(x, y):
    if check_vertical(x, y): return True
    elif check_horizontal(x, y): return True
    elif check_diagonal(x, y): return True
    else: return False
    
def display_win_message(turn):
    message = turn + ' wins! Click anywhere to restart...'
    font_size = int(LENGTH/(len(message))*1.75) # size responsive lol
    
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(message, True, (128,0,0), (0,0,128))
    screen.blit(text, (LENGTH / 2 - LENGTH / 2.5 , LENGTH / 2))
    
def restart():
    screen.fill(board_yor)
    create_board()
    turn = 'Black'

needs_to_restart = False
create_board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
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
                restart()
            
            
            
    pygame.display.update()