import pygame

class Line:
    def __init__(self ,screen:object ,start_pos:tuple[int] , stop_pos:tuple[int] , color:str , width:int) -> None:
        self.screen = screen
        self.start_pos = start_pos
        self.stop_pos = stop_pos
        self.color = color
        self.width = width 

    # ı want to use show instead of draw becouse of pylpllot lib :)
        
    def show(self) -> None:
        pygame.draw.line(self.screen, self.color, self.start_pos, self.stop_pos, self.width)
        pygame.display.flip()

    # wonderful suggsetion