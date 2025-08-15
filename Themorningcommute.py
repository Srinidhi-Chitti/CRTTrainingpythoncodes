import sys

it = iter(sys.stdin.read().strip().split())
T = int(next(it))
out = []
for _ in range(T):
    n = int(next(it))
    t = 0
    for _ in range(n):
        x = int(next(it)); l = int(next(it)); f = int(next(it))
        if t <= x:
            t = x + l
        else:
            r = (t - x) % f
            if r != 0:
                t += f - r
            t += l
    out.append(str(t))
print("\n".join(out))
