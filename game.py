# Modules
import pygame
import numpy as np
import settings as s

# Initialize pygame
pygame.init()

# screen
screen = pygame.display.set_mode((s.WIDTH,s.HEIGHT))
# Title and Icon
pygame.display.set_caption('TIC TAC TOE')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen.fill(s.BG_COLOR)

def drawLines():  # Drawing lines function
    # horizontal lines
    pygame.draw.line(screen, s.LINE_COLOR, (0,s.SQUARE_SIZE), (500,s.SQUARE_SIZE), s.LINE_WIDTH)
    pygame.draw.line(screen, s.LINE_COLOR, (0, 332), (500, 332), s.LINE_WIDTH)
    # vertical lines
    pygame.draw.line(screen, s.LINE_COLOR, (s.SQUARE_SIZE, 0), (s.SQUARE_SIZE, 500), s.LINE_WIDTH)
    pygame.draw.line(screen, s.LINE_COLOR, (332, 0), (332, 500), s.LINE_WIDTH)

# console board 
board = np.zeros((3,3))

# Functions

def playerEquals(x, y, z):
    return x!=0 and x==y and y==z

def checkWinner():
    winner = None

    # vertical win 
    for col in range (s.COLS):
        if playerEquals(board[0][col], board[1][col], board[2][col]):
            winner = board[0][col]
            vertical_winline(col, winner)
            return True
    
    # horizontal win
    for row in range (s.ROWS):
        if playerEquals(board[row][0], board[row][1], board[row][2]):
            winner = board[row][0]
            horizontal_winline(row, winner)
            return True
    
    # ascending diagonal win 
    if playerEquals(board[2][0], board[1][1], board[0][2]):
        winner = board[2][0]
        asc_diagonal_winline(winner)
        return True

    # descending diagonal win
    if playerEquals(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]
        desc_diagonal_winline(winner)
        return True

    return False

# functions for drawing winning lines

def vertical_winline(col, winner):
    posX = col * s.SQUARE_SIZE + s.SQUARE_SIZE//2  # column is constant 
    if winner == 1:
        color = 'white'
    elif winner == 2:
        color = 'black'
    pygame.draw.line(screen, color, (posX, 15), (posX, s.HEIGHT-15), 15)
 
def horizontal_winline(row, winner):
    posY = row * s.SQUARE_SIZE + s.SQUARE_SIZE//2
    if winner == 1:
        color = 'white'
    else:
        color = 'black'
    pygame.draw.line(screen, color, (15, posY), (s.WIDTH-15, posY), 15)

def asc_diagonal_winline(winner):
    if winner == 1:
        color = 'white'
    else: 
        color = 'black'
    pygame.draw.line(screen, color, (15, s.HEIGHT-15), (s.WIDTH-15, 15), 15)

def desc_diagonal_winline(winner):
    if winner == 1:
        color = 'white'
    else: 
        color = 'black'  
    pygame.draw.line(screen, color, (15, 15), (s.WIDTH-15, s.HEIGHT-15), 15)

    

def figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1: 
                pygame.draw.circle(screen, 'white', ( int(col * s.SQUARE_SIZE + 83), int(row * s.SQUARE_SIZE + 83)), s.C_RADIUS, s.C_WIDTH)

            elif board[row][col] == 2:
                pygame.draw.line(screen, 'black', (col * s.SQUARE_SIZE + s.SPACE, row * s.SQUARE_SIZE + s.SQUARE_SIZE - s.SPACE ), (col * s.SQUARE_SIZE + s.SQUARE_SIZE - s.SPACE, row * s.SQUARE_SIZE + s.SPACE), s.CROSS_WIDTH)
                pygame.draw.line(screen, 'black', (col * s.SQUARE_SIZE + s.SPACE, row * s.SQUARE_SIZE + s.SPACE ), (col * s.SQUARE_SIZE +  s.SQUARE_SIZE - s.SPACE, row * s.SQUARE_SIZE + s.SQUARE_SIZE - s.SPACE), s.CROSS_WIDTH)

def markSquare(row, col, player):
    board[row][col] = player

def availableSquare(row, col):
    return board[row][col] == 0

def isBoardFull():
    for row in range (3):
        for col in range (3):
            if board[row][col] == 0:
                return False
    
    return True


drawLines()
player = 1 # initializing player
gameOver = False
# game loop

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            mouseX = event.pos[0]  # x coordinate
            mouseY = event.pos[1]  # y coordinate

            clicked_row = int(mouseY // s.SQUARE_SIZE)
            clicked_col = int(mouseX // s.SQUARE_SIZE)

            if availableSquare (clicked_row, clicked_col):
                
                markSquare(clicked_row, clicked_col, player)
                if checkWinner():
                    gameOver = True
                player = player % 2 + 1

                figures()
                
    pygame.display.update()