def solvedeadlysin(x,y):
    while x!=0 and y!=0 and x!=y:
        if x>y:
            y-=x
        else:
            x-=y
    return x+y
T= int(input())
for _ in range(T):
    x,y= map(int,input().split())
    print(solvedeadlysin(x,y))
