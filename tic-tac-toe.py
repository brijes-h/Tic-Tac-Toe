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
    while (x!=0 and y!=0 and z!=0):
        if x==y and y==z:
            return True

def checkWinner():
    winner = None

    # vertical win 
    for col in range (s.COLS):
        if playerEquals(board[0][col], board[1][col], board[2][col]):
            winner = board[0][col]
            vertical_winline(col, winner)
    
    # horizontal win
    for row in range (s.ROWS):
        if playerEquals(board[row][0], board[row][1], board[row][2]):
            winner = board[row][0]
            # drawing line fun
    
    # ascending diagonal win 
    if playerEquals(board[2][0], board[1][1], board[0][2]):
        winner = board[2][0]
        # drawing line fun
    
    # descending diagonal win
    if playerEquals(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]
        # drawing line fun

    #return False winner is None


def vertical_winline(col, winner):
    posX = col * s.SQUARE_SIZE + s.SQUARE_SIZE//2  # column is constant 
    if winner == 1:
        color = 'white'
    elif winner == 2:
        color = 'black'
    pygame.draw.line(screen, color, (posX, 15), (posX, s.HEIGHT-15), 15)
 

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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # x coordinate
            mouseY = event.pos[1]  # y coordinate

            clicked_row = int(mouseY // s.SQUARE_SIZE)
            clicked_col = int(mouseX // s.SQUARE_SIZE)

            if availableSquare (clicked_row, clicked_col):
                if player == 1:
                    markSquare (clicked_row, clicked_col, 1)
                    checkWinner()
                    player = 2  # updating player for next turn
                elif player == 2:
                    markSquare (clicked_row, clicked_col, 2)
                    checkWinner()
                    player = 1
                
                figures()
                
    pygame.display.update()