def solution(nums):
    answer = 0
    candidate = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                candidate.append(nums[i]+nums[j]+nums[k])
    for num in candidate:
        if isPrime(num):
            answer += 1
    return answer



def isPrime(num):
    for n in range(2,num):
        if num%n ==0:
            return False
    return True