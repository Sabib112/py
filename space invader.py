import math
import random
import pygame

SCREEN_WIDTH= 800
SCREEN_HEIGHT = 500
PLAYER_START_X= 370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X= 5
ENEMY_SPEED_Y= 40
BULLET_SPEED= 10
COLLISION_DISTANCE= 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("bg.png")


pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


playerimg = pygame.image.load("player.png")
playerX= PLAYER_START_X
playerY= PLAYER_START_Y
playerX_change= 0

enemyimg= []
enemyX= []
enemyY= []
enemyX_change= []
enemyY_change= []
number_of_enemies= 6

for i in range(number_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH-64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletimg= pygame.image.load("bullet.png")
bulletX= 0
bulletY= PLAYER_START_Y
bulletY_change= 0
bulletstate= "ready"  

score=0
font= pygame.font.Font("freesansbold.ttf", 32)
textX= 10
textY= 10

over_font= pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    score= font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text= over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,200,250)


def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def fire_bullet(x, y):
    global bulletstate
    bulletstate= "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

