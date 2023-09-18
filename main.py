import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# Obtiene la información de la pantalla
screen_info = pygame.display.Info()
# Configura la pantalla para que tenga la misma resolución que la pantalla del monitor
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height-50))
# create the screen
# screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0 #vertical movement

#VAR VELOCITIES
player_speed = 2  # Ajusta la velocidad del jugador (mayor valor = más rápido)
enemy_speed = 1.5   # Ajusta la velocidad de los enemigos (mayor valor = más rápido)
bullet_speed = 8  # Ajusta la velocidad de las balas (mayor valor = más rápido)


# Enemy
enemyImgLoad = pygame.image.load('enemy2.png')
enemyImgLoad = pygame.transform.scale(enemyImgLoad, (100,100)) # Defined enemy size
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

#Enemy2
enemyImgLoad2 = pygame.image.load('enemy.png')
enemyImgLoad2 = pygame.transform.scale(enemyImgLoad2, (40,40))
enemyImg = []
enemyImg2 = []
enemy2X = []
enemy2Y = []
enemy2X_change = []
enemy2Y_change = []
num_of_enemies2 = 10

for i in range(num_of_enemies):
    enemyImg.append(enemyImgLoad)
    enemyX.append(random.randint(0, 730))
    enemyY.append(random.randint(50, 350)) #b: distance of enemies appear
    enemyX_change.append(1)
    enemyY_change.append(100)

for i in range(num_of_enemies2):
    enemyImg2.append(enemyImgLoad2)
    enemy2X.append(random.randint(0, 730))
    enemy2Y.append(random.randint(50, 350))  # b: distance of enemies appear
    enemy2X_change.append(1)
    enemy2Y_change.append(100)


# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (30,30))
bulletX = 0
bulletY = 480
bulletX_change = 5
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over_text, (600, 350))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def enemy2(x, y, i):
    screen.blit(enemyImg2[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x +18, y + 10)) #position bullet into player
    screen.blit(bulletImg, (x -20, y + 10))
    screen.blit(bulletImg, (x + 55 , y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 100:
        return True
    else:
        return False
def isCollision2(enemy2X, enemy2Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemy2X - bulletX, 2) + (math.pow(enemy2Y - bulletY, 2)))
    if distance < 40:
        return True
    else:
        return False

def isCollisionPlayer(enemyX, enemyY, playerX,playerY):
    distance = math.sqrt(math.pow(enemyX - playerX , 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 50:
        return True
    else:
        return False
# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -player_speed  # Ajusta la velocidad del jugador
                #playerX_change = -1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -player_speed  # Ajusta la velocidad del jugador

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = player_speed  # Ajusta la velocidad del jugador

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = player_speed # Ajusta la velocidad del jugador
                #playerX_change = 1
            if event.key == pygame.K_SPACE or event.key == pygame.K_KP0:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP or event.key == pygame.K_DOWN: #Stop movement when keyup
                playerX_change = 0
                playerY_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= screen_width-60:
        playerX = screen_width-60

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= screen_height - 60:
        playerY = screen_height - 60


    # Enemy Movement
    for i in range(num_of_enemies):
        # Game Over
        collision3 = isCollisionPlayer(enemyX[i], enemyY[i], playerX, playerY)
        if enemyY[i] > 450 or collision3:
            for j in range(num_of_enemies):

                enemyY[j] = 2000
                enemy2Y[j] = 2000
                if collision3:
                    explosionSound = mixer.Sound("explosion.wav")
                    explosionSound.play()
            game_over_text()
            break
        enemyX[i] += enemyX_change[i] * enemy_speed  # Ajusta la velocidad de los enemigos
        enemy2X[i] += enemy2X_change[i] * enemy_speed

        #enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemy2X[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
            enemy2X_change[i] = 1
            enemy2Y[i] += enemy2Y_change[i]
        elif enemyX[i] >= screen_width-60 or enemy2X[i] >= screen_width-60:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]
            enemy2X_change[i] = -1
            enemy2Y[i] += enemy2Y_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        collision2 = isCollision2(enemy2X[i], enemy2Y[i], bulletX, bulletY)

        if collision or collision2:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            if collision:
                score_value += 3 #for small enemy
            else:
                score_value += 1 #for bigger enemy

            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
            enemy2X[i] = random.randint(0, 736)
            enemy2Y[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
        enemy2(enemy2X[i], enemy2Y[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_speed  # Ajusta la velocidad de las balas
        #bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
pygame.quit()
