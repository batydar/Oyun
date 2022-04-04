import random
import math

import pygame

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

# Gun
gunX = playerX + 40
gunY = playerY

# Rainbow Gun
rGunX = playerX + 40
rGunY = playerY


# ammobx-ammo
ammoboxX = random.randint(0, 735)
ammoboxY = random.randint(50, 150)
ammoboxState = "ready"
# Ready = ready, falling = falling

# Enemy
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemys = 6
enemyHealth = []
enemyMaxhealth = 1
# Enemy Bullet
ebulletX = []
eBulletY = []
eBullet_state = "ready"

for i in range(number_of_enemys):
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(enemySpeed)
    enemyY_change.append(enemyFallSpeed)
    eBulletY.append(1000)
    ebulletX.append(1000)
    enemyHealth.append(1)

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
gameover = 0

# enemyTurret
turretTime = 0
turret_state = []
turretX = []
turretY = []
turretImg = []
turretBulletImg = []
bulletTime = []
turretBullet_state = []
turretBulletYchange = []
turretBulletX = []
turretBulletY = []

for i in range(6):
    turret_state.append("ready")
    turretX.append(random.randint(0, 735))
    turretY.append(random.randint(50, 150))
    turretImg.append(enemyTurretImg)
    bulletTime.append(0)
    turretBulletImg.append(bulletImg)
    turretBullet_state.append("ready")
    turretBulletYchange.append(3)
    turretBulletX.append(0)
    turretBulletY.append(0)


def enemyTurret(i):
    screen.blit(turretImg[i], (turretX[i], turretY[i]))


def GameOverDef():
    for j in range(number_of_enemys):
        enemyY[j] = 2000
    game_over_text()
    gameover = 1
    screen.fill("black")


def turretFire(i):
    global turretBullet_state
    turretBullet_state[i] = "fire"
    screen.blit(turretBulletImg[i], (turretX[i] + 16, turretY[i]))


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


def showTurretAmmo(i):
    screen.blit(turretBulletImg[i], (turretBulletX[i], turretBulletY[i]))


def fire_enemy_bullet(x, y):
    global e_bullet_state


