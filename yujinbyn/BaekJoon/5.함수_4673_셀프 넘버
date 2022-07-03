number1 = set(range(1, 10001))
number2 = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    number2.add(i)

self_num = sorted(number1 - number2)
for i in self_num:
    print(i)
