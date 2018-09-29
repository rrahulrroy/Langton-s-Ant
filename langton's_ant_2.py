import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024, 768), 0, 0)
myfont = pygame.font.SysFont("monospace", 36)
Matrix = [[(0) for x in range(96)] for x in range(128)]
clock = pygame.time.Clock()
FPS = 60
playtime = 0.0
formiga = []
formiga.append(50)
formiga.append(50)
formiga.append(1)
inte = 0;
while 1:
    background = pygame.Surface((screen.get_size()))
    background.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            a.close()
            pygame.quit()
            sys.exit()

    milliseconds = clock.tick(FPS)
    seconds = milliseconds / 1000.0
    playtime += milliseconds / 1000.0

    screen.lock()

    for i in range(96):
        for j in range(128):
            if Matrix[j][i] == 0:
                pygame.draw.rect(background, (255, 255, 255), Rect((j * 8, i * 8), (8, 8)))
            else:
                pygame.draw.rect(background, (0, 0, 0), Rect((j * 8, i * 8), (8, 8)))

    i = 128
    while i != 0:
        pygame.draw.line(background, (92, 51, 23), (i * 8, 0), (i * 8, 768))
        i = i - 1

    i = 96
    while i != 0:
        pygame.draw.line(background, (92, 51, 23), (0, i * 8), (1024, i * 8))
        i = i - 1

    pygame.draw.rect(background, (92, 0, 92), Rect((formiga[1] * 8, formiga[0] * 8), (8, 8)))

    if (Matrix[formiga[1]][formiga[0]] == 0 and playtime >= 0.01):
        Matrix[formiga[1]][formiga[0]] = 1
        formiga[2] = (formiga[2] + 1) % 4
        if formiga[2] == 0:
            formiga[0] -= 1
        if formiga[2] == 1:
            formiga[1] += 1
        if formiga[2] == 2:
            formiga[0] += 1
        if formiga[2] == 3:
            formiga[1] -= 1
        pygame.draw.rect(background, (92, 0, 92), Rect((formiga[1] * 8, formiga[0] * 8), (8, 8)))
        playtime = 0.0
        inte += 1

    if (Matrix[formiga[1]][formiga[0]] == 1 and playtime >= 0.01):
        Matrix[formiga[1]][formiga[0]] = 0
        formiga[2] = (formiga[2] - 1) % 4
        if formiga[2] == 0:
            formiga[0] -= 1
        if formiga[2] == 1:
            formiga[1] += 1
        if formiga[2] == 2:
            formiga[0] += 1
        if formiga[2] == 3:
            formiga[1] -= 1
        pygame.draw.rect(background, (92, 0, 92), Rect((formiga[1] * 8, formiga[0] * 8), (8, 8)))
        playtime = 0.0
        inte += 1
    strings = str(inte)
    label = myfont.render(strings, 1, (0, 0, 0))

    screen.unlock()
    screen.blit(background, (0, 0))
    screen.blit(label, (0, 0))
    pygame.display.update()