import sim
import utils
import numpy as np
import matplotlib.pyplot as plt
import argparse


my_parser = argparse.ArgumentParser(description='Parameters for Phase Diagram')
my_parser.add_argument('-L', '--length', type=int, action='store', help='Length of road', default = 250)
my_parser.add_argument('-N_i', '--n_init', type=int, action='store', help='Initial Car Number', default = 0)
my_parser.add_argument('-N_f', '--n_final', type=int, action='store', help='Final Car Number', default = 249)

args = my_parser.parse_args()

flow_list = []

for nc in range(args.n_init, args.n_final):

    L = args.length
    N = nc

    pos = np.zeros(N)
    vel = np.zeros(N)

    sim.populate_arrays(pos,vel,N)
    pos_list = sim.run_simulation(pos,vel,N,L, MAX_STEPS = 350, p = 0.1)
    flow = utils.estimate_flow(pos_list, N, 0,L-1)
    print(nc, flow[-1])
    plt.plot(nc, flow[-1], 'o')


plt.show()
