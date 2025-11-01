import numpy as np
import math



def period_finder(x_values, y_values):
    epsilon = 0.000000000000001
    for i in range(2,len(x_values)):
        if y_values[i]- y_values[0]< epsilon:
            if y_values[i+1] - y_values[1]< epsilon:
                period = x_values[i]-x_values[0]
                return period
    return f'No period was found'

x_values = np.linspace(-10,10,10000)
f = lambda x: math.sin(x)
y_values = []
for x in x_values:
    y_values.append(f(x))
print(period_finder(x_values,y_values))