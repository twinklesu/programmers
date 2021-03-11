from collections import deque
def solution(progresses, speeds):
    answer = []
    take_days = deque()
    for i in range(len(progresses)):
        take_days.append(ceil((100-progresses[i])/speeds[i]))
    pivot = take_days.popleft()
    count = 1
    while True:
        if take_days:
            tmp = take_days.popleft()
        else:
            answer.append(count)
            break
        if tmp > pivot:
            pivot = tmp
            answer.append(count)
            count =1
        else:
            count+=1
    return answer

def ceil(n):
    if n == int(n):
        return int(n)
    else:
        return int(n)+1