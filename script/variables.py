file = open("Variables.txt", "r")

v1 = file.readline()
v1 = v1.split("=")
coffeY_change = float(v1[1])

v1 = file.readline()
v1 = v1.split("=")
enemySpeed = float(v1[1])

v1 = file.readline()
v1 = v1.split("=")
enemyFallSpeed = float(v1[1])

v1 = file.readline()
v1 = v1.split("=")
bulletSpeed = float(v1[1])

v1 = file.readline()
v1 = v1.split("=")
bulletY_change = float(v1[1])

v1 = file.readline()
v1 = v1.split("=")
ammo = int(v1[1])

v1 = file.readline()
v1 = v1.split("=")
pammo = int(v1[1])

v1 = file.readline()
v1 = v1.split("=")
eventtime = float(v1[1])

v1 = file.readline()
v1 = v1.split("=")
playerSpeed = float(v1[1])

