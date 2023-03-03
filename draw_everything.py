import pygame
import cell_physics as p

zoom_fac = 1
cam_offset = pygame.math.Vector2()

def draw_cells(screen):
    for cell in p.Cells.all_cells:
        color = cell.color
        center = (cell.pos * zoom_fac) + cam_offset
        radius = cell.radius * zoom_fac
        
        pygame.draw.circle(screen, color, center, radius)

def change_zoom(zoom):
    '''
    "zoom" is the mouse wheel's state.
    It will either be 1 (zoom in) or -1 (zoom out).
    '''
    
    global zoom_fac
    zoom_fac += zoom * (zoom_fac/5)

class DragScreen:
    prev_mouse_pos = pygame.math.Vector2()
    cur_mouse_pos = pygame.math.Vector2()
    
    def start(mouse_pos: pygame.math.Vector2):
        DragScreen.prev_mouse_pos = mouse_pos
        DragScreen.cur_mouse_pos = mouse_pos
    
    def drag(mouse_pos: pygame.math.Vector2):
        DragScreen.prev_mouse_pos = DragScreen.cur_mouse_pos
        DragScreen.cur_mouse_pos = mouse_pos
        
        drag_vec = DragScreen.cur_mouse_pos - DragScreen.prev_mouse_pos
        print(drag_vec)
        global cam_offset
        cam_offset = cam_offset + drag_vec
        print(cam_offset)