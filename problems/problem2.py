# problem2.py

import random

import numpy as np

from problems.abstract_problem import AbstractProblem


class Problem2(AbstractProblem):

    def generate(self):
        # Muzzle velocity can actually reach 684 m/s however the shell's drag
        # coefficient is strongly dependent on mach number M (especially for
        # M > 0.9) and so we will limit this problem to M < 0.9.

        theta = random.uniform(-4, 72)  # [deg], M198 Howitzer firing angle
        v_0 = random.uniform(208, 309)  # [m/s], M198 Howitzer muzzle velocity

        # Coordinates of the Howitzer gun's muzzle.
        # TODO: This should depend on the barrel length and firing angle.
        # Let them calculate it?
        x_0 = random.uniform(1, 3)  # [m]
        y_0 = random.uniform(1, 3)  # [m]

        problem = {'theta': theta, 'v_0': v_0, 'x_0': x_0, 'y_0': y_0}
        return problem

    def solve(self, problem):
        g = 9.80665  # [m/s^2], standard gravity
        rho = 1.225  # [kg/m^3], density of air at sea level and 15°C

        m = 43  # [kg], M198 Howitzer shell mass
        A = np.pi * (15.5 / 2) ** 2  # [m^2], area of M107 155mm shell
        # blast_radius = 3  # [m], M198 Howitzer shell destructive radius

        # Drag coefficient depends very strongly on mach number M (especially
        # for M > 0.9), but for M < 0.9 it is essentially constant.
        C = 0.0579080038

        # Dynamic pressure on projectile. (Just bunching up coefficients.)
        P_D = 0.5*rho*C*A

        # Retrieving problem inputs.
        theta = problem['theta']
        v_0 = problem['v_0']
        x_0 = problem['x_0']
        y_0 = problem['y_0']

        # Feeding in initial conditions as the start of a list.
        x = [x_0]
        y = [y_0]
        vx = [v_0*np.cos(np.deg2rad(theta))]
        vy = [v_0*np.sin(np.deg2rad(theta))]
        v = [np.sqrt(vx[0]**2 + vy[0]**2)]

        # ODE solver parameters
        # TODO: Use a robust numpy RK4 ODE solver just to be safe?
        Delta_t = 0.00001  # [s]

        # Solve for the trajectories using Euler's method (RK1) and stop once
        # the projectile hits the ground.
        i = 0
        while i < 5:
            x.append(x[i] + vx[i] * Delta_t)
            vx.append(vx[i])
            # print("v_x change: ", (P_D / m) * v[i] * vx[i])
            # vx.append(vx[i] - (P_D/m) * v[i] * vx[i])
            y.append(y[i] + vy[i] * Delta_t)
            vy.append(vy[i] - g * Delta_t)
            # print("v_y change: ", - (P_D/m) * v[i] * vy[i])
            # vy.append(vy[i] - g * Delta_t - (P_D/m) * v[i] * vy[i])
            v.append(np.sqrt(vx[i+1]**2 + vy[i+1]**2))
            i = i+1

        # Interpolate between the last data point above ground and the data
        # point that would have been below the ground to get a better estimate
        # of the landing point.
        # r = -y[-2]/y[-1]
        # x_final = (x[-2] + r*x[-1]) / (r+1)

        x_final = x[-1]

        solution = {'x_final': x_final}

        print("Solver's solution:", solution)
        return solution

    def verify(self, proposed, actual):
        error = abs(proposed-actual)
        print("Error:", error)

        return error < 1e-3

    def test(self):
        problem = self.generate()
        print(problem)

        solution = self.solve(problem)
        print(solution)

if __name__ == '__main__':
    Problem2().test()
