from copy import deepcopy

grid_ex = [["-", "-", "-", "#", "#"],
               ["-", "#", "-", "-", "-"],
               ["-", "-", "#", "-", "-"],
               ["-", "#", "#", "-", "-"],
               ["-", "-", "-", "-", "-"]]


# define function of adjacent mines
def mines_adj(grid):

    # example list input 
    

    # assigning/splitting grid into 2 variables, row & col
    row = len(grid)
    col = len(grid[0])

    # directions are used as a form of navigation, (cordinates)
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    # make a copy of grid
    newgrid = deepcopy(grid)    
    
    # iterate through rows & columns
    for r in range(row):
        for c in range(col):
            
            # if row or column in grid = -, count is 0
            if(grid[r][c] == "-"):
                count = 0

                # navigation in directions of rows at index 0 and columns in index 1
                for nav in directions:
                    nr = r + nav[0]
                    nc = c + nav[1]
                    
                    '''keeping row and col in check of grid and if nr, nc 
                        in grid = # than increment count by 1'''
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "#":
                        count += 1 

                newgrid[r][c] = str(count)  # outputs lists in string, newgrid row & col = count

    return newgrid

# display newgrid
for newgrid in mines_adj(grid_ex):
        print(newgrid)
