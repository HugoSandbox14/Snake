
import pygame
import Outils as o
import random

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game Screen")


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen,color):
        o.draw_block(screen,self.x, self.y,color)
    
    def move(self,direction):
        if direction == "UP":
            self.y -= 1
        elif direction == "DOWN":
            self.y += 1
        elif direction == "LEFT":
            self.x -= 1
        elif direction == "RIGHT":
            self.x += 1

        if self.x < 0:
            self.x = o.Width - 1
        elif self.x >= o.Width:
            self.x = 0
        if self.y < 0:
            self.y = o.Height - 1
        elif self.y >= o.Height:
            self.y = 0

class Snake:
    def __init__(self):
        self.head = Block(9, 6)
        self.body = [Block(9, 5), Block(9,4)]
        self.direction = "DOWN"
        self.speed = False

    def draw(self, screen):
        self.head.draw(screen, o.Colors["RED"])
        for block in self.body:
            block.draw(screen, o.Colors["GREEN"])
    
    def add_block(self, x, y):
        self.body.append(Block(x, y))
    
    def move(self,direction,count,screen,score):
        if count == 20 or (count == 10 and self.speed == True):
            tail = self.body[-1]
            pygame.draw.rect(screen.screen, o.Colors["WHITE"], ((tail.x * o.Case) + o.Padding, (tail.y * o.Case) + o.Padding, o.Case, o.Case))
            count = 0
            for i in range(len(self.body),0,-1):
                if i == 1:
                    self.body[i-1].x = self.head.x
                    self.body[i-1].y = self.head.y
                else:
                    self.body[i-1].x = self.body[i-2].x
                    self.body[i-1].y = self.body[i-2].y
            self.head.move(direction)
            score.mouvement += 1
        else:
            count += 1
        return count
    
    def eat(self,apple):
        if self.head.x == apple.x and self.head.y == apple.y:
            return True
        return False

    def lose(self):
        for block in self.body:
            if self.head.x == block.x and self.head.y == block.y:
                return True
        return False
    
class Apple:
    def __init__(self,snake):
        self.x = random.randint(0, o.Width - 1)
        self.y = random.randint(0, o.Height - 1)
        if (self.x,self.y) in o.infos_snake(snake):
            self.regenerate(snake)

    def draw(self, screen):
        o.draw_apple(screen, self.x, self.y, o.Colors["BLUE"])

    def regenerate(self,snake):
        self.x = random.randint(0, o.Width - 1)
        self.y = random.randint(0, o.Height - 1)
        if (self.x,self.y) in o.infos_snake(snake):
            self.regenerate()


class Score:
    def __init__(self):
        self.score = 0
        self.mouvement = 0

    def add_score(self):
        self.score += 50 - self.mouvement
        self.mouvement = 0

    def display(self, screen):
        pygame.draw.rect(screen, o.Colors["BLACK"], (900, 0, 300, 100))
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {self.score}', True, o.Colors["WHITE"])
        text2 = font.render(f'Mouvements: {self.mouvement}', True, o.Colors["WHITE"])
        screen.blit(text, (900, 20))
        screen.blit(text2, (900, 60))
