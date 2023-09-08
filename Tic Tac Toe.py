import pygame, sys
import numpy as np

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")

screen.fill((64, 45, 150))
line = (255, 0, 70)
width = 15
rows = 3
columns = 3
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55
player = 1

board = np.zeros((rows, columns))

def lines():
    pygame.draw.line(screen, line, (200, 00), (200, 600), width)
    pygame.draw.line(screen, line, (400, 00), (400, 600), width)
    pygame.draw.line(screen, line, (00, 200), (600, 200), width)
    pygame.draw.line(screen, line, (00, 400), (600, 400), width)

def draw_figures():
    for row in range(rows):
        for col in range(columns):
            if board[row][col] == 1:
                pygame.draw.circle(screen, (150, 254, 198), (int(col * 200 + 100 ), int(row * 200 + 100)), circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, (150, 254, 198), (col * 200 + space, row * 200 + 200 - space), (col * 200 + 200 - space, row * 200 + space), cross_width)
                pygame.draw.line(screen, (150, 254, 198), (col * 200 + space, row * 200 + space), (col * 200 + 200 - space, row * 200 +  200 - space), cross_width)

def check_win(player):
    for col in range(columns):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical(col, player)
            return True

    for row in range(rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal(row, player)
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diagonal2(player)
        return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diagonal1(player)
        return True

    return False                            # if draw

def draw_horizontal(row, player):
    posY = row * 200 + 100
    pygame.draw.line(screen, (150, 160, 200), (15, posY), (585, posY), 15)

def draw_vertical(col, player):
    posX = col * 200 + 100
    pygame.draw.line(screen, (150, 160, 200), (posX, 15), (posX, 585), 15)

def draw_diagonal1(player):
    pygame.draw.line(screen, (150, 160, 200), (15, 585), (585, 15), 15)

def draw_diagonal2(player):
    pygame.draw.line(screen, (150, 160, 200), (15, 15), (585, 585), 15)

def restart():
    screen.fill((64, 45, 150))
    lines()
    player = 1
    for row in range(rows):
        for col in range(columns):
            board[row][col] = 0
 

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def board_full():
    for row in range(rows):
        for col in range(columns):
            if board[row][col] == 0:
                return False
    return True

lines()

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col ):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()

