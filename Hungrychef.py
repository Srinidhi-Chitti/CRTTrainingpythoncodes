t = int(input())

for _ in range(t):
    X, Y, N, R = map(int, input().split())

    min_cost = N * X
    max_cost = N * Y

    if R < min_cost:
        print(-1)
        continue

    if R >= max_cost:
        print(0, N)
        continue

    premium = (R - N * X) // (Y - X)
    if premium > N:
        premium = N

    normal = N - premium
    print(normal, premium)
