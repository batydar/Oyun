import pygame
import random
import math
from visualizer import *
from variables import *

# intilaze the pygmae
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Game")
pygame.display.set_icon(icon)

# Buttons
pressedB = 0

# Player
playerX = 370
playerY = 480
playerX_change = 0

# Keyboard

# Kahve-ammo
coffeX = random.randint(0, 735)
coffeY = random.randint(50, 150)
coffeState = "ready"
# Ready = ready, falling = falling

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemys = 6

for i in range(number_of_enemys):
    enemyImg.append(enemyphoto)
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(enemySpeed)
    enemyY_change.append(enemyFallSpeed)

# Bullet
bulletX = 0
bulletY = 480
bulletX_change = 0


# Ready= You cant see the bullet
# Fire= The bullet is moving
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

text1X = 10
text1Y = 10

# Ammo
text2X = 10
text2Y = 50

# Game Over
overfont = pygame.font.Font('freesansbold.ttf', 64)
gameover=0

def game_over_text():
    gameover = overfont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover, (200, 250))


def show_score(x, y):
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_ammo(x, y):
    mag = font.render(f"Ammo : {ammo}", True, (255, 255, 255))
    screen.blit(mag, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def keyboard():
    screen.blit(keyboardImg, (playerX, playerY - 40))


def falling_coffe(x, y):
    screen.blit(coffeImg, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def isCollision2(playerX, playerY, coffeX, coffeY):
    distance = math.sqrt(math.pow(playerX - coffeX, 2) + math.pow(playerY - coffeY, 2))
    if distance < 27:
        return True
    else:
        return False


time = 0

# GameLoop
running = True
while running:
    # RGB Red Green Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                pressedB += 1
                playerX_change = -playerSpeed
            if event.key == pygame.K_RIGHT:
                playerX_change = playerSpeed
                pressedB += 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    if ammo > 0:
                        fire_bullet(playerX, playerY)
                        bulletX = playerX
                        bulletY = playerY
                        ammo -= 1

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pressedB -= 1

                if event.key == pygame.K_LEFT:
                    playerX_change = +playerSpeed
                if event.key == pygame.K_RIGHT:
                    playerX_change = -playerSpeed
                if pressedB == 0:
                    playerX_change = 0

    # Checking Boundries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    # Enemy  Movement
    for i in range(number_of_enemys):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = enemySpeed
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 736:
            enemyX_change[i] = -enemySpeed
            enemyY[i] += enemyY_change[i]

        if enemyY[i] > 400:
            for j in range(number_of_enemys):
                enemyY[j]=2000
            game_over_text()
            gameover=1
            break

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            score_value += 1
            ammo += 1
            bullet_state = "ready"
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if coffeState == "falling":
        if gameover == 0:
            falling_coffe(coffeX, coffeY)
            coffeY -= coffeY_change

    collision2 = isCollision2(playerX, playerY, coffeX, coffeY)
    if collision2:
        coffeState = "ready"
        ammo += pammo
        time = 0
        coffeY = -100

    if coffeY > 680:
        if gameover == 0:
            coffeY = -100
            coffeState = "ready"
            time = 0

    if bulletY <= -30:
        if gameover == 0:
            bulletY = 480
            bullet_state = "ready"

    if time >= eventtime:
        if coffeState != "falling":
            time = 0
            coffeState = "falling"
            coffeX = random.randint(0, 735)
            coffeY = -30

    player(playerX, playerY)
    keyboard()
    show_score(text1X, text1Y)
    show_ammo(text2X, text2Y)
    pygame.display.update()
    time += 1
