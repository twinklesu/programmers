def solution(priorities, location):
    answer = 0
    cursor = 0
    order = sorted(priorities, reverse=True)
    i = 0
    max_ = order[i]
    while(True):
        if priorities[cursor] == max_:
            answer += 1
            if cursor == location:
                break
            i += 1
            max_ = order[i]
            cursor += 1
        else:
            priorities.append(priorities[cursor])
            if location == 0:
                location = l
            l+= 1
            location -= 1
            cursor += 1
    return answer