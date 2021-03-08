def solution(N, stages):
    answer = []
    playerN = [0] * (N + 2)
    playerN[0] = None  # dummy
    for n in stages:
        for i in range(1, n + 1):
            playerN[i] += 1

    fail = []
    for i in range(1, N + 1):
        acc = sum(playerN[i:])
        if acc != 0:
            if playerN[i] == 0:
                fail.append([i, 1])
            else:
                fail.append([i, (playerN[i] - playerN[i + 1]) / acc])
        else:
            fail.append([i, 0])

    fail = sorted(fail, key=lambda x: x[1], reverse=True)
    for i in fail:
        answer.append(i[0])

    return answer
