from abc import ABCMeta, abstractmethod


class AbstractProblem(metaclass=ABCMeta):

    @property
    @abstractmethod
    def constants(self):
        """A dictionary of physical constants needed to solve the problem. Generally supplied to the user."""
        pass

    @property
    @abstractmethod
    def testing(self):
        """A dictionary of constants relevant for verifying user solutions. Includes stuff like error tolerances."""
        pass

    @abstractmethod
    def generate_input(self, test_type):
        """Create the input(s) for a problem and return them as a TestCase object. If the solution is known at input
        creation time, it should be included in the TestCase. It would be called generate_test_case except that it is
        only expected to generate the input, not the output."""

    @abstractmethod
    def solve_test_case(self, test_case):
        """Solve a problem given a TestCase object with an input and update the TestCase object with the solution."""

    @abstractmethod
    def verify_user_solution(self, user_input_str, user_output_str):
        """Given the user's input and output (solution) strings, verify that they have solved the problem correctly by
        solving the test case ourselves. Return True if their solution is correct, else False."""

    @abstractmethod
    def test_our_solution(self):
        """Just a method used to test that our code all works (no errors) and that our solution is correct (which will
        probably involve some solution checking by humans). It should test the generate_input and solve_problem methods
        extensively. It will probably just be run occasionally to ensure our code still works in between updates."""

    @abstractmethod
    def generate_test_cases(self):
        """Generates a bunch of TestCase objects used to check the user's submitted code. Should be called at
        __init__."""