import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import time

'''Enter function here: '''
'''Careful to use notation that python will understand (math is imported)'''
f = lambda x: math.sin(x**2)

x_values = np.linspace(-10, 10, 1000)
y_values = []
'''Number of iterations that will be run'''
N = 50
A_n, B_n = [], []

'''Have to manually enter period of function'''
period = 2 * math.pi

for x in x_values:
    y_values.append(f(x))

# Set up subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 12))
fig.tight_layout(pad=5.0)

# Plot 1: Given function
axs[0].plot(x_values, y_values)
axs[0].set_title('Given function')

start = time.time()

a_0 = (1 / period) * (quad(f, -period / 2, period / 2)[0])
final_y = [a_0 / 2] * len(x_values)
axs[1].plot(x_values, final_y)

for n in range(1, N):
    y_values_cos, y_values_sin = [], []
    func_cos = lambda x: math.cos(n * x)
    final_cos = lambda x: f(x) * func_cos(x)
    a_n = (2 / period) * (quad(final_cos, -period / 2, period / 2)[0])
    A_n.append(a_n)
    func_sin = lambda x: math.sin(n * x)
    final_sin = lambda x: f(x) * func_sin(x)
    b_n = (2 / period) * (quad(final_sin, -period / 2, period / 2)[0])
    B_n.append(b_n)
    for x in x_values:
        y_values_cos.append(a_n * math.cos(n * x))
        y_values_sin.append(b_n * math.sin(n * x))
    axs[1].plot(x_values, y_values_sin)
    axs[1].plot(x_values, y_values_cos)
    for i in range(len(x_values)):
        final_y[i] = final_y[i] + y_values_cos[i] + y_values_sin[i]

end = time.time()

axs[1].set_title('Individual functions that will compose the Fourier series')

# Plot 3: Final function
axs[2].plot(x_values, final_y)
axs[2].set_title('Final function')

plt.show()

print(f'Computation time: {end - start} s')
'''print(A_n, B_n)'''
