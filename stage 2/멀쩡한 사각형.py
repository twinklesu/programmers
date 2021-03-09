def solution(w,h):
    answer = 1
    # 닮은 사각형 중 가장 작은 경우
    gcd = 1
    for i in range(w,0,-1):
        if w%i ==0 and h%i==0:
            gcd = i
            break
    x = w//gcd
    y = h//gcd

    rate = h/y
    notuse = x+y-1
    answer = w*h-notuse*rate
    return answer

# 최대공약수 함수
from math import gcd, lcm
gcd(w,h) #최대공약수
lcm(w,h) #최소공배수