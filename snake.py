import os
import pygame as pg


def main():

    # Initialize
    pg.init()
    screen = pg.display.set_mode((500, 500))
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
    # snake = Snake()
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
        # snake.draw
        pg.display.flip()

    pg.quit()



if __name__ == "__main__":
    main()