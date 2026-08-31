import numpy as np

x = np.array([2, 3, 4, 5, 6])
y = np.array([4, 6, 8, 10, 12])

x_mean = np.mean(x)
y_mean = np.mean(y)

a = (x - x_mean) * (y - y_mean)
print(a)
b = np.sum(a)
c = (x - x_mean) ** 2
d = np.sum(c)
e = b / d
print(e)
f = y_mean - e * x_mean
print(f)

print(f"y = {e} x + {f}")
