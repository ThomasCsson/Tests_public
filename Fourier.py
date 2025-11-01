import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad

def f(x):
    return x % (2 * np.pi) - np.pi


N = 100
x_values = np.linspace(-10,10,1000)
initial_y_values = []
for x in x_values:
    initial_y_values.append(f(x))
y_values = []
A_n,B_n = [],[]
all_values = []
functions = []
final_y_values = []


'''A_n part'''
for n in range(1,N):
    A = lambda x: math.cos(math.pi*n*x)
    s = lambda x: f(x)*A(x)

    result, error = quad(s,-math.pi,math.pi)
    A_n.append(result)
    A_func = lambda x: result*math.cos(n*x)
    for x in x_values:
        y_values.append(A_func(x))
    
    all_values.append(y_values)
    plt.plot(x_values,y_values)
    plt.title('Cosine part')
    functions.append(A_func)
    y_values = []
plt.show()


'''B_n part'''
for n in range(1,N):
    
    B = lambda x: math.sin(math.pi*x)
    s = lambda x: f(x)*B(x)
    result, error = quad(s,-math.pi,math.pi)
    B_n.append(result)
    B_func = lambda x: result*math.cos(n*x)
    print(result)
    for x in x_values:
        y_values.append(B_func(x))
    
    

    plt.plot(x_values,y_values)
    plt.title('Sine part')
    all_values.append(y_values)
    functions.append(B_func)
    y_values = []
plt.show()

'''Determine end function (sum of all sine/cosine functions)'''
for i in range(0,len(all_values[0])):
    sum = 0
    for j in range(0,len(all_values)):
        sum += all_values[j][i]
    final_y_values.append(sum)
plt.plot(x_values,final_y_values)
plt.plot(x_values, initial_y_values)
plt.show()

