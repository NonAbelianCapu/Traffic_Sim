import unittest
from src import sim 
import numpy as np

class Test(unittest.TestCase):

    N = 40
    L = 250
    MAX_STEPS = 250

    init_pos = np.zeros(N)
    init_vel = np.zeros(N)

    sim.populate_arrays(init_pos, init_vel, N)
    test_pos = sim.run_simulation(init_pos, init_vel,N,L, MAX_STEPS=MAX_STEPS)

    def test_size(self):

        SIZE = self.L*(self.MAX_STEPS+1)
        pos_size = sum([len(row) for row in self.test_pos])
        self.assertEqual(pos_size, SIZE)

    def test_vel(self):

        MAX_VEL = 5

        for ri,row in enumerate(self.test_pos):
            for val in row:
                self.assertLessEqual(val, MAX_VEL)



if __name__ == '__main__':

    unittest.main()
