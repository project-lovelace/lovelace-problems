# problem2.py

import math
import random

import numpy as np

from abstract_problem import AbstractProblem


class Problem2(AbstractProblem):

    def generate(self):
        # Physical constants
        # TODO: Find reasonable values for g, m, C, rho, A.
        g = 9.8 # [m/s^2]
        m = 1 # [kg]

        C = 1
        rho = 1
        A = 1
        B2 = 0.5 * C * rho * A

        # Problem generation parameters
        # TODO: Find good values for these that make sense for the problem.
        minShots = 5
        maxShots = 250

        minTheta = 0
        maxTheta = 180

        minV0 = 0
        maxV0 = 500

        # TODO: Got to n-shot case?
        # nShots = random.randint(minShots, maxShots)
        # theta = [random.uniform(minTheta, maxTheta) for _ in range(nShots)]
        # v0 = [random.uniform(minV0, maxV0) for _ in range(nShots)]

        # For now we just do 1 shot.
        nShots = 1
        theta  = random.uniform(minTheta, maxTheta)
        v0     = random.uniform(minV0, maxV0)

        # TODO: How do we do this here? Modify it a bit? Use files?
        # print("Input:", str(r1[0]), str(r1[1]), str(tS1-tP1), str(r2[0]), str(r2[1]), str(tS2-tP2), str(r3[0]), str(r3[1]), str(tS3-tP3))
        # print("Generator's solution:", str(r0[0]), str(r0[1]))
        #
        # problem = [
        #     r1[0], r1[1], (tS1 - tP1),
        #     r2[0], r2[1], (tS2 - tP2),
        #     r3[0], r3[1], (tS3 - tP3)
        # ]
        # solution = r0
        #
        # return problem, solution

    def solve(self, problem):
        # Physical constants
        # TODO: Find reasonable values for g, m, C, rho, A. Also x0, y0, blast_radius.
        g = 9.8 # [m/s^2]
        m = 1 # [kg]

        C = 1
        rho = 1
        A = 1
        B2 = 4e-5

        x0 = 1 # [m]
        y0 = 1 # [m]

        blast_radius = 3 # [m]

        # ODE solver parameters
        delta_t = 0.001 # [s]

        theta = 33.45
        v0 = 45

        x = [x0]
        y = [y0]
        vx = [v0*np.cos(np.deg2rad(theta))]
        vy = [v0*np.sin(np.deg2rad(theta))]
        v = [np.sqrt(vx[0]**2 + vy[0]**2)]

        # Solve for the trajectories using Euler's method (RK1) and stop once the
        # projectile hits the ground.
        i = 0
        while y[i] > 0:
            # Calculate the i+1 entries and append them.
            x.append( x[i] + vx[i]*delta_t )
            vx.append( vx[i] - (B2/m)*v[i]*vx[i] )
            y.append( y[i] + vy[i]*delta_t )
            vy.append( vy[i] - g*delta_t - (B2/m)*v[i]*vy[i] )
            v.append( np.sqrt(vx[i+1]**2 + vy[i+1]**2) )
            i = i+1

        # Interpolate between the last two data points to get a (usually) slightly
        # more accurate x-position value. Probably doesn't matter too much.
        x_final = (x[-1] + x[-2]) / 2

        solution = str(x_final)

        print("Solver's solution:", solution)
        return solution


    def verify(self, proposed, actual):
        error = abs(proposed-actual)
        print("Error:", error)

        return error == 0


    def test(self):
        problem, solution = self.generate()

        actual = solution
        proposed = self.solve(problem)

        is_correct = self.verify(proposed, actual)
        print("Problem solved!") if is_correct else print("Incorrect solution.")


if __name__ == '__main__':
    Problem2().test()
