from cmath import rect
from email.mime import image
import os
from tkinter import CENTER
from turtle import position
import pygame as pg

SIZE = (500, 500)
CENTER = (SIZE[0]/2, SIZE[1]/2)

class Snake(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.width = 10
        self.height = 10
        self.image = pg.Surface([self.width, self.height])
        self.image = self.image.convert()
        self.image.fill((200,200,200))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = CENTER

        # create array used to store snake head and tail positions
        self.positions = []
        self.positions.append((self.rect.x, self.rect.y))
        print(self.positions)
    
    def draw(self):
        for pos in self.positions:
            return



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
    allsprites = pg.sprite.RenderPlain((snake))
    clock = pg.time.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False

        # Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        #pg.draw.rect(screen, (200,200,200), snake.rect)
        pg.display.flip()

    pg.quit()



if __name__ == "__main__":
    main()