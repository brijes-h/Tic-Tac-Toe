import pygame, sys
pygame.init()

WIDTH = 500
HEIGHT = 500
LINE_COLOR = 'black'
LINE_WIDTH = 7

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill('grey')

# Drawing lines
# horizontal lines
pygame.draw.line(screen, LINE_COLOR, (0,166), (500,166), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (0, 332), (500, 332), LINE_WIDTH)
# vertical lines
pygame.draw.line(screen, LINE_COLOR, (166, 0), (166, 500), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (332, 0), (332, 500), LINE_WIDTH)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()