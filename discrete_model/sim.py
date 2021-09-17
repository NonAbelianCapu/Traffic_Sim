import numpy as np
import matplotlib.pyplot as plt
import random

def populate_arrays(pos,vel,N):

    for n in range(N):
        pos[n] = n
        vel[n] = np.random.randint(0,5)

def dist(i,j,L,pos):

    if pos[i] <= pos[j]:
        return pos[j] - pos[i]
    else:
        return L - pos[i] + pos[j]


def update_vel(pos,vel,p,L,v_max,N):

    for i,_ in enumerate(vel):

        next_idx = (i+1) % N

        next_distance = dist(i, next_idx,L,pos)

        # aplicamos las reglass

        vel[i] = min(vel[i]+1, v_max)
        vel[i] = min(vel[i], next_distance-1)

        r = random.uniform(0, 1)

        if r < p:
            vel[i] = max(vel[i]-1, 0)

        vel[i] = max(vel[i], 0)


def run_simulation(pos,vel,N,L,MAX_STEPS=250,p=0.1,v_max=5):

    pos_list = [np.zeros(L+1) for i in range(MAX_STEPS)]

    for step in range(MAX_STEPS):

        for i in range(N):
            pos_list[step][int(pos[i])] = int(vel[i])

        update_vel(pos,vel,p,L,v_max,N)
        pos = [(pos[i] + vel[i])%L for i in range(N)]

    return pos_list
