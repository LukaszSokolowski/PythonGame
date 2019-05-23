import pygame
import random
from network import Network
from circle import Cell
from circle import CellPosition
import math
pygame.font.init()

windowWidth = 750
windowHeight = 750
window = pygame.display.set_mode((windowWidth, windowHeight))
clientNumber = 0
positionCell = []

font = pygame.font.SysFont("comicsans", 80)
text3 = font.render(" ", 1, (255, 0, 0), True)

positionCell.append(CellPosition(587,154))
positionCell.append(CellPosition(618,241))
positionCell.append(CellPosition(157,710))
positionCell.append(CellPosition(234,409))
positionCell.append(CellPosition(442,221))
positionCell.append(CellPosition(842,523))
positionCell.append(CellPosition(356,180))
positionCell.append(CellPosition(300,251))
positionCell.append(CellPosition(223,600))
positionCell.append(CellPosition(422,555))
positionCell.append(CellPosition(19,335))
positionCell.append(CellPosition(50,495))
positionCell.append(CellPosition(37,190))
positionCell.append(CellPosition(699,694))
positionCell.append(CellPosition(313,165))
positionCell.append(CellPosition(610,416))
positionCell.append(CellPosition(281,120))

allCellsList = []

for i in range(len(positionCell)):
    allCellsList.append(Cell(positionCell[i].x, positionCell[i].y, 10, (0, 0, 255), 1))

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
        pygame.draw.rect(window, (0, 0, 255), (0, 0, 750, 50))
        window.blit(text3, (350, 350))
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

def winner():
    print("Wygrał")

def main():
    run = True
    myNetwork = Network()
    startPos = read_pos(myNetwork.getPos())
    p = Player(startPos[0],startPos[1],(0, 255, 0), 25)
    p2 = Player(0, 0,(255, 0, 0), 25)
    clock = pygame.time.Clock()
    wyjscieZPetli = True
    score = 0
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

        window.blit(text, (5,0))
        window.blit(text2, (660,0))

        pygame.display.flip()

        for index in allCellsList:
            print(index)
            if  math.fabs(math.sqrt(math.pow((index.x - p.x), 2) + math.pow((index.y - p.y), 2))) < math.fabs(p.radius - index.r):
                score = score + 10
                p.radius = p.radius + 1
                allCellsList.remove(index)

            if  math.fabs(math.sqrt(math.pow((index.x - p2.x), 2) + math.pow((index.y - p2.y), 2))) < math.fabs(p2.radius - index.r):
                enemyScore = enemyScore + 10
                p2.radius = p2.radius + 1
                allCellsList.remove(index)

            if math.fabs(math.sqrt(math.pow((p.x - p2.x), 2) + math.pow((p.y - p2.y), 2))) < math.fabs(p2.radius - p.radius):
                if score > enemyScore:
                    text3 = font.render("Wygrałeś", 1, (255, 0, 0), True)
                    window.blit(text3,(350,350))
                    pygame.display.flip()
                if score < enemyScore:
                    text3 = font.render("Przegrałeś", 1, (255, 0, 0), True)
                    window.blit(text3, (350, 350))
                    pygame.display.flip()
                if wyjscieZPetli:
                    if score > enemyScore:
                        p.vel = 0
                        p2.color = p.color
                        p.radius = p.radius + p2.radius
                        wyjscieZPetli = False
                        text = font.render("WIN", 1, (255, 0, 0), True)
                        window.blit(text, (5, 0))
                        pygame.display.flip()

                    if score < enemyScore:
                        p2.vel = 0
                        p.color = p2.color
                        p2.radius = p.radius + p2.radius
                        wyjscieZPetli = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(window, p, p2)
main()
