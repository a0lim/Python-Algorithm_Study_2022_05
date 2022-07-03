n = int(input())
#한수 x
x = 0

for i in range(1, n+1):
    if i <100:
        x += 1
    else:
        num = list(str(i))
        if int(num[2])- int(num[1]) == int(num[1]) - int(num[0]):
            x += 1

print(x)