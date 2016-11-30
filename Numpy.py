import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from numpy.random import rand
from numpy.random import normal,rand

A = np.random.randint(10, size=(2,2))
B = np.random.randint(10, size=(2,2))

for row in A:
	print(row)

for row in B:
	print(row)

E = A * B

for row in E:
	print(row)

E = A.transpose()
for row in E:
	print(row)

ainv = inv(A)
for row in ainv:
	print(row)

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
r = np.cos(2*np.pi*t)
plt.plot(t,s)
plt.plot(t,r)
plt.show()

x = normal(size = 1000)
plt.hist(x, bins = 100)
plt.show()
plt.cla()

a = rand(1000)
b = rand(1000)
plt.scatter(a,b)
plt.show()
