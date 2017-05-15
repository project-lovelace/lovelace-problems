# abstract_problem.py

import abc


class AbstractProblem(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_input(self, test_type):
        """Create the input(s) for a problem and return them as a TestCase object. If the solution is known at input
        creation time, it should be included in the TestCase. It would be called generate_test_case except that it is
        only expected to generate the input, not the output."""

    @abc.abstractmethod
    def solve_test_case(self, test_case):
        """Solve a problem given a TestCase object with an input and update the TestCase object with the solution."""

    @abc.abstractmethod
    def test_our_solution(self):
        """Just a method used to test that our code all works (no errors) and that our solution is correct (which will
        probably involve some solution checking by humans). It should test the generate_input and solve_problem methods
        extensively. It will probably just be run occasionally to ensure our code still works in between updates.
        """

    @abc.abstractmethod
    def verify_user_solution(self, test_case):
        """Given a TestCase object containing the user's input and output (solution), verify that they have solved the
        problem correctly by comparing the test case our own solution. Return True if correct, else False."""

    @abc.abstractmethod
    def generate_test_cases(self):
        """Generates a bunch of TestCase objects used to check the user's submitted code."""

    # @property
    # @abc.abstractmethod
    # def error_margin(self):
    #     return
