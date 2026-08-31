import numpy as np
Matrix = np.array([[10, 15, 20, 16],
                                [14, 20, 17, 19],
                                [13, 15, 16, 18]])

print(f"nomarat droos math, english, python daneshjooyan: {Matrix}")
print(f"miyangin sotoon ha: {np.mean(Matrix, axis=0)}")
print(f"miyangin satrha ha: {np.mean(Matrix, axis=1)}")
#------------------------------------------------------
lis1 = []
for x in Matrix:
    lis1.append(float(np.mean(x)))
print(f"miangin satr ha: {lis1}")
print(f"max miangin: {max(lis1)}")

lis = []
for i in range(len(Matrix) + 1):
    avg = np.mean(Matrix[:, i])
    lis.append(float(avg))
print(f"mingin stoon ha: {lis}")
print(f"min miangin stoon ha: {min(lis)}")
