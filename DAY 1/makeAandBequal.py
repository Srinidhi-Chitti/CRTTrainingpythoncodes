T=int(input())
for _ in range(T):
    a,b= map(int, input().split())

    while a % 2 == 0:
        a // 2

    while b % 2 == 0:
        b // 2

    if a == b:
        print("yes")
    else:
        print("no")
