import pygame
import random
from network import Network
from circle import Cell


windowWidth = 750
windowHeight = 750
window = pygame.display.set_mode((windowWidth, windowHeight))
clientNumber = 0



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
        pygame.draw.circle(window, (0, 0, 255), (500, 200), 20)
        pygame.draw.circle(window, (0, 0, 255), (370, 100), 20)
        pygame.draw.circle(window, (0, 0, 255), (640, 300), 20)
        pygame.draw.circle(window, (0, 0, 255), (500, 400), 20)
        pygame.draw.circle(window, (0, 0, 255), (700, 450), 20)
        pygame.draw.circle(window, (0, 0, 255), (500, 700), 20)
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

def createCells():
    howManyCells = range(10)
    thislist = []
    #for cell in howManyCells
    thislist.append(Cell(100,100))

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
    p = Player(startPos[0], startPos[1],(0, 255, 0), 100)
    p2 = Player(0, 0,(255, 0, 0), 100,)
    clock = pygame.time.Clock()

    while run:
        clock.tick(120)
        p2Pos = read_pos(myNetwork.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(window, p, p2)
main()