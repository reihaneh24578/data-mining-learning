import numpy as np
arr = np.array([["reyhaneh", "reza", "javad"]])
narr = np.random.randint(0, 20, (1, 3))
print(f"enheraf meyar: {narr.std()}")
print(f"nomrat daneshjooyan: {narr}")
for x, y in zip(arr[0], narr[0]):
    print(f"nomre {x} is: {y}")
print(f"moadel: {np.mean(narr)}")
print(f"total: {np.sum(narr)}")
print(f"maximum: {np.max(narr)}")
print(f"minimum: {np.min(narr)}")
print(f"sorted: {np.sort(narr)}")
print(f"index less than 10: {np.where(narr < 10)}")

l = [int(x) for x in narr[0] if x < 10]
m = [int(x) for x in narr.flatten() if x >= 10]
t = [int(x) for x in narr.flatten() if x > np.mean(narr)]
print(f"score less than 10 of student: {m}")
print(f"score more than 10 of student: {l}")
print(f"score more than average of student: {t}")
