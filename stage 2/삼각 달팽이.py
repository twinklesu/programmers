def solution(n):
    l = n * (n + 1) // 2
    answer = [None] * (l)
    now = 0
    step = 1
    isRight = True
    for i in range(1, l + 1):
        print("now: ", now)
        print("step: ", step)
        answer[now] = i
        print(answer)
        if isRight:
            if now + step >= l:
                print("case 1")
                now += 1
            elif now + step < l and answer[now + step] is None:
                print("case 2")
                now += step
                step += 1
            if now == l:
                isRight = False
                step = n - 1
                now -= (n + 1)
        else:
            if now - step <= 0:
                print("case 3")
                now -= 1
            elif now - step > 0 and answer[now - step] is None:
                print("case4")
                now -= step
                step -= 1
                print("case4 now: ", now)
                print("case4 step: ", step)
            if answer[now] is not None:
                isRight = True
                step = 2
                now += step
    return answer

