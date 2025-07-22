import math
import sys
input= sys.stdin.readline
i,k,s= map(int, input().split())
a_i,b_i= map(float, input().split())
x= math.sqrt(2)
y= math.sqrt(3)
power_diff= k-i
a_k=a_i*pow (x, power_diff)
b_k=b_i*pow (y, power_diff)
denominator= pow(2,s)
Q=a_k+b_k / denominator
print(Q)

