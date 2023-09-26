from typing import List

# A board with 4x4 grids. You can put a ship with size 1X3 and a ship with 1X2 on the board. 
# Ask: How many different ways to put it.

def is_available_horizontal(grid, i, j, size):
    for k in range(j, j+size):
        if k>= len(grid):
            return False
        if grid[i][k] != 0:
            return False
    
    return True

def is_available_vertical(grid, i, j, size):
    for k in range(i, i+size):
        if k >= len(grid):
            return False
        if grid[k][j] != 0:
            return False
    return True

def put_piece(i,j, size: int, orientation : str, index):
    if orientation == "horizontal":
        for k in range(j, j+size):
            grid[i][k] = index
    
    elif orientation == "vertical":
        for k in range(i, i +size):
            grid[k][j] = index

def remove_piece(i, j, size, orientation):
    if orientation == "horizontal":
        for k in range(j, j+size):
            grid[i][k] = 0
    
    elif orientation == "vertical":
        for k in range(i, i +size):
            grid[k][j] = 0

class Piece:
    def __init__(self, size, index ) -> None:
        self.size = size
        self.index = index
        


def count(pieces : List[Piece], grid, counted_grids : set = None):
    global counter
    if len(pieces) == 0:
        counter += 1
        return
    
    n = len(grid)
    
    for i in range(n):
        for j in range(n):
            if is_available_horizontal(grid,i,j, pieces[-1].size):

                piece = pieces.pop()
                put_piece(i,j, piece.size, "horizontal", piece.index)
                tuple_grid = [tuple(grid[i]) for i in range(n) ] 

                if not tuple(tuple_grid) in counted_grids:
                    counted_grids.add(tuple(tuple_grid))
                    count(pieces, grid, counted_grids)

                remove_piece(i, j, piece.size, "horizontal")
                pieces.append(piece)

            if is_available_vertical(grid, i, j, pieces[-1].size):
                piece = pieces.pop()
                put_piece(i,j, piece.size, "vertical", piece.index)
                
                tuple_grid = [tuple(grid[i]) for i in range(n) ] 
                if not tuple(tuple_grid) in counted_grids:
                    counted_grids.add(tuple(tuple_grid))
                    count(pieces, grid, counted_grids)

                remove_piece(i, j, piece.size, "vertical")
                pieces.append(piece)


n= 4
pieces = [Piece(2,2), Piece(3,3)]
counter = 0
counted_grids = set()
grid = [[0 for i in range(n)] for j in range(n)]
count(pieces, grid ,counted_grids)