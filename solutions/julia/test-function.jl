function timed_function_call(f, input)
    @timed f(input...)
end

function test_function(a, b, c)
    return (a, string(b), string(a)*string(b)*string(c), [a^2, b^2, c^3], (a^3, b^3, c^3))
end
