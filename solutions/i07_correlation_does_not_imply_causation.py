import csv
import numpy as np

csv_filename = input()

x = []
y = []

with open(csv_filename) as csvfile:
    xy_reader = csv.reader(csvfile, delimiter=',')
    for row in xy_reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

N = len(x)
x = np.array(x)
y = np.array(y)

x_bar = x.mean()
y_bar = y.mean()

cov_XY = 0
sigma_X = 0
sigma_Y = 0

for i in range(N):
    cov_XY = cov_XY + (x[i] - x_bar)*(y[i] - y_bar)
    sigma_X = sigma_X + (x[i] - x_bar)**2
    sigma_Y = sigma_Y + (y[i] - y_bar)**2

sigma_X = np.sqrt(sigma_X)
sigma_Y = np.sqrt(sigma_Y)

r = cov_XY / (sigma_X * sigma_Y)

print('{}'.format(r))
