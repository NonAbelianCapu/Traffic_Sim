import numpy as np
import matplotlib.pyplot as plt
import random


N = 40
L = 250
v_max = 5
p = 0.1

pos = np.zeros(N)
vel = np.zeros(N)


for n in range(N):
    pos[n] = 3*n
    vel[n] = np.random.randint(0,5)

def dist(i,j):
    if pos[i] <= pos[j]:
        return pos[j] - pos[i]
    else:
        return L - pos[i] + pos[j]


def update_vel(pos,vel):

    for i,_ in enumerate(vel):

        next_idx = (i+1) % N

        next_distance = dist(i, next_idx)


        if i == N-1:
            print(next_distance)

        # aplicamos las reglass

        vel[i] = min(vel[i]+1, v_max)
        vel[i] = min(vel[i], next_distance-1)

        r = random.uniform(0, 1)

        if r < p:
            vel[i] = max(vel[i]-1, 0)
        vel[i] = max(vel[i], 0)


MAX_STEPS = 250

pos_list = [np.zeros(L+1) for i in range(MAX_STEPS)]
vel_list = [np.zeros(L+1) for i in range(MAX_STEPS)]

for step in range(MAX_STEPS):
    print(step,pos)
    for i in range(N):
        pos_list[step][int(pos[i])] = 1+int(vel[i])
    update_vel(pos, vel)
    pos = [(pos[i] + vel[i])%L for i in range(N)]


plt.imshow(pos_list, cmap='inferno')
plt.show()
