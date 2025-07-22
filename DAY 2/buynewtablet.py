#budget is b, can't buy tablet>b, area of tablet large,
#screen is rectangle,
#n tablets(1-n) wi-width, height-hi and price-pi
T= int(input())
for _ in range(T):
    N,B= map(int, input.split())
    max_area=0

    for _ in range(N):
        W,H,P= map(int,input.split())

        if P<=B:
            area= W*H
            
        if area>max_area:
            area=max_area

    if max_area==0:
        print("Nothing")
    else:
        print(max_area)


