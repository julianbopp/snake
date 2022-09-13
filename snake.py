import pygame as pg
import random

SIZE = (500, 500)
CENTER = (SIZE[0]/2, SIZE[1]/2)

class Food(pg.sprite.Sprite):
    
    def __init__(self, xpos, ypos):
        pg.sprite.Sprite.__init__(self)

        self.width = 10
        self.height = 10
        self.image = pg.Surface([self.width, self.height])
        self.image = self.image.convert()
        self.image.fill((255,000,000))
        self.rect = self.image.get_rect()
        self.rect.topleft = (xpos, ypos)

class FoodSpawner():

    def __init__(self):
        self.count = 0
        self.foodEaten = False

        # create initial food item
        self.newFood = Food(random.randint(0,SIZE[0]), random.randint(0,SIZE[1]))
        self.foods = pg.sprite.RenderPlain(self.newFood)

    def update(self):
        if self.foodEaten:
            self.newFood = Food(random.randint(0,SIZE[0]), random.randint(0,SIZE[1]))
            self.foods = pg.sprite.RenderPlain(self.newFood)
            self.foodEaten = False
    
    def draw(self, screen):
        self.foods.draw(screen)

    def eaten(self, snake):
        if self.newFood.rect.colliderect(snake.rect):
            self.foodEaten = True
        


class SnakePart(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

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
        self.size = 1
        self.snakeElements = []
        self.snakeElementsPos = []

        self.snakeElements.append(self.head)
        self.allsprites = pg.sprite.RenderPlain(self.snakeElements)

        # speed
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        tmpPos = self.head.rect.topleft
        self.head.rect.move_ip(self.xspeed, self.yspeed)

        n = len(self.snakeElements)
        
        for i in range(n-1):
            tmp = self.snakeElements[i+1].rect.topleft
            self.snakeElements[i+1].rect.topleft = tmpPos
            tmpPos = tmp
            if self.collision(self.snakeElements[i+1].rect):
                quit()
        

    def collision(self, rectangle):
        return self.head.rect.colliderect(rectangle)

    def draw(self, screen):
        self.allsprites.draw(screen)

    def grow(self):
        newPart = SnakePart()
        self.snakeElements.append(newPart)
        self.allsprites = pg.sprite.RenderPlain(self.snakeElements)



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
    foodSpawner = FoodSpawner()
    clock = pg.time.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(10)

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    snake.yspeed = -10
                    snake.xspeed = + 0
                if event.key == pg.K_a:
                    snake.yspeed = + 0
                    snake.xspeed = -10
                if event.key == pg.K_s:
                    snake.yspeed = +10
                    snake.xspeed = + 0
                if event.key == pg.K_d:
                    snake.yspeed = + 0
                    snake.xspeed = +10

        # Draw Everything
        screen.blit(background, (0, 0))
        foodSpawner.eaten(snake.head)
        foodSpawner.update()
        foodSpawner.draw(screen)
        snake.update()
        snake.draw(screen)
        pg.display.flip()

    pg.quit()



if __name__ == "__main__":
    main()