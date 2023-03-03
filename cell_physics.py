import pygame

class Cells:
    amount_created = 0
    all_cells = []

    def __init__(self, position: pygame.math.Vector2):
        self.pos = position
        self.oldPos = position
        self.acc = pygame.math.Vector2()
        self.radius = 10
        self.color = (255, 255, 255)

        Cells.amount_created += 1
        self.id = Cells.amount_created

        Cells.all_cells.append(self)

    def __str__(self) -> str:
        returnString = f'<Circle {self.id} = '
        returnString += f'pos: {self.pos}, '
        returnString += f'oldPos: {self.oldPos}, '
        returnString += f'acc: {self.acc}, '
        returnString += f'radius: {self.radius}, '
        returnString += f'color: {self.color}>'
        return returnString

    def print_all():
        for cell in Cells.all_cells:
            print(cell)
    
    

