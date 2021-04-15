from itertools import permutations

def solution(a_, edges):
    li = []
    comb = list(permutations(edges,len(edges)))
    for ed in comb:
        a = a_.copy()
        count = 0
        for edge in ed:
            n1 = a[edge[0]]
            n2 = a[edge[1]]
            adding = max(abs(n1), abs(n2))
            count += adding
            if n1+adding == 0 or n2-adding == 0:
                a[edge[0]] += adding
                a[edge[1]] -= adding
            else:
                a[edge[0]] -= adding
                a[edge[1]] += adding
        if sum(a) == 0:
            li.append(count)
    if li:
        return min(li)
    else:
        return -1