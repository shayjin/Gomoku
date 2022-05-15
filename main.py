import pygame, sys

WIDTH = 800
HEIGHT = 800

background_color = (100,120,120)
line_color = (0,0,0)
line_width = 5
O_color = (0,0,0)
X_color = (255,255,255)
win_color = (255,255,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(background_color)

def draw_board():
    pygame.draw.line(screen, line_color, (0,HEIGHT/3), (WIDTH,HEIGHT/3), line_width)
    pygame.draw.line(screen, line_color, (0,HEIGHT*2/3), (WIDTH,HEIGHT*2/3), line_width)
    pygame.draw.line(screen, line_color, (WIDTH/3,0), (WIDTH/3,HEIGHT), line_width)
    pygame.draw.line(screen, line_color, (WIDTH*2/3,0), (WIDTH*2/3,HEIGHT), line_width)

turn = 'O'
board = [
            ['', '', ''], 
            ['', '', ''], 
            ['', '', '']
        ]

def mark(row, col):
    global turn
    if board[row][col] == '':
        if turn == 'O':
            board[row][col] = 'O'
            draw(row, col)
            switch_turn()
        else:
            board[row][col] = 'X'
            draw(row, col)
            switch_turn()
            
def set_circle_radius():
    if WIDTH > HEIGHT:
        circle_radius = HEIGHT / 10
    else:
        circle_radius = WIDTH / 10
    return int(circle_radius)

def set_element_width():
    if WIDTH > HEIGHT:
        element_width = HEIGHT / 60
    else:
        element_width = WIDTH / 60
    return int(element_width)

def draw(row, col):
    global turn
    if turn == 'O':
        pygame.draw.circle(screen, O_color, (int(col * WIDTH/3 + WIDTH/6), int(row * HEIGHT/3 + HEIGHT/6)), set_circle_radius(), element_width)
    else:
        pygame.draw.line(screen, X_color, (int(col * WIDTH/3 + WIDTH/12), int(row * HEIGHT/3+ HEIGHT/12)), (int(col* WIDTH/3 + WIDTH/4), int(row * HEIGHT/3 + HEIGHT/4)), element_width)
        pygame.draw.line(screen, X_color, (int(col * WIDTH/3 + WIDTH/12), int(row * HEIGHT/3 + HEIGHT/4)), (int(col* WIDTH/3 + WIDTH/4), int(row * HEIGHT/3 + HEIGHT/12)), element_width)

def switch_turn():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

def is_win():
    for i in range(2):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != '':
            pygame.draw.line(screen, win_color, (0, int(i * HEIGHT/3 + HEIGHT/6)), (WIDTH, int(i * HEIGHT/3 + HEIGHT/6)), element_width)
            return board[i][0]
        elif (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != '':
            pygame.draw.line(screen, win_color, (int(i * WIDTH/3 + WIDTH/6), 0), (int(i * WIDTH/3 + WIDTH/6), HEIGHT), element_width)
            return board[0][i]
        
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != '':
        pygame.draw.line(screen, win_color, (0,0), (WIDTH,HEIGHT), element_width)
        return board[0][0]
    
    if (board[2][0] == board[1][1] == board[0][2]) and board[2][0] != '':
        pygame.draw.line(screen, win_color, (WIDTH,0), (0,HEIGHT), element_width)
        return board[2][0]
    
    return False

def display_win_message(turn):
    message = turn + ' wins! Click anywhere to restart...'
    font_size = int(WIDTH/(len(message))*1.75) # size responsive lol
    
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(message, True, (128,0,0), (0,0,128))
    screen.blit(text, (WIDTH / 2 - WIDTH / 2.5 , HEIGHT / 2))

def restart():
    global board
    screen.fill((background_color))
    draw_board()
    turn = 'O'
    board = [
            ['', '', ''], 
            ['', '', ''], 
            ['', '', '']
        ]
    
draw_board()
need_to_restart = False
element_width = set_element_width()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not need_to_restart:
                col = int(event.pos[0] / (WIDTH / 3))
                row = int(event.pos[1] / (HEIGHT / 3))
                
                mark(row, col)
                win_shape = is_win()
                
                if win_shape:
                    switch_turn()
                    display_win_message(turn)
                    print(win_shape + ' wins!!!!!!!')
                    need_to_restart = True
            else:
                need_to_restart = False
                restart()
                
    pygame.display.update()