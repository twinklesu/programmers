def solution(n):
    l = n*(n+1)//2
    answer = [None]*l
    toRight = True
    cursor = 0
    step = 0
    for i in range(1, l+1):
        answer[cursor] = i
        if toRight:
            if (step == 1 and cursor+step == l):
                toRight = False
                step = n
                cursor -= step
            elif cursor+step > l:
                step = 1
                cursor += step
            else:
                step += 1
                cursor += step

        else:
            if (step == 1 and cursor-step == 0) or (answer[cursor-step] is not None):
                toRight = True
                step = 2
                cursor += step
            else:
                step -= 1
                cursor -= step
    return answer