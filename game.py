# Modules
import pygame
import numpy as np
import random
from pygame.constants import KEYDOWN
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

# console board 
board = np.zeros((3,3))

# Functions

def drawLines():  # Drawing lines function
    # horizontal lines
    pygame.draw.line(screen, s.LINE_COLOR, (0,s.SQUARE_SIZE), (500,s.SQUARE_SIZE), s.LINE_WIDTH)
    pygame.draw.line(screen, s.LINE_COLOR, (0, 332), (500, 332), s.LINE_WIDTH)
    # vertical lines
    pygame.draw.line(screen, s.LINE_COLOR, (s.SQUARE_SIZE, 0), (s.SQUARE_SIZE, 500), s.LINE_WIDTH)
    pygame.draw.line(screen, s.LINE_COLOR, (332, 0), (332, 500), s.LINE_WIDTH)


def playerEquals(x, y, z):
    return x!=0 and x==y and y==z

def checkDraw():
    emp = 0
    for row in range (s.ROWS):
        for col in range (s.COLS):
            if availableSquare(row, col):
                emp += 1
    
    if emp==0:
        return 'Draw'

def checkWinner():
    winner = None
    # check for tie
    winner = checkDraw()
    # vertical win 
    for col in range (s.COLS):
        if playerEquals(board[0][col], board[1][col], board[2][col]):
            winner = board[0][col]
    # horizontal win
    for row in range (s.ROWS):
        if playerEquals(board[row][0], board[row][1], board[row][2]):
            winner = board[row][0]
    # ascending diagonal win 
    if playerEquals(board[2][0], board[1][1], board[0][2]):
        winner = board[2][0]
    # descending diagonal win
    if playerEquals(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]

    return winner

# functions for drawing winning lines
def vertical_winline(col, winner):
    posX = col * s.SQUARE_SIZE + s.SQUARE_SIZE//2  # column is constant 
    if winner == 1:
        color = s.O_COLOR
    elif winner == 2:
        color = s.X_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, s.HEIGHT-15), 15)
 
def horizontal_winline(row, winner):
    posY = row * s.SQUARE_SIZE + s.SQUARE_SIZE//2  # row is constant
    if winner == 1:
        color = s.O_COLOR
    else:
        color = s.X_COLOR
    pygame.draw.line(screen, color, (15, posY), (s.WIDTH-15, posY), 15)

def asc_diagonal_winline(winner):
    if winner == 1:
        color = s.O_COLOR
    else: 
        color = s.X_COLOR
    pygame.draw.line(screen, color, (15, s.HEIGHT-15), (s.WIDTH-15, 15), 15)

def desc_diagonal_winline(winner):
    if winner == 1:
        color = s.O_COLOR
    else: 
        color = s.X_COLOR  
    pygame.draw.line(screen, color, (15, 15), (s.WIDTH-15, s.HEIGHT-15), 15)

# function for drawing Os and Xs
def figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1: 
                pygame.draw.circle(screen, s.O_COLOR, ( int(col * s.SQUARE_SIZE + 83), int(row * s.SQUARE_SIZE + 83)), s.C_RADIUS, s.C_WIDTH)

            elif board[row][col] == 2:
                pygame.draw.line(screen, s.X_COLOR, (col * s.SQUARE_SIZE + s.SPACE, row * s.SQUARE_SIZE + s.SQUARE_SIZE - s.SPACE ), (col * s.SQUARE_SIZE + s.SQUARE_SIZE - s.SPACE, row * s.SQUARE_SIZE + s.SPACE), s.CROSS_WIDTH)
                pygame.draw.line(screen, s.X_COLOR, (col * s.SQUARE_SIZE + s.SPACE, row * s.SQUARE_SIZE + s.SPACE ), (col * s.SQUARE_SIZE +  s.SQUARE_SIZE - s.SPACE, row * s.SQUARE_SIZE + s.SQUARE_SIZE - s.SPACE), s.CROSS_WIDTH)

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

