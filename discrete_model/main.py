from sim import *

pos = np.zeros(40)
vel = np.zeros(40)
N=40
L=250

populate_arrays(pos,vel,N)
pos_list = run_simulation(pos,vel,N,L)

plt.imshow(pos_list, cmap='inferno')
plt.show()

if __name__ == '__main__':
    main()
