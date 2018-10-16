# Project Lovelace problem module and solution repository

As of alpha2018 this is under construction...

## How to create a problem module
Every problem is a module containing three mandatory functions that [lovelace-engine](https://github.com/project-lovelace/lovelace-engine) expects the problem module to have implemented otherwise user submissions cannot be tested. Problem modules must also implement the test case data structures in [`test_case.py`](problems/test_case.py), namely the `TestCase` and `TestCaseTypeEnum` classes. Finally, each problem must provide some metadata about itself stored as module variables.

See [`problem_template.py`](problems/problem_template.py) for an example. It provides all this boilerplate needed to create a problem module.

### Problem module variables and metadata
The metadata stores some actual metadata but is mostly used to instruct the engine on how to process test cases for this problem and what information to send back to the user/client and in what form.
* `PROBLEM_ID`: the problem's integer ID. These are assigned manually, usually incrementally as problems are created.
* `PROBLEM_NAME`: the problem's name in snake_case (lower_case_with_underscores).
* `TEST_CASE_TYPE_ENUM`: points to the problem's `TestCaseTypeEnum` class. The engine requires this so it can iterate over all test case types.
* `STATIC_RESOURCES`: list of filenames indicating files that must be placed in the current working directory before running any test case. They are required by the solution for at least one test case (and possibly by all test cases). These are usually files that do not change between submissions and are available before test case generation.
* `DYNAMIC_RESOURCES`: list of filenames indicating files that must be copied into the current working directory before running each test case. These are usually files that are generated on-the-fly during test case generation to create random inputs.
* `PHYSICAL_CONSTANTS`: dictionary of physical constants used in the solution of the problem. This dictionary is internal to the problem module. Example contents include the radius of the Earth, the speed of the baseball in the problem (if constant between test cases), or the speed of light.
* `TESTING_CONSTANTS`: dictionary of constants used in the testing and verification of user submissions. This dictionary is internal to the problem module. Example contents include the floating-point error tolerance of the solution.

### Creating test cases

#### Creating test case types
A class inherited from `TestCaseTypeEnum` should contain all the different types of test cases. It will typically be called `TestCaseXType` where `X` is the problem's integer ID. Modeled after the [Planet Enum example](https://docs.python.org/3/library/enum.html#planet) from the official Python documentation. Each test case type has two values:
* `test_name`: A short name describing the test case, e.g. general case, sphere, lorem ipsum, n=2 case, glider gun. This will be shown to the user so it should be descriptive enough to be somewhat useful to them.
* `multiplicity`: The number of times this test case should be used, e.g. you might want to test the user's code against three general cases but only one sphere case.

#### Test case structure
* `TestCase`: The input and output dictionaries should never be accessed outside of the problem module so it is up to you to store input/outputs in them in any way. The engine will access them using `input_tuple()` and `output_tuple()`. The class will typically be called `TestCaseX` where `X` is the problem's integer ID.

All `TestCase` classes must implement these functions and methods.
* `test_type`: An enum of type `TestCaseXType` indicating the test case's type.
* `input`: dictionary holding all the inputs for internal use.
* `output`: dictionary holding all the outputs for internal use.
* `input_tuple() -> tuple`: Returns a tuple containing the input arguments in the correct order so that it can be used to call the user's submitted function directly.
* `output_tuple() -> str`: If the solution/output is known, returns a tuple containing the correct output arguments of the user's submitted function in the correct order.

### Problem module functions
* `generate_input(test_type: TestCaseTypeEnum) -> TestCase`: Creates the input(s) for a problem of type `test_type` and returns a `TestCase` object. The test case's inputs are stored in the `input` dictionary of a `TestCase` object. If the solution is known at this time, it should be included in the `output` dictionary, but there is no expectation that the solution will be included.

* `solve_test_case(test_case: TestCase) -> None`: Solve the problem described by `test_case` in its `input` dictionary and populate its `output` dictionary with the full solution.

* `user_solution_correct(user_input: tuple, user_output: tuple) -> bool`: Given the user's input and output (solution) tuples, verify that they have solved the problem correctly. Returns True if their solution is correct (or at least correct to within specific tolerances), otherwise False.
