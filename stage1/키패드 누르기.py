def solution(numbers, hand):
    answer = ''
    left = 10
    right = 10
    two = {1: 1, 2: 0, 4: 2, 5: 1, 7: 3, 8: 2, 0: 3, 10: 4}
    five = {1: 2, 2: 1, 4: 1, 5: 0, 7: 2, 8: 1, 10: 3, 0: 2}
    eight = {1: 3, 2: 2, 4: 2, 5: 1, 7: 1, 8: 0, 10: 2, 0: 1}
    zero = {1: 4, 2: 3, 4: 3, 5: 2, 7: 2, 8: 1, 10: 1, 0: 0}
    mid = {2: two, 5: five, 8: eight, 0: zero}

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num - 2
        elif mid[num][left] == mid[num][right]:
            if hand == 'left':
                left = num
                answer += 'L'
            else:
                right = num
                answer += 'R'
        elif mid[num][left] > mid[num][right]:
            right = num
            answer += 'R'
        else:
            left = num
            answer += 'L'

    return answer

# 좌표축 이용해서 풀기
def solution1(numbers, hand):
    answer = ''
    xy = {1: (0, 3), 2: (1, 3), 3: (2, 3),
          4: (0, 2), 5: (1, 2), 6: (2, 2),
          7: (0, 1), 8: (1, 1), 9: (2, 1),
          '*': (0, 0), 0: (1, 0), '#': (2, 0)}

    left = '*'
    right = '#'

    for num in numbers:
        if num in [1, 4, 7]:
            left = num
            answer += 'L'
        elif num in [3, 6, 9]:
            right = num
            answer += 'R'
        else:
            dist_l = abs(xy[left][0] - xy[num][0]) + abs(xy[left][1] - xy[num][1])
            dist_r = abs(xy[right][0] - xy[num][0]) + abs(xy[right][1] - xy[num][1])
            if dist_l < dist_r:
                left = num
                answer += 'L'
            elif dist_l > dist_r:
                right = num
                answer += 'R'
            elif hand == 'left':
                left = num
                answer += 'L'
            else:
                right = num
                answer += 'R'

    return answer