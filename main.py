# pong game 0.3
import pygame
import sys
import random
# initialize pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
# making the screen
screen_width = 1530
screen_height = 810
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("P0NG")
# shapes that are empty rectangles without pygame.draw
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
bg_color = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.SysFont(None, 64)
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    # increments the position of the ball with +ve and -ve values
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # -ve speed induces backwards movement
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        winlose()
    if ball.right >= screen_width:
        opponent_score += 1
        winlose()
    if ball.colliderect(player) and ball_speed_x > 0:
        ball_speed_x *= -1
    if ball.colliderect(opponent) and ball_speed_x < 0:
        ball_speed_x *= -1
def player_animation():
    player.y += player_speed
    opponent.y += opponent_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
def winlose():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))
# the base speed of the ball
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
# display text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# players
player_speed = 0
opponent_speed = 0
# game loop
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('Main Menu', font, (255, 255, 255), screen, 647, 810/2)
        draw_text('Pong - By R9', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(665, 505, 200, 50)
        button_2 = pygame.Rect(665, 605, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (0, 0, 0), button_1)
        pygame.draw.rect(screen, (0, 0, 0), button_2)
        draw_text('Start', font, (255, 255, 255), screen, 665, 505)
        draw_text('Options', font, (255, 255, 255), screen, 665, 605)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
def game():
    global player_speed
    global opponent_speed
    while True:
        # input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7
            # player 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    opponent_speed += 7
                if event.key == pygame.K_w:
                    opponent_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    opponent_speed -= 7
                if event.key == pygame.K_w:
                    opponent_speed += 7
        ball_animation()
        player_animation()
        # objects
        screen.fill(bg_color)
        pygame.draw.rect(screen, white, player)
        pygame.draw.rect(screen, white, opponent)
        pygame.draw.ellipse(screen, white, ball)
        pygame.draw.aaline(screen, white, (screen_width/2, 0), (screen_width/2, screen_height))
        # aaline stands for anti-aliasing line
        # text
        player_text = game_font.render(f"{player_score}", False, white)
        # the false is for anti-aliasing
        opponent_text = game_font.render(f"{opponent_score}", False, white)
        screen.blit(player_text, (1500, 20))
        # this function says take the background surface and draw it onto the screen and position it at (x,y)
        screen.blit(opponent_text, (15, 20))
        # updates the game window
        pygame.display.flip()
        clock.tick(60)
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()