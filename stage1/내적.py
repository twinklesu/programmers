def solution(a, b):
    answer = 0
    for i, _ in enumerate(a):
        answer += a[i]*b[i]
    return answer

"""
    for i,j in zip(a,b):
        answer+=i*j
    zip 활용하기!!!!!!
"""