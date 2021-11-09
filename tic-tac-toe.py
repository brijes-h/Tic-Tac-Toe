# Modules
import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH = 500
HEIGHT = 500
SQUARE_SIZE = 166
LINE_WIDTH = 7
BG_COLOR = (171,219,227)
C_RADIUS = 50
C_WIDTH = 12
LINE_COLOR = (21,76,121) # rgb values
CROSS_WIDTH = 20
SPACE = 37  # space between the line and cross

# screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
# Title and Icon
pygame.display.set_caption('TIC TAC TOE')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen.fill(BG_COLOR)

# Drawing lines
# horizontal lines
pygame.draw.line(screen, LINE_COLOR, (0,SQUARE_SIZE), (500,SQUARE_SIZE), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (0, 332), (500, 332), LINE_WIDTH)
# vertical lines
pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, 500), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (332, 0), (332, 500), LINE_WIDTH)

# console board 
board = np.zeros((3,3))

# Functions

def figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1: 
                pygame.draw.circle(screen, 'white', ( int(col * SQUARE_SIZE + 83), int(row * SQUARE_SIZE + 83)), C_RADIUS, C_WIDTH)

            elif board[row][col] == 2:
                pygame.draw.line(screen, 'black', (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE ), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, 'black', (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE ), (col * SQUARE_SIZE +  SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

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

player = 1 # initializing player

# game loop

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # x coordinate
            mouseY = event.pos[1]  # y coordinate

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if availableSquare (clicked_row, clicked_col):
                if player == 1:
                    markSquare (clicked_row, clicked_col, 1)
                    player = 2  # updating player for next turn
                elif player == 2:
                    markSquare (clicked_row, clicked_col, 2)
                    player = 1
                
                figures()
                
    pygame.display.update()