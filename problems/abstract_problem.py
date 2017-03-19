# abstract_problem.py

import abc


class AbstractProblem(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate(self):
        """Create a problem and return it with the solution."""

    @abc.abstractmethod
    def solve(self, problem):
        """Solve a given problem and return its solution."""

    @abc.abstractmethod
    def verify(self, answer, solution):
        """Given an answer to the problem, compare it to the solution and
        return True if correct, else False."""

    # @property
    # @abc.abstractmethod
    # def error_margin(self):
    #     return
