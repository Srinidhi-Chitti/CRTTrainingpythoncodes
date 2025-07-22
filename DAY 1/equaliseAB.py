T = int(input())

for _ in range(T):
    A, B, X = map(int, input().split())
    
    if (A + B) % 2 != 0:
        print("NO")
    elif abs(A - B) % (2 * X) == 0:
        print("YES")
    else:
        print("NO")
