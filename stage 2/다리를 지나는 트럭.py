from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = bridge_length

    bridge = deque([0] * bridge_length)
    total = 0

    for t in truck_weights:
        while True:
            answer += 1
            total -= bridge.popleft()
            if total + t <= weight:
                bridge.append(t)
                total += t
                break
            else:
                bridge.append(0)
    return answer

# for 문 내에서 sum 쓸경우 변수 따로 두고 쓰는게 빠름. 자꾸 순회 돌면 안좋으니까