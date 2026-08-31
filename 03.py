import numpy as np
coin = np.random.randint(0, 2, (1, 20))
print(f"0 --> shir, 1 --> khat: {coin}")
print(f"number of shir: {len(coin[coin == 0])}")
print(f"number of all: {len(coin.flatten())}")
print(f"ehtemal shir ha: {len(coin[coin == 0]) / len(coin.flatten())}")

tas = np.random.randint(1, 7, (10, 2))
print(f"tas: {tas}")
x = np.sum(tas, axis=1)
print(f"total row's: {x}")
count = 0
for i in range(len(x)):
    if x[i] == 7:
        count += 1
    
count1 = 0
for i in range(len(x)):
    if x[i] == 6:
        count1 += 1

count2 = 0
for i in range(len(x)):
    if x[i] == 5:
        count2 += 1

count3 = 0
for i in range(len(x)):
    if x[i] == 4:
        count3 += 1

count4 = 0
for i in range(len(x)):
    if x[i] == 3:
        count4 += 1

count5 = 0
for i in range(len(x)):
    if x[i] == 2:
        count5 += 1
    
count6 = 0
for i in range(len(x)):
    if x[i] == 1:
        count6 += 1

print(count, count1, count2, count3, count4, count5, count6)
print(f"ehtemal tozie 1: {count / len(tas)}")
print(f"ehtemal tozie 2: {count1 / len(tas)}")
print(f"ehtemal tozie 3: {count1 / len(tas)}")
print(f"ehtemal tozie 4: {count1 / len(tas)}")
print(f"ehtemal tozie 5: {count1 / len(tas)}")
print(f"ehtemal tozie 6: {count1 / len(tas)}")
print(f"ehtemal tozie 7: {count1 / len(tas)}")

