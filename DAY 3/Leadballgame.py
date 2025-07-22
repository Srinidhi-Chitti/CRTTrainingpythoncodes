T= int(input())
m1=0
m2=0
p1=0
p2=0
for _ in range(T):
    a,b=map(int, input().split())
    m1 += a
    m2 += b
    if m1>m2:
        p1= print(max(p1, m1-m2))
    else:
        p2= print(max(p2, m2-m1))
if p1>p2:
    print(1,p1)
else:
    print(2,p2)