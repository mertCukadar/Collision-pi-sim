import pygame

class Map:
    def __init__(self, x:int, y:int ,caption:str ) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.running:bool = True
    

    def fill(self, color:str) -> None:
        self.screen.fill(color)
        pygame.display.flip()

    def is_event_quit(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
        
