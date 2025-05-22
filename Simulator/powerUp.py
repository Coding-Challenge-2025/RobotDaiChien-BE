import random
from collections import deque
from listOfPlayers import *
from Players import *

class PowerUp:
    def __init__(self, x, y, powerup_type, timeout):
        self.x = x
        self.y = y
        self.type = powerup_type
        self.timeout = timeout

    def toDictionary(self):
        return {"x": self.x, "y": self.y, "type": self.type, "timeout": self.timeout}
    
    def reduceTimeout(self):
        self.timeout -= 1

    def checkExpired(self):
        if self.timeout == 0:
            return True
        else:
            return False
    
def findPowerUp(x: int, y: int, listOfPowerUps: list) -> str:
    for powerUp in listOfPowerUps:
        if powerUp.x == x and powerUp.y == y:
            return powerUp.type
    return None

def deletePowerUp(x: int, y: int, listOfPowerUps: list) -> None:
    for powerUp in listOfPowerUps:
        if powerUp.x == x and powerUp.y == y:
            listOfPowerUps.remove(powerUp)

def updatePowerUpTimeout(listOfPowerUps: list) -> None:
    powerUpsToCheck = list(listOfPowerUps)
    for pu in powerUpsToCheck:
        pu.reduceTimeout()
        if pu.checkExpired():
            if pu in listOfPowerUps:
                listOfPowerUps.remove(pu)

def addPowerUp(board, listOfPowerUps: list, timeout: int, listOfPlayers: ListOfPlayers) -> None:
    powerup_types = ['G', 'E', 'F']
    chosen_types = random.sample(powerup_types, 2)
    movable_cells = board.listMovableCells()
    set_of_movable_cells = set(movable_cells)
    if len(listOfPlayers) > 2:
        for i in range(len(listOfPlayers)):
            set_of_movable_cells.discard(listOfPlayers[i].getCurrentPosition())
        
        set_of_movable_cells = list(set_of_movable_cells)
        for powerup_type in chosen_types:
            if not set_of_movable_cells:
                break
            x, y = random.choice(set_of_movable_cells)
            x, y = int(x), int(y)
            if findPowerUp(x, y, listOfPowerUps) == None:
                listOfPowerUps.append(PowerUp(x, y, powerup_type, timeout))
                set_of_movable_cells.remove((x,y))
        
        return
    pos1 = listOfPlayers[0].getCurrentPosition()
    pos2 = listOfPlayers[1].getCurrentPosition()

    near_equidistant_cells = set()
    for cell in movable_cells:
            dist_pos1_to_cell = get_path_distance(pos1, cell, set_of_movable_cells)
            dist_pos2_to_cell = get_path_distance(pos2, cell, set_of_movable_cells)
            if dist_pos1_to_cell == dist_pos2_to_cell and dist_pos1_to_cell != float('inf') and min(dist_pos1_to_cell, dist_pos2_to_cell) >= 2:
                near_equidistant_cells.add(cell)
            elif abs(dist_pos1_to_cell - dist_pos2_to_cell) == 1 and min(dist_pos1_to_cell, dist_pos2_to_cell) >= 2:
                near_equidistant_cells.add(cell)

    near_equidistant_cells = list(near_equidistant_cells)
    for powerup_type in chosen_types:
        if not near_equidistant_cells: # No more available cells
            break
        x, y = random.choice(near_equidistant_cells)
        x, y = int(x), int(y)
        if findPowerUp(x, y, listOfPowerUps) == None:
            listOfPowerUps.append(PowerUp(x, y, powerup_type, timeout))
            near_equidistant_cells.remove((x,y))
        
def get_path_distance(start_pos: tuple, end_pos: tuple, set_of_all_movable_cells: set) -> float:
    if start_pos == end_pos:
        return float('inf')
    
    if start_pos not in set_of_all_movable_cells or end_pos not in set_of_all_movable_cells:
        return float('inf')

    queue = deque([(start_pos, 0)])
    visited = {start_pos}

    while queue:
        (current_x, current_y), dist = queue.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_pos = (current_x + dx, current_y + dy)

            if next_pos == end_pos:
                return dist + 1

            if next_pos in set_of_all_movable_cells and next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, dist + 1))
    
    return float('inf')