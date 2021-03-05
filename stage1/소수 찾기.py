def solution(n):
    answer = n - 1
    # 에라토스테네스의 체

    prime = []
    for i in range(2, int(n ** 0.5) + 2):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            prime.append(i)
            answer += 1
    # 체
    for i in range(2, n + 1):
        for j in prime:
            if i % j == 0:
                answer -= 1
                break
    return answer

# 모범 답안 참고해서 짠거
def solution(n):
    num = set(range(2, n+1))
    for i in range(2, int(n**0.5)+2):
        num -= set(range(i*2, n+1, i))
    answer = len(num)
    return answer
