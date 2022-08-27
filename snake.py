from cmath import rect
from email.mime import image
import os
from tkinter import CENTER
from turtle import position
import pygame as pg

SIZE = (500, 500)
CENTER = (SIZE[0]/2, SIZE[1]/2)

class Food():
    
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

        self.width = 10
        self.height = 10
        self.image = pg.Surface([self.width, self.height])
        self.image = self.image.convert()
        self.image.fill((255,000,000))
        self.rect = self.image.get_rect()
        


class SnakePart(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.xspeed = 0
        self.yspeed = 0

        self.width = 10
        self.height = 10
        self.image = pg.Surface([self.width, self.height])
        self.image = self.image.convert()
        self.image.fill((200,200,200))
        self.rect = self.image.get_rect()

class Snake():

    def __init__(self):
        # create snake head
        self.head = SnakePart()
        self.head.rect.topleft = CENTER

        # create array used to store snake head and tail positions
        self.snakeElements = []
        self.snakeElements.append(self.head)

    def draw(self, screen):
        allsprites = pg.sprite.RenderPlain(self.snakeElements)
        allsprites.draw(screen)

    def grow(self, food):
        newPart = SnakePart()
        newPart.rect.topleft = food.rect.topleft
        self.snakeElements.append(newPart)



def main():

    # Initialize
    pg.init()
    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption("Snake")
    pg.mouse.set_visible(False)

    # Create The Backgound
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Display The Background
    screen.blit(background, (0, 0))
    pg.display.flip()

    # Prepare Game Objects
    snake = Snake();
    clock = pg.time.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            if event.type == pg.K_w:
                snake.yspeed = -10
            if event.type == pg.K_a:
                snake.xspeed = -10
            if event.type == pg.K_s:
                snake.yspeed = +10
            if event.type == pg.K_d:
                snake.yspeed = +10


        # Draw Everything
        screen.blit(background, (0, 0))
        snake.draw(screen)
        pg.display.flip()

    pg.quit()



if __name__ == "__main__":
    main()