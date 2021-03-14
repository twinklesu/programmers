def solution(prices):
    answer = []
    l=len(prices)
    for i, el in enumerate(prices):
        count = 0
        for j in range(i+1,l):
            if el > prices[j]:
                count += 1
                break
            else:
                count += 1
        answer.append(count)
    return answer