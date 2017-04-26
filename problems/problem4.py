# problem4.py
# Convex chocolate chip cookies

import logging

from problems.abstract_problem import AbstractProblem

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Problem4(AbstractProblem):
    def generate(self):
        return

    @staticmethod
    def in_hull(p, hull):
        """
        Test if points in p are in hull

        * p should be an NxK coordinates of N points in K dimensions.
        * hull is either a scipy.spatial.Delaunay object or the MxK array of the 
          coordinates of M points in K dimensions for which Delaunay
          triangulation will be computed.
        """
        from scipy.spatial import Delaunay
        if not isinstance(hull, Delaunay):
            hull = Delaunay(hull)

        return hull.find_simplex(p) >= 0

    def solve(self, problem):
        return

    def verify(self, proposed, actual):
        return proposed == actual

    def test(self):
        problem = self.generate()
        print(problem)

        solution = self.solve(problem)
        print(solution)

if __name__ == '__main__':
    Problem4().test()
