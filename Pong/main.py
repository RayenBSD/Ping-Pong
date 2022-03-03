import pygame as pg
import random as rand
from pygame import mixer
#Ping Pong Game

class Player:
    WHITE = (255, 255, 255)
    #Constructor
    def __init__(self, posX, posY, width, height):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.score = 0
    #setter
    def set_posX(self, step):
        self.posX += step
    def set_posY(self, step):
        self.posY += step
    def set_score (self):
        self.score += 1
    #getter
    def get_posX(self):
        return self.posX
    def get_posY(self):
        return self.posY
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height 
    def get_score(self):
        return self.score

#set pygame
pg.init()

#back ground music
mixer.music.load("PyGame/Pong/is-trap-SBA-300514651-preview.mp3")
mixer.music.play(-1)

#set screen
screenX, screenY = 700, 700
screen = pg.display.set_mode((screenX, screenY))
pg.display.set_caption("Ping Pong")
icon = pg.image.load("PyGame/Pong/PingPong.png")
pg.display.set_icon(icon)

width, height = 20, 100
#Player1
player1X, player1Y = 50, 350 
player1 = Player(player1X, player1Y, width, height)

#Player2
player2X, player2Y = 600, 350
player2 = Player(player2X, player2Y, width, height)

#ball mave
X = rand.choice([-10, 10])
Y = rand.choice([-10, 10])
ballX, ballY = 350, 350

def move():
    global player1, player2, screenY, height
    step = 20

    keys = pg.key.get_pressed()

    if keys[pg.K_z] and player1.get_posY() - step >= 0:
        player1.set_posY(-step)
    if keys[pg.K_s] and player1.get_posY() + step + height <= screenY:
        player1.set_posY(step)
    if keys[pg.K_UP] and player2.get_posY() - step >= 0:
        player2.set_posY(-step)
    if keys[pg.K_DOWN] and player2.get_posY() + step + height <= screenY:
        player2.set_posY(step)

def ballMove():
    global ballX, ballY, player1, player2, width, height, X, Y, screenY

    step = 10
    ballX += X
    ballY += Y

    #edge
    if ballY - step <= 0:
        Y = step
    if ballY + step >= screenY:
        Y = step * -1
    
    touch = mixer.Sound("PyGame/Pong/ping-pong-paddle-hitting-ball-2-SBA-300283145-preview.mp3")
    #player1
    if (player1.get_posX() + width < ballX <= player1.get_posX() + width + 10) and (ballY + int(step/2) > player1.get_posY() and ballY + int(step/2) < player1.get_posY() + height):
        touch.play()
        X = step
        Y = rand.choice([-10, 10])
        step += 1
    #player2
    if (player2.get_posX() > ballX + step >= player2.get_posX() - 10) and (ballY + int(step/2) > player2.get_posY() and ballY + int(step/2) < player2.get_posY() + height):
        touch.play()
        X = step * -1
        Y = rand.choice([-10, 10])
        step += 1
    #win player1
    if (ballX + step >= 700):
        player1.set_score()
        ballX, ballY = 350, 350
        X = rand.choice([-10, 10])
        Y = rand.choice([-10, 10])        

    #win player2
    if (ballX <= 0):
        player2.set_score()
        ballX, ballY = 350, 350
        X = rand.choice([-10, 10])
        Y = rand.choice([-10, 10])

def redraw ():
    font = pg.font.Font("freesansbold.ttf", 32)
    player1_score = font.render(f"Score1: {str(int(player1.get_score()))}", True, (255, 255, 255))
    screen.blit(player1_score, (50, 650))

    player2_score = font.render(f"Score2: {str(int(player2.get_score()))}", True, (255, 255, 255))
    screen.blit(player2_score, (500, 650))

def main():
    global player1, player2, screen,ballX, ballY
    BLACK = (0, 0, 0)

    while True:
        #pg.time.delay(50)
        time = pg.time.Clock()
        time.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
        pg.draw.rect(screen, player1.WHITE, (
            player1.get_posX(), player1.get_posY(), player1.get_width(), player1.get_height()
            )
        )
        pg.draw.rect(screen, player2.WHITE, (
            player2.get_posX(), player2.get_posY(), player2.get_width(), player2.get_height()
            )
        )
        pg.display.update()
        screen.fill(BLACK)
        #ball
        center, radius = (ballX, ballY), 10
        pg.draw.circle(screen, (255, 255, 255), center, radius)
        move()
        ballMove()
        redraw()

if __name__ == "__main__":  main()