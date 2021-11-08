import pygame
import numpy as np
pygame.init()

WIDTH = 500
HEIGHT = 500
LINE_COLOR = (21,76,121)
LINE_WIDTH = 7
BG_COLOR = (171,219,227)

screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Title and Icon
pygame.display.set_caption('TIC TAC TOE')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen.fill(BG_COLOR)

# Drawing lines
# horizontal lines
pygame.draw.line(screen, LINE_COLOR, (0,166), (500,166), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (0, 332), (500, 332), LINE_WIDTH)
# vertical lines
pygame.draw.line(screen, LINE_COLOR, (166, 0), (166, 500), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (332, 0), (332, 500), LINE_WIDTH)

# board 
board = np.zeros((3,3))

def markSquare(row, col, player):
    board[row][col] == player

def availableSquare(row, col):
    return board[row][col] == 0

def isBoardFull():
    for row in range (3):
        for col in range (3):
            if board[row][col] == 0:
                return False
    
    return True

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()