def solution(n):
    answer = ''
    num = ["4","1","2"]
    answer = sol(n, num)
    return answer

def sol(n, num):
    if n<=3:
        return num[n%3]
    return sol((n-1)//3, num) + num[n%3]
