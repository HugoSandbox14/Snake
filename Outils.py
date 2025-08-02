import pygame
import random

Case = 50
Height = 16
Width = 16
Padding = 20

Colors = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255)
}

def draw_block(screen,x,y,color,size = 50):
    pygame.draw.rect(screen, color, (x*size+Padding,y*size+Padding,size,size))
    pygame.draw.rect(screen, Colors["BLACK"], (x*size+Padding,y*size+Padding,size,size),2)

def draw_apple(screen,x,y,color,size = 25,padding = 10):
    pygame.draw.rect(screen, color, ((x*Case)+Padding+padding,(y*Case)+Padding+padding,size,size))

def base(screen):
    screen.fill(Colors["BLACK"])
    pygame.draw.rect(screen, Colors["WHITE"], (Padding,Padding, Height*Case, Width*Case))

def compute_next(x,y,direction):
    if direction == "UP":
        y -= 1
    elif direction == "DOWN":
        y += 1
    elif direction == "LEFT":
        x -= 1
    elif direction == "RIGHT":
        x += 1
    return x, y

def is_valid_position(snake,direction):
    hx,hy = compute_next(snake.head.x, snake.head.y, direction)
    bx,by = snake.body[0].x, snake.body[0].y
    print("Head: ", hx,",", hy, "Body:", bx,",", by)
    if hx == bx and hy == by:
        return False
    else :
        return True


def infos_snake(snake):
    liste = []
    liste.append((snake.head.x, snake.head.y))
    for el in snake.body:
        liste.append((el.x, el.y))
    return liste
