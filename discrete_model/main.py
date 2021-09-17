import sim
import utils
import numpy as np
import matplotlib.pyplot as plt


def main():


    N=40
    L=250

    pos = np.zeros(N)
    vel = np.zeros(N)

    sim.populate_arrays(pos,vel,N)
    pos_list = sim.run_simulation(pos,vel,N,L, MAX_STEPS=250, p = 0)
    flow = utils.estimate_flow(pos_list,N, 0,250)
    sim_fig = utils.plot_simulation(pos_list)
    plt.show()
    plt.plot(flow)
    plt.show()


if __name__ == '__main__':
    main()
