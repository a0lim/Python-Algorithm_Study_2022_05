n = int(input())

for i in range(n):
    R, S = input().split()
    x =''
    for j in S:
        x += int(R)*j 
    print(x)