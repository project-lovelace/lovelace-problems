import logging
import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')

# Problem-specific constants.
PHYSICAL_CONSTANTS = {
    'v': 3.0  # [km/s], velocity of seismic waves
}

TESTING_CONSTANTS = {
    'error_tol': 0.0001  # [km]
}


class TestCase1Type(TestCaseTypeEnum):
    GENERAL = ('general case', '', 3)
    ZERO_CASE = ('Zero case',
                 'One of the three stations is randomly placed exactly on top of the earthquake epicenter.',
                 1)
    EQUIDISTANT = ('equidistant case',
                   'All three stations are the same distance from the earthquake epicenter.',
                   1)
    UNKNOWN = ('unknown case',
               'Used when given the input of a test case but not its type. Primarily used by '
               + 'AbstractProblem.verify_user_solution.',
               0)


class TestCase1(TestCase):
    # TestCase1 input and output data structure:
    # Inputs:
    #   x1, y1, t1, x2, y2, t2, x3, y3, t3 (all floats)
    #
    # Outputs:
    #   x, y: coordinates of earthquake epicenter

    def input_str(self):
        input_str = str(self.input['x1']) + ' ' + str(self.input['y1']) + ' ' + str(self.input['t1']) + ' '
        input_str += str(self.input['x2']) + ' ' + str(self.input['y2']) + ' ' + str(self.input['t2']) + ' '
        input_str += str(self.input['x3']) + ' ' + str(self.input['y3']) + ' ' + str(self.input['t3'])
        return input_str

    def output_str(self):
        return str(self.output['x']) + ' ' + str(self.output['y'])


def generate_test_cases():
    """Generates a bunch of TestCase objects used to check the user's submitted code."""
    # TODO: This method will look the same for every module. Any way to reuse this code?
    logger.info("Generating test cases...")
    test_cases = []

    # Count number of test cases we'll be generating in total.
    num_cases = 0
    for test_type in TestCase1Type:
        num_cases += test_type.multiplicity

    # Generate all the cases and store them in test_cases.
    n = 1
    for test_type in TestCase1Type:
        for _ in range(test_type.multiplicity):
            logger.debug("Generating test case %d/%d...", n, num_cases)
            test_cases.append(generate_input(test_type))
            n = n+1

    return test_cases


def generate_input(test_type):
    """Create the input(s) for a problem and return them as a TestCase object. If the solution is known at input
    creation time, it should be included in the TestCase. It would be called generate_test_case except that it is
    only expected to generate the input, not the output."""
    if not isinstance(test_type, TestCase1Type):
        logger.critical('test_type is not of type TestCase1Type!')
        raise TypeError('test_type is not of type TestCase1Type!')

    test_case = TestCase1(test_type)
    logger.debug("Generating %s...", test_type.test_name)

    if test_type is TestCase1Type.GENERAL:
        r0 = np.random.uniform(-100, 100, 2)
        r1 = np.random.uniform(-100, 100, 2)
        r2 = np.random.uniform(-100, 100, 2)
        r3 = np.random.uniform(-100, 100, 2)
    elif test_type is TestCase1Type.ZERO_CASE:
        r0 = np.random.uniform(-100, 100, 2)

        zero_station = np.random.choice([1, 2, 3])
        if zero_station == 1:
            r1 = r0
            r2 = np.random.uniform(-100, 100, 2)
            r3 = np.random.uniform(-100, 100, 2)
        elif zero_station == 2:
            r1 = np.random.uniform(-100, 100, 2)
            r2 = r0
            r3 = np.random.uniform(-100, 100, 2)
        else:
            r1 = np.random.uniform(-100, 100, 2)
            r2 = np.random.uniform(-100, 100, 2)
            r3 = r0
    elif test_type is TestCase1Type.EQUIDISTANT:
        r0 = np.random.uniform(-10, 10, 2)  # Place the earthquake near the origin.
        d = np.random.uniform(10, 90)  # Distance to all the stations. Max=90 ensures we stay inside the box.
        theta = np.random.uniform(0, 2*np.pi, 3)  # Choose three angles to place the stations at a distance d away.

        r1 = r0 + d * np.array([np.cos(theta[0]), np.sin(theta[0])])
        r2 = r0 + d * np.array([np.cos(theta[1]), np.sin(theta[1])])
        r3 = r0 + d * np.array([np.cos(theta[2]), np.sin(theta[2])])
    else:
        logger.critical('test_type is not a known case type!')
        raise ValueError('test_type is not a known case type!')

    v = PHYSICAL_CONSTANTS['v']

    t1 = np.linalg.norm(r1-r0) / v
    t2 = np.linalg.norm(r2-r0) / v
    t3 = np.linalg.norm(r3-r0) / v

    test_case.input = {'x1': r1[0], 'y1': r1[1], 't1': t1,
                       'x2': r2[0], 'y2': r2[1], 't2': t2,
                       'x3': r3[0], 'y3': r3[1], 't3': t3}

    logger.debug("Test case input:")
    logger.debug("(x1, y1, t1) = (%f, %f, %f)", r1[0], r1[1], t1)
    logger.debug("(x2, y2, t2) = (%f, %f, %f)", r2[0], r2[1], t2)
    logger.debug("(x3, y3, t3) = (%f, %f, %f)", r3[0], r3[1], t3)

    test_case.output['x'] = r0[0]
    test_case.output['y'] = r0[1]

    logger.debug("Test case solution available at creation:")
    logger.debug("(x, y) = (%f, %f)", r0[0], r0[1])

    return test_case


