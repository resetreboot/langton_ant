#! /usr/bin/env python3

import pygame
from pygame.locals import *
from pygame.draw import rect


CELL_SIZE = 7


class Ant:
    def __init__(self, size=128):
        self.x = int(size/2)
        self.y = int(size/2)
        self.angle = 0
        self.size = size

    def calculate_step(self, point):
        if point == 0:
            self.angle += 1

        else:
            self.angle -= 1

        self.angle = self.angle % 4

        if self.angle == 0:
            self.y -= 1

        if self.angle == 1:
            self.x += 1

        if self.angle == 2:
            self.y += 1

        if self.angle == 3:
            self.x -= 1

        self.x = self.x % self.size
        self.y = self.y % self.size

        if point==0:
            return 1

        else:
            return 0


class Board:
    def __init__(self, ant, size=128):
        self.size = size
        self.board = [0 for x in range(0, size * size)]
        self.ant = ant

    def draw(self, surface):
        count = 0
        for elem in self.board:
            if elem == 0:
                color = (0, 0, 0)

            else:
                color = (255, 255, 255)

            rect(surface, color, ((count % self.size) * CELL_SIZE, (int(count/self.size)) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            count += 1

        rect(surface, (255, 0, 0), (ant.x * CELL_SIZE, ant.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def step(self):
        pointer = (self.ant.y * self.size) + self.ant.x
        point = self.board[pointer]
        value = self.ant.calculate_step(point)
        self.board[pointer] = value


if __name__ == "__main__":
    pygame.init()
    board_size = 128
    screen = pygame.display.set_mode((board_size * CELL_SIZE, board_size * CELL_SIZE))
    pygame.display.set_caption("Langton Ant")

    ant = Ant(board_size)

    board = Board(ant, board_size)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        board.step()

        background.lock()

        board.draw(background)

        background.unlock()

        screen.blit(background, (0, 0))
        pygame.display.flip()
