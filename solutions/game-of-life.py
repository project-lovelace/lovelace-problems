import numpy as np

ALIVE = 1
DEAD = 0

def game_of_life(grid, steps):
    grid = np.array(grid)
    N, M = grid.shape

    for n in range(steps):
        newGrid = grid.copy()
        for i in range(N):
            for j in range(M):
                total = (grid[i, (j-1)%M] + grid[i, (j+1)%M] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%M] + grid[(i-1)%N, (j+1)%M] +
                         grid[(i+1)%N, (j-1)%M] + grid[(i+1)%N, (j+1)%M])
                if grid[i, j]  == ALIVE:
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = DEAD
                else:
                    if total == 3:
                        newGrid[i, j] = ALIVE
                grid = newGrid

    return grid
