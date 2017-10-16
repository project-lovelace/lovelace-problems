input_str = str(input())
input_list = input_str.split()
problem = [float(number) for number in input_list]

r = problem[0]

x = [0.5]
print(x[0])

for _ in range(50):
    x.append(r * x[-1] * (1 - x[-1]))
    print(x[-1])