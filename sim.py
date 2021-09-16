import numpy as np
import matplotlib.pyplot as plt

N = 6
L = 20
v_max = 5

pos = np.zeros(N)
vel = np.zeros(N)


for n in range(N):
    pos[n] = 2*n 
    vel[n] = np.random.randint(0,5)

def dist(i,j):
    return np.abs(pos[i] - pos[j])


def update_vel(pos,vel):


    for i,_ in enumerate(vel):

        next_idx = (i+1) % N
        print(i, next_idx)
        next_distance = dist(i, next_idx)

        # aplicamos las reglass

        vel[i] = min(vel[i]+1, v_max)
        vel[i] = min(vel[i], next_distance-1)
        vel[i] = max(vel[i], 0)


pos_list = [[] for i in range(N)]
vel_list = [[] for i in range(N)]

for step in range(30):
    for i in range(N):
        pos_list[i].append(pos[i])
        vel_list[i].append(vel[i])
    update_vel(pos, vel)
    pos = [pos[i] + vel[i] for i in range(N)]

for i in range(N):
    plt.plot(pos_list[i])

plt.show()

for i in range(N):

    plt.plot(vel_list[i])
plt.show()