def solve_test_case(test_case):
    """Solve a problem given a TestCase object with an input and update the TestCase object with the solution."""
    v = PHYSICAL_CONSTANTS['v']

    x1, y1, t1 = test_case.input['x1'], test_case.input['y1'], test_case.input['t1']
    x2, y2, t2 = test_case.input['x2'], test_case.input['y2'], test_case.input['t2']
    x3, y3, t3 = test_case.input['x3'], test_case.input['y3'], test_case.input['t3']

    # TODO: Find my derivation and write down the steps/logic here.

    r1 = v*t1
    r2 = v*t2
    r3 = v*t3

    # Setting up the equations, we get two simultaneous linear equations for
    # x0 and y0, namely ax + by = e and cx + dy = f where

    a = 2*(x2-x1)
    b = 2*(y2-y1)
    c = 2*(x3-x1)
    d = 2*(y3-y1)
    e = r1**2 - x1**2 - y1**2 - r2**2 + x2**2 + y2**2
    f = r1**2 - x1**2 - y1**2 - r3**2 + x3**2 + y3**2

    # Solving ax + by = e and cx + dy = f for x,y gives
    x = (b*f - d*e) / (b*c - a*d)
    y = (c*e - a*f) / (b*c - a*d)

    if test_case.output:  # Testing if output dict is non-empty.
        logger.warning("Test case already has solution:")
        logger.warning("(x, y) = (%f, %f)", test_case.output['x'], test_case.output['y'])
        logger.warning("Overwriting with new solution.")

    test_case.output['x'] = x
    test_case.output['y'] = y

    logger.debug("Test case solution:")
    logger.debug("(x, y) = (%f, %f)", x, y)

    return


def test_our_solution():
    """Just a method used to test that our code all works (no errors) and that our solution is correct (which will
    probably involve some solution checking by humans). It should test the generate_input and solve_problem methods
    extensively. It will probably just be run occasionally to ensure our code still works in between updates."""
    # TODO: Should this be a unit test?
    # Just solve the test cases we already have from initialization and verify them.
    logger.info("Testing Problem1...")
    for tc in self.test_cases:
        self.solve_test_case(tc)
        if not self.verify_user_solution(tc.input_str(), tc.output_str()):
            # TODO: This should fail or throw an exception if something is wrong.
            # TODO: How should we be throwing exceptions? Should everything be in a try-catch block? Do this later?
            logger.critical("Our own solution is incorrect!")
    return


def verify_user_solution(user_input_str, user_output_str):
    """Given the user's input and output (solution) strings, verify that they have solved the problem correctly by
    solving the test case ourselves. Return True if their solution is correct, else False."""
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input_str)
    logger.debug("User output string: %s", user_output_str)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase1(TestCase1Type.UNKNOWN)

    inputs = list(map(float, user_input_str.split()))
    x1, y1, t1, x2, y2, t2, x3, y3, t3 = inputs

    tmp_test_case.input = {'x1': x1, 'y1': y1, 't1': t1,
                           'x2': x2, 'y2': y2, 't2': t2,
                           'x3': x3, 'y3': y3, 't3': t3}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    x = tmp_test_case.output['x']
    y = tmp_test_case.output['y']

    # Extract user solution.
    outputs = list(map(float, user_output_str.split()))
    user_x = outputs[0]
    user_y = outputs[1]

    # Compare our solution with user's solution.
    error_tol = TESTING_CONSTANTS['error_tol']
    error_distance = np.sqrt((x - user_x)**2 + (y - user_y)**2)  # [km]

    logger.debug("User solution:")
    logger.debug("(x, y) = (%f, %f)", user_x, user_y)
    logger.debug("Our solution:")
    logger.debug("(x, y) = (%f, %f)", x, y)
    logger.debug("Error tolerance = %e. Error distance: %e.", error_tol, error_distance)

    if error_distance < error_tol:
        logger.info("User solution correct within error margin.")
        return True
    else:
        logger.info("User solution incorrect within error margin.")
        return False
