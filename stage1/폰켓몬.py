def solution(nums):
    n = len(nums)/2
    distinct_set = set(nums)
    if len(distinct_set) > n:
        return n
    return len(distinct_set)