def show_background(x, y):
    screen.blit(backgroundImg, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    if enemyHealth[i] == 3:
        screen.blit(enemyl3Img, (x, y))
    if enemyHealth[i] == 2:
        screen.blit(enemyl2Img, (x, y))
    if enemyHealth[i] == 1:
        screen.blit(enemyphoto, (x, y))


def show_gun(gunX, gunY):
    screen.blit(gunImg, (gunX, gunY))


def falling_coffe(x, y):
    screen.blit(coffeImg, (x, y))


def redline(x, y):
    screen.blit(redlineImg, (x, y))


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


def isCollision3(turretX, turretY, bulletX, bulletY):
    distance = math.sqrt(math.pow(turretX - bulletX, 2) + (math.pow(turretY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def isCollision4(TurretBulletX, TurretBulletY, gunX, gunY):
    distance = math.sqrt(math.pow(gunX - TurretBulletX, 2) + (math.pow(gunY - TurretBulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

guntype = "normal" # normal X, r-gun O, shotgun ?, uzi ?
time = 0
activation = []
for i in range(0, 10):
    activation.append(0)

# GameLoop
running = True


def play():
    global turretTime, guntype, rgunX, rGunY, turretBulletY, turretBulletX, turretBulletYchange, turretY, turretX, turret_state, time, enemyFallSpeed, activation, playerX, playerY, gunX, gunY, running, pressedB, ammo, playerX_change, playerSpeed, bullet_state, bulletX, bulletY, enemySpeed, score_value, enemyMaxhealth, bulletX_change, bulletY_change, ammoboxState, gameover, ammoboxX, ammoboxY, pammo
    while running:
        # RGB Red Green Blue
        screen.fill((0, 0, 0))

        gunX = playerX
        gunY = playerY
        rGunX = playerX
        rgunY = playerY

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
                    if guntype == "normal":
                        if bullet_state == "ready":
                            if ammo > 0:
                                bulletX = gunX - 9
                                fire_bullet(bulletX, gunY)
                                bulletY = gunY
                                ammo -= 1
                    if guntype == "r-gun":
                        print("r-gun")

                if event.key == pygame.K_1:
                    guntype = "normal"
                if event.key == pygame.K_2:
                    guntype = "r-gun"



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
            elif enemyX[i] > 736:
                enemyX_change[i] = -enemySpeed

            enemyY[i] += enemyY_change[i]
            if enemyY[i] > 430:
                GameOverDef()
                break

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                score_value += 1
                ammo += 1
                bullet_state = "ready"
                enemyHealth[i] -= 1
                if enemyHealth[i] < 1:
                    enemyX[i] = random.randint(0, 735)
                    enemyY[i] = random.randint(50, 150)
                    enemyHealth[i] = enemyMaxhealth

            enemy(enemyX[i], enemyY[i], i)

        turretTime += random.randint(0, 9)

        # Turret
        if gameover != 1:
            for i in range(6):
                if turretTime >= 12000:
                    if turret_state[i] == "ready":
                        turret_state[i] = "placed"
                        turretTime = 0

                if turret_state[i] == "placed":
                    enemyTurret(i)
                    bulletTime[i] += random.randint(0, 9)

                collision3 = isCollision3(turretX[i], turretY[i], bulletX, bulletY)
                if collision3:
                    bulletY = 480
                    score_value += 2
                    ammo += 1
                    bullet_state = "ready"
                    turretX[i] = random.randint(0, 735)
                    turretY[i] = random.randint(50, 150)
                    turret_state[i] = "ready"


                if bulletTime[i] >= 3000:
                    turretBulletX[i] = turretX[i] + 16
                    if turret_state[i] == "placed":
                        if turretBullet_state[i] == "ready":
                            turretBulletY[i] = turretY[i]
                            bulletTime[i] = 1500
                            turretFire(i)

                if turretBulletY[i]>1000:
                    turretBullet_state[i]="ready"

                if turretBullet_state[i] == "fire":
                    turretBulletY[i] += turretBulletYchange[i]
                    showTurretAmmo(i)
                    collision4 = isCollision4(turretBulletX[i], turretBulletY[i], gunX, gunY)
                    if collision4:
                        GameOverDef()
                        gameover=1



        # Bullet Movement
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        if ammoboxState == "falling":
            if gameover == 0:
                falling_coffe(ammoboxX, ammoboxY)
                ammoboxY -= ammoboxY_change

        collision2 = isCollision2(gunX, gunY, ammoboxX, ammoboxY)
        if collision2:
            ammoboxState = "ready"
            ammo += pammo
            time = 0
            ammoboxY = -100

        if ammoboxY > 680:
            if gameover == 0:
                ammoboxY = -100
                ammoboxState = "ready"
                time = 0

        if bulletY <= -30:
            if gameover == 0:
                bulletY = 480
                bullet_state = "ready"

        if time >= eventtime:
            if ammoboxState != "falling":
                time = 0
                ammoboxState = "falling"
                ammoboxX = random.randint(0, 735)
                ammoboxY = -30

        if score_value > 10:
            if activation[0] == 0:
                pammo = 7
                bulletY_change = 6
                activation[0] = 1

        if score_value > 20:
            if activation[1] == 0:
                enemyFallSpeed += 0.01
                activation[1] = 1

        if score_value > 50:
            if activation[2] == 0:
                enemyHealth.clear()
                activation[2] = 1
                for i in range(number_of_enemys):
                    enemyMaxhealth = 2
                    enemyHealth.append(enemyMaxhealth)

        if score_value > 60:
            if activation[3] == 0:
                activation[3] = 1
                playerSpeed = 0.6
                pammo = 8
                enemySpeed = 0.3

        if score_value > 70:
            if activation[4] == 0:
                activation[4] = 1
                playerSpeed = 0.7
                enemySpeed = 0.35
                enemyFallSpeed = 0.1

        if score_value > 100:
            if activation[5] == 0:
                enemyHealth.clear()
                activation[5] = 1
                for i in range(number_of_enemys):
                    enemyMaxhealth = 3
                    enemyHealth.append(enemyMaxhealth)

        if score_value > 150:
            if activation[6] == 0:
                enemyHealth.clear()
                activation[6] = 1
                for i in range(number_of_enemys):
                    enemyMaxhealth = 3
                    enemyHealth.append(enemyMaxhealth)

        if gameover != 1:
            redline(0, 470)
            player(playerX, playerY)
            show_gun(gunX, gunY)

        else:
            game_over_text()

        show_score(text1X, text1Y)
        show_ammo(text2X, text2Y)
        pygame.display.update()
        time += 1


def main_menu():
    pygame.display.set_caption("Menu")
    while True:
        show_background(0, 0)


play()
