from collections import deque


def solution(skill, skill_trees):
    answer = len(skill_trees)
    for tree in skill_trees:
        skill_deq = deque(skill)
        s = skill_deq.popleft()
        for t in tree:
            if t in skill and t == s:
                if skill_deq:
                    s = skill_deq.popleft()
                else:
                    break
            elif t in skill and t != s:
                answer -= 1
                break
            else:
                pass

    return answer