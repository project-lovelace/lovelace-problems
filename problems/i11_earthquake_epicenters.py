import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCase11Type(TestCaseTypeEnum):
    GENERAL = ('General case', 3)
    ZERO_CASE = ('Zero case', 1)
    EQUIDISTANT = ('Equidistant case', 1)


class TestCase11(TestCase):
    def input_tuple(self) -> tuple:
        input_str = str(self.input['x1']) + ' ' + str(self.input['y1']) + ' ' + str(self.input['t1']) + ' '
        input_str += str(self.input['x2']) + ' ' + str(self.input['y2']) + ' ' + str(self.input['t2']) + ' '
        input_str += str(self.input['x3']) + ' ' + str(self.input['y3']) + ' ' + str(self.input['t3'])
        return (self.input['x1'], self.input['y1'], self.input['t1'],
        	self.input['x2'], self.input['y2'], self.input['t2'],
        	self.input['x3'], self.input['y3'], self.input['t3'])

    def output_tuple(self) -> tuple:
        return (self.output['x'], self.output['y'])


TEST_CASE_TYPE_ENUM = TestCase11Type
TEST_CASE_CLASS = TestCase11

STATIC_RESOURCES = []

# Problem-specific constants.
PHYSICAL_CONSTANTS = {
    'v': 3.0  # [km/s], velocity of seismic waves
}

TESTING_CONSTANTS = {
    'error_tol': 0.0001  # [km]
}


def generate_test_case(test_type: TestCase11Type) -> TestCase11:
    if not isinstance(test_type, TestCase11Type):
        logger.critical('test_type is not of type TestCase11Type!')
        raise TypeError('test_type is not of type TestCase11Type!')

    test_case = TestCase11(test_type)
    logger.debug("Generating %s...", test_type.test_name)

    if test_type is TestCase11Type.GENERAL:
        r0 = np.random.uniform(-100, 100, 2)
        r1 = np.random.uniform(-100, 100, 2)
        r2 = np.random.uniform(-100, 100, 2)
        r3 = np.random.uniform(-100, 100, 2)
    elif test_type is TestCase11Type.ZERO_CASE:
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
    elif test_type is TestCase11Type.EQUIDISTANT:
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

    # Convert to float so the user gets Python floats and not numpy floats.
    test_case.input = {
    	'x1': float(r1[0]),
    	'y1': float(r1[1]),
    	't1': float(t1),
    	'x2': float(r2[0]),
    	'y2': float(r2[1]),
    	't2': float(t2),
    	'x3': float(r3[0]),
    	'y3': float(r3[1]),
    	't3': float(t3)
    }

    logger.debug("Test case input:")
    logger.debug("(x1, y1, t1) = (%f, %f, %f)", r1[0], r1[1], t1)
    logger.debug("(x2, y2, t2) = (%f, %f, %f)", r2[0], r2[1], t2)
    logger.debug("(x3, y3, t3) = (%f, %f, %f)", r3[0], r3[1], t3)

    test_case.output['x'] = r0[0]
    test_case.output['y'] = r0[1]

    logger.debug("Test case solution available at creation:")
    logger.debug("(x, y) = (%f, %f)", r0[0], r0[1])

    return test_case


def solve_test_case(test_case: TestCase11) -> None:
    v = PHYSICAL_CONSTANTS['v']

    x1, y1, t1 = test_case.input['x1'], test_case.input['y1'], test_case.input['t1']
    x2, y2, t2 = test_case.input['x2'], test_case.input['y2'], test_case.input['t2']
    x3, y3, t3 = test_case.input['x3'], test_case.input['y3'], test_case.input['t3']

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


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase11()

    x1, y1, t1, x2, y2, t2, x3, y3, t3 = user_input

    tmp_test_case.input = {'x1': x1, 'y1': y1, 't1': t1,
                           'x2': x2, 'y2': y2, 't2': t2,
                           'x3': x3, 'y3': y3, 't3': t3}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    x = tmp_test_case.output['x']
    y = tmp_test_case.output['y']

    # Extract user solution.
    user_x, user_y = user_output

    # Compare our solution with user's solution.
    error_tol = TESTING_CONSTANTS['error_tol']
    error_distance = np.sqrt((x - user_x)**2 + (y - user_y)**2)  # [km]

    logger.debug("User solution:")
    logger.debug("(x, y) = (%f, %f)", user_x, user_y)
    logger.debug("Our solution:")
    logger.debug("(x, y) = (%f, %f)", x, y)
    logger.debug("Error tolerance = %e. Error distance: %e.", error_tol, error_distance)

    if error_distance < error_tol:
        logger.info("User solution correct within error tolerance of {:g}.".format(error_tol))
        return True
    else:
        logger.info("User solution incorrect.")
        logger.info("Error tolerance = %e. Error distance: %e.", error_tol, error_distance)
        return False
