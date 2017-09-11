from enum import Enum


class TestCaseTypeEnum(Enum):
    def __init__(self, test_name, debug_description, multiplicity):
        self.test_name = test_name
        self.debug_description = debug_description
        self.multiplicity = multiplicity


class TestCase(object):
    def __init__(self, test_type):
        self.test_type = test_type
        self.input = {}
        self.output = {}

    def input_str(self) -> str:
        pass

    def output_str(self) -> str:
        pass
