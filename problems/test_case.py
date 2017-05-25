from enum import Enum


class TestCaseTypeEnum(Enum):
    def __init__(self, test_name, debug_description, multiplicity):
        self.test_name = test_name
        self.debug_description = debug_description
        self.multiplicity = multiplicity


class TestCase:
    def __init__(self, test_type):
        self.test_type = test_type
        self.input = {}
        self.output = {}

    def input_str(self):
        """Should return the input string the user sees for this test case."""

    def output_str(self):
        """If the solution/output is known, this should return the output string expected by
        AbstractProblem.verify_user_solution."""