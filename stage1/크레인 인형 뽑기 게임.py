def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for ind, el in enumerate(board):
            if el[i-1] != 0:
                basket.append(el[i-1])
                board[ind][i-1] = 0
                if len(basket) >= 2 and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    answer += 2
                break
    return answer