import pygame
import cell_physics as p

zoom_fac = 1

def draw_cells(screen):
    for cell in p.Cells.all_cells:
        color = cell.color
        center = cell.pos * zoom_fac
        radius = cell.radius * zoom_fac
        
        
        pygame.draw.circle(screen, color, center, radius)

def change_zoom(zoom):
    '''
    "zoom" is the mouse wheel's state.
    It will either be 1 (zoom in) or -1 (zoom out).
    '''
    
    global zoom_fac
    zoom_fac += zoom * (zoom_fac/5)
    print(f"new zoom_fac: {zoom_fac}")