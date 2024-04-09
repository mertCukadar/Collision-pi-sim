import pygame
from src.Map import Map
from src.Box import Box
from src.Math import Vector2D
from src.Line import Line

screen_size = (800 , 600)
fps = 60

def main() -> None:
    dt = 0
    screen_obj = Map(screen_size[0], screen_size[1], "Collide-pi-sim")
    clock = screen_obj.clock

    small_vector = Vector2D(0, 0)
    big_vector = Vector2D(-50, 0)
    box_small = Box(200, screen_size[1] - 90, 50, 50, "blue",1, "box_small" ,small_vector)
    box_big = Box(400, screen_size[1] - 90, 50, 50, "green", 10000000000 , "red box" , big_vector)


    while screen_obj.running:
        screen_obj.is_event_quit()
        #-------------------"CODE GOES HERE"-------------------#
        screen_obj.fill("red")
        box2.draw(screen_obj.screen)
        box1.draw(screen_obj.screen)
        box1.move(dt)
        box1.collide(box2)

        horizantal_line = Line(screen_obj.screen, (0, screen_size[1] - 40), (800, screen_size[1] - 40), "white", 9)
        vertical_line = Line(screen_obj.screen, (40, 0), (40, 600), "white", 9)


        horizantal_line.show()
        vertical_line.show()
        #-------------------"CODE GOES HERE"-------------------#
        dt = clock.tick(fps) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()