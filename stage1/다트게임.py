def solution(dartResult):
    answer = 0
    value = []
    ten = False
    for ind, el in enumerate(dartResult):
        if el == '1':
            if dartResult[ind + 1] == '0':
                ten = True
            else:
                value.append(1)
        elif el == '0':
            if ten:
                value.append(10)
                ten = False
            else:
                value.append(0)
        elif el in '23456789':
            value.append(int(el))
        elif el == 'S':
            pass
        elif el == 'D':
            value[-1] = value[-1] ** 2
        elif el == 'T':
            value[-1] = value[-1] ** 3
        elif el == "*":
            if len(value) > 1:
                value[-2] = value[-2] * 2
            value[-1] = value[-1] * 2
        else:
            value[-1] = value[-1] * (-1)

    print(value)
    answer = sum(value)

    return answer