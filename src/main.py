import sim
import utils
import numpy as np
import matplotlib.pyplot as plt
import argparse


def main():

    my_parser = argparse.ArgumentParser(description='Parameters for Simulation')
    my_parser.add_argument('-N', '--n_cars', type=int, action='store', help='Number of cars', default = 40)
    my_parser.add_argument('-L', '--length', type=int, action='store', help='Length of road', default = 250)
    my_parser.add_argument('-P', '--p_break', type=float, action='store', help='probability of stopping', default = 0.1)
    my_parser.add_argument('-S', '--steps', type=int, action='store', help='Steps of simulation', required = True)

    args = my_parser.parse_args()
    print(dir(args))

    N=args.n_cars
    L=args.length

    pos = np.zeros(N)
    vel = np.zeros(N)

    sim.populate_arrays(pos,vel,N)
    pos_list = sim.run_simulation(pos,vel,N,L, MAX_STEPS=args.steps, p = args.p_break)
    flow = utils.estimate_flow(pos_list,N, 0,250)
    sim_fig = utils.plot_simulation(pos_list)
    plt.show()




if __name__ == '__main__':
    main()
