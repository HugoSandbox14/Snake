import Class
import pygame
import Outils as o


pygame.init()
Screen = Class.Screen(1200, 850)
Snake = Class.Snake()
Apple = Class.Apple(Snake)
Score = Class.Score()
count = 0

o.base(Screen.screen)
running = True
while running : 
    Score.display(Screen.screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if o.is_valid_position(Snake,"UP") == True:
                    Snake.direction = "UP"
            elif event.key == pygame.K_DOWN:
                if o.is_valid_position(Snake,"DOWN") == True:
                    Snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                if o.is_valid_position(Snake,"LEFT") == True:
                    Snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                if o.is_valid_position(Snake,"RIGHT") == True:
                    Snake.direction = "RIGHT"
            elif event.key == pygame.K_SPACE:
                Snake.speed = not Snake.speed
                print("Speed:", Snake.speed)
    
    Apple.draw(Screen.screen)
    Snake.draw(Screen.screen)
    count = Snake.move(Snake.direction, count,Screen,Score)
    if Snake.lose() == True:
        print("You lose!")
        print("Your score is:", Score.score)
        running = False
    if Snake.eat(Apple) == True:
        Apple = Class.Apple(Snake)
        Snake.add_block(Snake.body[-1].x, Snake.body[-1].y)
        Score.add_score()

    pygame.display.flip()
    pygame.time.Clock().tick(60) 