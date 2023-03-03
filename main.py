import pygame, sys
from pygame.locals import *
import cell_physics as p
import draw_everything as d


screen_draging = False

# Updates variables and processes stuff.
# Called once per frame.
# dt is the amount of time passed since last frame.
def update(dt):
    global screen_draging
    
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                screen_draging = True
                d.DragScreen.start(pygame.math.Vector2(event.pos))
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                screen_draging = False
        elif event.type == pygame.MOUSEMOTION:
            if screen_draging:
                d.DragScreen.drag(pygame.math.Vector2(event.pos))
        
        elif event.type == MOUSEWHEEL:
            d.change_zoom(event.y, pygame.math.Vector2(pygame.mouse.get_pos()))

    
    # SOLVER UPDATE HERE


# Draws everything on the screen.
# Called once per frame. 
def draw(screen):
    # Clears everything on the screen by making it black. 
    screen.fill((0, 0, 0))

    d.draw_cells(screen)

    # Updates the display. 
    pygame.display.update()


def init():
    # Create a few circles. 
    for x in range(1, 4):
        for y in range(1, 4):
            p.Cells(pygame.Vector2(x*25, y*25))
    p.Cells.print_all()

# Runs the PyGame window.
def runPyGame():
    init()
    
    pygame.init()
    
    FPS = 500
    fpsClock = pygame.time.Clock()
    
    WINDOW_SIZE = (pygame.display.get_desktop_sizes()[0][0]/1.5, pygame.display.get_desktop_sizes()[0][1]/1.5)
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption('Dislpay Name')

    dt = 0
    
    # The main game loop.
    while True:
        update(dt)
        draw(screen)

        # dt is time since the last frame.
        # Pauses the program to create the correct FPS. 
        dt = fpsClock.tick(FPS)


runPyGame()