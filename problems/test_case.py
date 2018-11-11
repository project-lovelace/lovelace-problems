from enum import Enum


class TestCaseTypeEnum(Enum):
    def __init__(self, test_name, multiplicity):
        self.test_name = test_name
        self.multiplicity = multiplicity


class TestCase(object):    
    def __init__(self, test_type=None):
        self.test_type = test_type
        self.input = {}
        self.output = {}

    def input_tuple(self) -> tuple:
        pass

    def output_tuple(self) -> tuple:
        pass
