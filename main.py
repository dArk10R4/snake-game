# importing libraries
import pygame
import time
import random
import math
snake_speed = 15

# Window size0
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]
snake_position1 = [80, 30]
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
snake_body1 = [[60, 10],
              [50, 10],
              [30, 10],
              [30, 10]
              ]

# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
direction1 = 'LEFT'
change_to1 = direction1
# initial score
score = 0
score1 = 0

# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_surface1 = score_font.render('                     Score1 : ' + str(score1), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    score_rect1 = score_surface1.get_rect()
    # displaying text
    game_window.blit(score_surface, score_rect)
    game_window.blit(score_surface1, score_rect1)


# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn

    game_over_surface = my_font.render(
        'Score1 is : ' + str(score) + '  Score2 is' + str(score1), True, red)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Main Function
while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP :
                change_to = 'UP'
            if event.key == pygame.K_DOWN :
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT :
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT :
                change_to = 'RIGHT'
            if  event.key == pygame.K_w:
                change_to1 = 'UP'
            if  event.key == pygame.K_s:
                change_to1 = 'DOWN'
            if  event.key == pygame.K_a:
                change_to1 = 'LEFT'
            if  event.key == pygame.K_d:
                change_to1 = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    ##
    if change_to1 == 'UP' and direction1 != 'DOWN':
        direction1 = 'UP'
    if change_to1 == 'DOWN' and direction1 != 'UP':
        direction1 = 'DOWN'
    if change_to1 == 'LEFT' and direction1 != 'RIGHT':
        direction1 = 'LEFT'
    if change_to1 == 'RIGHT' and direction1 != 'LEFT':
        direction1 = 'RIGHT'


    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    ######
    if direction1 == 'UP':
        snake_position1[1] -= 10
    if direction1 == 'DOWN':
        snake_position1[1] += 10
    if direction1 == 'LEFT':
        snake_position1[0] -= 10
    if direction1 == 'RIGHT':
        snake_position1[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    snake_body1.insert(0, list(snake_position1))
    if(snake_position[0]>0):
        snake_position[0] = snake_position[0]%window_x
    if (snake_position1[0] > 0):
        snake_position1[0] = snake_position1[0] % window_x
    if (snake_position[1] > 0):
        snake_position[1] = snake_position[1] % window_y
    if (snake_position1[1] > 0):
        snake_position1[1] = snake_position1[1] % window_y
    if(snake_position[0]<0):
        snake_position[0] = window_x-(-snake_position[0])%window_x
    if (snake_position1[0] < 0):
        snake_position1[0] = window_x-(-snake_position1[0])% window_x
    if (snake_position[1] < 0):
        snake_position[1] = window_y - (-snake_position[1]) % window_y
    if (snake_position1[1] < 0):
        snake_position1[1] = window_y - (-snake_position1[1]) % window_y


    if (snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]) or (snake_position1[0] == fruit_position[0] and snake_position1[1] == fruit_position[1]):

        fruit_spawn = False
        if (snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]):
            snake_body1.pop()
            score += 10
        else:
            score1 += 10
            snake_body.pop()
    else:
        snake_body.pop()
        snake_body1.pop()


    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        if(pos[0]>window_x):
            pos[0] = pos[0]%window_x
        if (pos[1] > window_y):
            pos[1] = pos[1] % window_y
        if (pos[0] <0):
            pos[0] = window_x - (-pos[0])%window_x
        if (pos[1] < 0):
            pos[1] = window_y - (-pos[1]) % window_y
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    for pos in snake_body1:
        if (pos[0] > window_x):
            pos[0] = pos[0] % window_x
        if (pos[1] > window_y):
            pos[1] = pos[1] % window_y
        if (pos[0] <0):
            pos[0] = window_x - (-pos[0])%window_x
        if (pos[1] < 0):
            pos[1] = window_y - (-pos[1]) % window_y
        pygame.draw.rect(game_window, blue,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    # if snake_position[0] < 0 or snake_position[0] > window_x - 10:
    #     game_over()
    # if snake_position[1] < 0 or snake_position[1] > window_y - 10:
    #     game_over()
    # if snake_position1[0] < 0 or snake_position1[0] > window_x - 10:
    #     game_over()
    # if snake_position1[1] < 0 or snake_position1[1] > window_y - 10:
    #     game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    for block in snake_body1[1:]:
        if snake_position1[0] == block[0] and snake_position1[1] == block[1]:
            game_over()
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
