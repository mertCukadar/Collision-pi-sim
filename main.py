import pygame
from src.Map import Map
from src.Box import Box
from src.Math import Vector2D

screen_size = (800 , 600)
fps = 60

def main() -> None:
    dt = 0
    screen_obj = Map(screen_size[0], screen_size[1], "Collide-pi-sim")
    clock = screen_obj.clock


    velocity = Vector2D(1, 1)
    box1 = Box(100, 100, 50, 50, "blue", 10, velocity , "box1")
    box2 = Box(200, 200, 50, 50, "green", 10, velocity , "red box")


    while screen_obj.running:
        screen_obj.is_event_quit()
        #-------------------"CODE GOES HERE"-------------------#
        screen_obj.fill("red")
        box2.draw(screen_obj.screen)
        box1.draw(screen_obj.screen)
        box1.move(dt)
        box1.collide(box2)
    





        #-------------------"CODE GOES HERE"-------------------#
        dt = clock.tick(fps) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()