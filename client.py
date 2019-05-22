import pygame
import random
from network import Network
from circle import Cell
import math
pygame.font.init()

windowWidth = 750
windowHeight = 750
window = pygame.display.set_mode((windowWidth, windowHeight))
clientNumber = 0



allCellsList = []
allCellsList.append(Cell(500, 100, 10, (0, 0, 255), 1))
allCellsList.append(Cell(700, 200, 10, (0, 0, 255), 2))
allCellsList.append(Cell(700, 500, 10, (0, 0, 255), 3))
allCellsList.append(Cell(500, 200, 10, (0, 0, 255), 4))
allCellsList.append(Cell(200, 200, 10, (0, 0, 255), 5))

#score = 0
#enemyScore = 0

class Player():
    def __init__(self, x, y, color,radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.circle = (x, y)
        self.vel = 3

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.circle, self.radius)
        createCells(window)
        pygame.display.flip()
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.circle = (self.x, self.y)

def createCells(win):

    for i in allCellsList:

        pygame.draw.circle(win, (0,0,255), i.position, i.r)

    pygame.display.flip()


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win,player, player2):
    win.fill((128, 128, 128))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    myNetwork = Network()
    startPos = read_pos(myNetwork.getPos())
    p = Player(startPos[0],startPos[1],(0, 255, 0), 25)
    p2 = Player(0, 0,(255, 0, 0), 25)
    clock = pygame.time.Clock()
    #global score
    score = 0
    #global enemyScore
    enemyScore = 0

    while run:
        clock.tick(120)
        p2Pos = read_pos(myNetwork.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        createCells(window)

        font = pygame.font.SysFont("comicsans", 80)
        text = font.render(str(score), 1, (255, 0, 0), True)
        text2 = font.render(str(enemyScore), 1, (255, 0, 0), True)

        window.blit(text, (300,300))
        window.blit(text2, (100,100))

        pygame.display.flip()

        for index in allCellsList:
            print(index)
            if  math.fabs(math.sqrt(math.pow((index.x - p.x), 2) + math.pow((index.y - p.y), 2))) < math.fabs(p.radius - index.r):
                print("jest zloto")

                score = score + 10
                allCellsList.remove(index)
                print("Player1 %s", score)

            if  math.fabs(math.sqrt(math.pow((index.x - p2.x), 2) + math.pow((index.y - p2.y), 2))) < math.fabs(p2.radius - index.r):
                print("jest zloto")
                enemyScore = enemyScore + 10
                allCellsList.remove(index)
                print("Player2 %s", enemyScore)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(window, p, p2)

main()