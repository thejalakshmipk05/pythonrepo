n = int(input())
flag = 1

if n <= 1:
    flag = 0
else:
    for i in range(2, n):
        if n % i == 0:
            flag = 0
            break

if flag == 1:
    print("Prime Number")
else:
    print("Not Prime")