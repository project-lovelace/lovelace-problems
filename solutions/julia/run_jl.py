import julia

j = julia.Julia()
j.include("test-function.jl")

user_input = (3, 7, 12)

j.timed_function_call(j.test_function, user_input)  # Call function to pre/compile.
submission_output = j.timed_function_call(j.test_function, user_input)

user_output = submission_output[0]
runtime = submission_output[1]
bytes_allocated = submission_output[2]

# print(submission_output[0])
# print(submission_output[1])
#
# user_output = submission_output[0]
# runtime = submission_output[1]
#
print("User input: {:}".format(user_input))
print("User output: {:}".format(user_output))
print("Runtime: {:} seconds".format(runtime))
print("Memory allocated: {:} bytes".format(bytes_allocated))
