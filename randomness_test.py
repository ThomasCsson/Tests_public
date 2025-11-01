import random
import time
import matplotlib.pyplot as plt

random_ints = []
random_ints_occ = []
x = []
n = 100000      #dont use larger than 10^6
start = time.time()

while n:
    random_ints.append(random.randint(0,100))
    n -= 1

for i in range(0,100+1):
    random_ints_occ.append(random_ints.count(i))
    x.append(i)

plt.plot(x,random_ints_occ)
    


end = time.time()
print(f'Time = {end-start}')

plt.show()
