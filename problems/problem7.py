import logging

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')


class TestCase7Type(TestCaseTypeEnum):
    GENERAL = ('general case', '', 1)
    UNKNOWN = ('unknown case', '', 0)


class TestCase7(TestCase):
    def input_str(self) -> str:
        return self.input['text']

    def output_str(self) -> str:
        s = ''
        for char in 'abcdefghijklmnopqrstuvwxyz':
            s += char + ' ' + str(self.output.freq[char]) + '\n'
        return s


TEST_CASE_TYPE_ENUM = TestCase7Type
TEST_CASE_CLASS = TestCase7


def generate_input(test_type: TestCase7Type) -> TestCase7:
    test_case = TestCase7(test_type)
    if test_type == TestCase7Type.GENERAL:
        from os import path
        filepath = path.join(path.dirname(path.abspath(__file__)), 'resources', 'problem7', 'moby_dick_chapter1.txt')
        with open(filepath, 'r') as fin:
            text = fin.read().replace('\n', '')
    else:
        text = ''

    test_case.input['text'] = text
    solve_test_case(test_case)
    return test_case


def solve_test_case(test_case: TestCase7) -> None:
    text = test_case.input['text']
    freq = {}
    n_char = 0

    for char in 'abcdefghijklmnopqrstuvwxyz':
        freq[char] = 0

    for char in text:
        if char.isalpha():
            c = char.lower()
            freq[c] += 1
            n_char += 1

    # Normalize frequencies so they sum to 1.
    # for char in freq.keys():
    #     freq[char] = freq[char] / n_char

    test_case.output['freq'] = freq
    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input_str)
    logger.debug("User output string: %s", user_output_str)

    # Build TestCase object out of user's input string.
    test_case = TestCase7(TestCase7Type.UNKNOWN)
    test_case.input = {'text': user_input_str}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(test_case)

    # Extract user solution.
    outputs = user_output_str.split()
    user_freq = {}
    for i in range(0, len(outputs), 2):
        char = outputs[i].lower()
        char_freq = int(outputs[i+1])
        user_freq[char] = char_freq

    # Compare our solution with user's solution.
    frequency_dict_matches = True if user_freq == test_case.output['freq'] else False

    if frequency_dict_matches:
        logger.info("User solution correct.")
        return True
    else:
        logger.info("User solution incorrect.")
        return False
