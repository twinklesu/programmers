def solution1(priorities, location):
    answer = 0
    while (True):
        for ind, el in enumerate(priorities):
            if el == max(priorities):
                answer += 1
                if ind == location:
                    return answer
                priorities[ind] = 0




from collections import deque

# deque이 pop append 가 리스트보다 월등히 빠르다
def solution(priorities, location):
    answer = 0
    deq = deque((i, el) for i, el in enumerate(priorities))

    while (True):
        tmp = deq.popleft()
        if any(tmp[1] < x[1] for x in deq):
            deq.append(tmp)
        else:
            answer += 1
            if tmp[0] == location:
                return answer
