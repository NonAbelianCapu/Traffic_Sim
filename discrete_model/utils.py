import numpy as np
import matplotlib.pyplot as plt


def estimate_flow(pos_grid,N,i,f):

    # estimates flow over time between position i and f in the road

    flow = []
    L = len(pos_grid[0])
    T = len(pos_grid)

    assert (i >= 0 and i <= L-1), "i out of bound"
    assert (f >= 0 and f <= L-1), "f out of bound"

    for row in pos_grid:

        temp_array = row[i:f]
        temp_flow = np.sum(temp_array)*(N/(L*T))
        flow.append(temp_flow)

    return flow




def plot_simulation(pos_grid):

    fig = plt.figure(figsize=(10,6))

    # we add some contrast to the velocity to the background of imshow

    for r,row in enumerate(pos_grid):
        for c,col in enumerate(row):
            pos_grid[r][c] += 1

    plt.xlabel('Occupation', fontsize = 13)
    plt.ylabel('Time', fontsize = 13)
    plt.title('Simulation')
    plt.legend()
    plt.imshow(pos_grid, cmap='inferno')

    return fig
