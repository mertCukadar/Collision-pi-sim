import pygame
from .Math import Vector2D


class Box:
    def __init__(self,x:int , y:int, width:int, height:int, color:str , mass:int , Vector2d:Vector2D , name:str) -> None:
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.mass = mass
        self.velocity_x = Vector2d.x
        self.velocity_y = Vector2d.y
        self.v:int = 100

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.display.flip()


    def move(self , dt:float)-> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.v * dt
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.v * dt
        if keys[pygame.K_UP]:
            self.rect.y -= self.v * dt
        if keys[pygame.K_DOWN]:
            self.rect.y += self.v * dt
        
    def update(self, dt:float) -> None:
        self.rect.x += self.velocity_x * dt
        self.rect.y += self.velocity_y * dt

    def collide(self, obj) -> None:
        self.collide_count += 1
        return self.rect.colliderect(obj.rect)
        
    
    def bounce(self, obj) -> None:
        if self.collide(obj):  
            sum_mass = self.mass + obj.mass
            new_velocity = ((self.mass - obj.mass) / sum_mass * self.velocity.x)
            new_velocity += ((2 * obj.mass) / sum_mass * obj.velocity.x)
            self.velocity.x = new_velocity

    def collision_wall(self) -> None:
        if self.rect.x <= 45:
            self.collide_count += 1
            self.velocity.x *= -1

    def end_game(self) -> None:
        if self.rect.x <40:
            print(f"{self.name} has collided {self.collide_count} times")
            pygame.quit()
            exit()