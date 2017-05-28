# Project Lovelace problem repository

## How to create a problem
Every problem is a module containing three mandatory functions that [lovelace-engine](https://github.com/project-lovelace/lovelace-engine) expects the problem module to have implemented otherwise user submissions cannot be tested. Problem modules must also implement the test case data structures in [`test_case.py`](problems/test_case.py), namely the `TestCase` and `TestCaseTypeEnum` classes. Finally, each problem must provide some metadata about itself in the form of a `ProblemMetadata` object.

[`problem_template.py`](problems/problem_template.py) provides all this boilerplate needed to create a problem.

### Problem module functions
#### Mandatory
* `generate_input(test_type: TestCaseTypeEnum) -> TestCase`: Creates the input(s) for a problem of type `test_type` and returns a TestCase object. The test case's inputs are stored in the `input` dictionary of a `TestCase` object. If the solution is known at this time, it should be included in the `output` dictionary, but there is no expectation that the solution will be included.

* `solve_test_case(test_case: TestCase) -> None`: Solve the problem described by `test_case` in its `input` dictionary and update its `output` dictionary with the full solution.

* `user_solution_correct(user_input_str: str, user_output_str: str) -> bool`: Given the user's input and output (solution) strings, verify that they have solved the problem correctly. Returns True if their solution is correct, otherwise False.

#### Optional (as needed)
* `generate_test_cases() -> List[TestCase]`: if `CUSTOM_TEST_CASE_GENERATION` is `True`.

### Test case types
A class inherited from `TestCaseTypeEnum` should contain all the different types of test cases. It will typically be called `TestCaseXType` where `X` is the problem's integer ID. Modeled after the [Planet Enum example](https://docs.python.org/3/library/enum.html#planet) from the official Python documentation. Each test case type has three values:
* `test_name`: A short name describing the test case, e.g. general case, sphere, lorem ipsum, n=2 case, glider gun. This will be shown to the user so it should be descriptive enough to be useful to them.
* `debug_description` (optional): A longer, more detailed description of the test case in case this extra description helps in debugging issues. Might also be useful as an 
* `multiplicity`: The number of times this test case should be used, e.g. you might want to test the user's code against three general cases but only one n=2 case.

### Test case structure
* `TestCase`: The input and output dictionaries should never be accessed outside of the problem module so it is up to you to store input/outputs in them in any way. The engine will access them using methods like `input_str()` and `output_str()`. Will typically be called `TestCaseX` where `X` is the problem's integer ID.

#### Minimal structure
All `TestCase` classes must implement these functions and methods.
* `test_type`: of type `TestCaseXType`.
* `input`: dictionary holding all the inputs.
* `output`: dictionary holding all the outputs.
* `input_str() -> str`: Returns the input string the user sees for this test case.
* `output_str() -> str`: If the solution/output is known, return the output string expected by `user_solution_correct()`.

#### Optional (as needed)
* `aux_dict() -> dict`: See `AUXILIARY_DICTIONARY`.

### Problem metadata
The metadata stores some actual metadata but is mostly used to instruct the engine on how to process test cases for this problem and what information to send back to the user/client and in what form.
* `PROBLEM_ID`: the problem's integer ID. These are assigned manually, usually incrementally as problems are created.
* `PROBLEM_NAME`: the problem's name in snake_case (lower_case_with_underscores).
* `TEST_CASE_TYPE_ENUM`: points to the problem's TestCaseTypeEnum class. The engine requires this so it can iterate over all test case types.
* `CUSTOM_TEST_CASE_GENERATION`: If `True`, the problem module must specify a custom test case generation scheme implemented as `generate_test_cases() -> List[TestCase]`. If `False`, then the engine simply iterates over all test case types in `TEST_CASE_TYPE_ENUM` accounting for test case multiplicity and creates test cases using `generate_input()`.
* `AUXILIARY_DICTIONARY`: If `True`, `TestCase` must implement a `aux_dict()` function that returns a dict to be sent to the client in the HTTP response called `aux_dict`. Mostly used by the client to plot/illustrate test cases when more data is needed than is provided by `input_str()` and `output_str(), or when the data is needed in a more convinient format, e.g. as a list or dict.

#### Future features?
* `INPUT_RESPONSE_TYPE`, `OUTPUT_RESPONSE_TYPE`: `FULL_TEXT`, `HYPERLINK`, or `NONE`. Future problems may need e.g. `IMAGE` or `AUDIO`.
* `INPUT_FEED_METHOD`: `STDIN`, `ONE_FILE`, or `MULTIPLE_FILES`.
* `OUTPUT_READ_METHOD`: `STDOUT`, `ONE_FILE`, or `MULTIPLE_FILES`.
