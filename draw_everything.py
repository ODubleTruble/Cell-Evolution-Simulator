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

def change_zoom(wheel_state, mouse_pos: pygame.math.Vector2):
    '''
    "wheel_state" is the mouse wheel's state.
    It will either be 1 (zoom in) or -1 (zoom out).
    '''
    
    global zoom_fac
    global cam_offset
    
    d_zoom_fac = wheel_state * (zoom_fac/5)
    
    relative_mouse_pos = (mouse_pos - cam_offset) / zoom_fac
    d_cam_offset = relative_mouse_pos.copy().rotate(180)
    d_cam_offset.scale_to_length(d_cam_offset.length() * d_zoom_fac)
    cam_offset = cam_offset + d_cam_offset
    
    zoom_fac += d_zoom_fac
    
    print(f"d_zoom_fac: {d_zoom_fac}")
    print(f"relative_mouse_pos: {relative_mouse_pos}")
    print(f"d_cam_offset: {d_cam_offset}")
    print(f"cam_offset: {cam_offset}")
    print(f"zoom_fac: {zoom_fac}")

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
        global cam_offset
        cam_offset = cam_offset + drag_vec