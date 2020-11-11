import pygame

pygame.init()
win = pygame.display.set_mode((1024, 1024))

pygame.display.set_caption('Hero Of Stones - The Game')

walkLeft = [pygame.image.load('pygame_left_1.png'), pygame.image.load('pygame_left_2.png'), pygame.image.load('pygame_left_3.png'), pygame.image.load('pygame_left_4.png'), pygame.image.load('pygame_left_5.png'), pygame.image.load('pygame_left_6.png')]
walkRight = [pygame.image.load('pygame_right_1.png'), pygame.image.load('pygame_right_2.png'), pygame.image.load('pygame_right_3.png'), pygame.image.load('pygame_right_4.png'), pygame.image.load('pygame_right_5.png'), pygame.image.load('pygame_right_6.png')]

playerStand = pygame.image.load('idle.png')
playerJumpLeft = pygame.image.load('pygame_jump_left.png')
playerJumpRight = pygame.image.load('pygame_jump_right.png')
playerFallLeft = pygame.image.load('fall_left.png')
playerFallRight = pygame.image.load('fall_right.png')
stone = pygame.image.load('stone.png')
bg = pygame.image.load('pygame_bg.png')

clock = pygame.time.Clock()

x = 50
y = 570
height = 128
width = 96
speed = 5 

isJump = False
jumpCount = 10

left = False
right = False
up = False
falling = False
animCount = 0
lastMove = "right"

xstone = 100
ystone = 100
hstone = 100
wstone = 100


class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class stones():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = hstone
        self.width = wstone

    def drawstone(self, win):
        win.blit(stone, (x, y))
        

def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if up and lastMove == "right":
        win.blit(playerJumpRight, (x, y))
        animCount += 0
    elif up and lastMove == "left":
        win.blit(playerJumpLeft, (x, y))
        animCount += 0
    elif falling and lastMove == "left":
        win.blit(playerFallLeft, (x, y))
        animCount += 0
    elif falling and lastMove == "right":
        win.blit(playerFallRight, (x, y))
        animCount += 0    
    elif left and up == False:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right and up == False:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    elif up == False:
        win.blit(playerStand, (x, y))
        animCount = 0
    
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()

run = True
bullets = []
# stones = []
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 1024 and bullet.x > 0: 
            bullet.x += bullet.vel
        else: 
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if left == True or right == True:
        if keys[pygame.K_f]:
            if lastMove == "right":
                facing = 1
            else:
                facing = -1

            if len(bullets) < 5:
                bullets.append(snaryad(round(x + width // 2), round(y + height //2), 5, (255, 0, 0), facing))

    # if keys[pygame.K_f]:
    #     if lastMove == "right":
    #         facing = 1
    #     else:
    #         facing = -1

    #     if len(bullets) < 5:
    #          bullets.append(snaryad(round(x + width // 2), round(y + height //2), 5, (255, 0, 0), facing))
    
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] and x < 1024 - 100:
        x += speed
        left = False
        right = True 
        lastMove = "right"
    else:
        left = False
        right = False    
        animCount = 0
        
    if not(isJump): 
        # if keys[pygame.K_UP] and y > 5:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < 495 - 60:
        #     y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            up = True
            animCount = 0
    else:
        if jumpCount >=-10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2    
            else:
                y -= (jumpCount ** 2) / 2
                up = False
                falling = True
                
            jumpCount -= 1

        else: 
            jumpCount = 10
            isJump = False
            up = False
            falling = False

    # def drawstone(self, win):
    #     win.blit(stone, (x, y))

    drawWindow()

pygame.quit()