def restart():
    screen.fill(s.BG_COLOR)
    drawLines()
    player = 1
    for row in range (s.ROWS):
        for col in range (s.COLS):
            board[row][col] = 0

def render():
    x = checkWinner()

    if x != None and x != 'Draw':
        # vertical win
        for col in range (s.COLS):
            if playerEquals(board[0][col], board[1][col], board[2][col]):
                winner = board[0][col]
                vertical_winline(col, winner)
        # horizontal win
        for row in range (s.ROWS):
            if playerEquals(board[row][0], board[row][1], board[row][2]):
                winner = board[row][0]
                horizontal_winline(row, winner)
        # ascending diagonal win 
        if playerEquals(board[2][0], board[1][1], board[0][2]):
            winner = board[2][0]
            asc_diagonal_winline(winner)
        # descending diagonal win
        if playerEquals(board[0][0], board[1][1], board[2][2]):
            winner = board[0][0]
            desc_diagonal_winline(winner)

    display(x)

def display(x):
    if x == 1:
        text = "O WINS!!!  Press 'R' to play again!"
        drawTexttoScreen (screen, text, 250, 250, 'GREEN')
    elif x == 2:
        text = "X WINS!!!   Press 'R' to play again!"
        drawTexttoScreen (screen, text, 250, 250)
    elif x == 'Draw':
        text = "DRAW!!!   Press 'R' to play again!"
        drawTexttoScreen (screen, text, 250, 250)


def drawTexttoScreen (screen, text, x, y, color = (250, 0, 0)):
    font = pygame.font.SysFont('chalkduster.ttf', 30)
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()

    textRect.centerx = x
    textRect.centery = y

    screen.blit(textSurface, textRect)

def playerMove(row, col, player):
    markSquare(row, col, player)
    return 
        
def compMove():  
    bestScore = float('-inf')
    new_r = new_c = None
    for row in range(s.ROWS):
        for col in range(s.COLS):
            if availableSquare(row, col):

                markSquare(row, col, 1)
                score = minimax(0, float('-inf'), float('inf'), False)
                markSquare(row, col, 0)
                if score > bestScore:
                    bestScore = score
                    new_r, new_c = row, col
    markSquare(new_r, new_c, 1)
    return

# Minimax function
def minimax(depth, alpha, beta, is_maximizing):
    winner = checkWinner()
    if winner != None:
        return s.score[winner]

    if is_maximizing:
        bestScore = float('-inf')

        for row in range(s.ROWS):
            for col in range(s.COLS):
                if availableSquare(row, col):

                    markSquare(row, col, 1)
                    score = minimax(depth + 1, alpha, beta, False)
                    markSquare(row, col, 0)
                    bestScore = max(score, bestScore)

                    alpha = max(alpha, bestScore)  # pruning
                    if beta <= alpha:
                        return bestScore

        return bestScore

    else:
        bestScore = float('inf')

        for row in range(3):
            for col in range(3):
                if availableSquare(row, col):

                    markSquare(row, col, 2)
                    score = minimax(depth + 1, alpha, beta, True)
                    markSquare(row, col, 0)
                    bestScore = min(score, bestScore)

                    beta = min(beta, bestScore)  # pruning
                    if beta <= alpha:
                        return bestScore

        return bestScore

drawLines()
player =  random.choice(s.p) # initializing player
gameOver = False

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # for comp move
        if player == 1 and not gameOver:
            compMove()
            winner = checkWinner()
            if winner != None:
                gameOver = True
            player = 2
            figures()
            render()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            mouseX = event.pos[0]  # x coordinate
            mouseY = event.pos[1]  # y coordinate

            clicked_row = int(mouseY // s.SQUARE_SIZE)
            clicked_col = int(mouseX // s.SQUARE_SIZE)
            # for player move
            if availableSquare (clicked_row, clicked_col):
                if player == 2:
                    playerMove(clicked_row, clicked_col, 2)
                    
                winner = checkWinner()
                if winner != None:
                    gameOver = True
                player = 1
                figures()
                render()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                gameOver = False # changing gameOver to False for the next game

    pygame.display.update()
