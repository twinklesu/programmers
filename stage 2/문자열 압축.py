def solution(s):
    answer = 0
    l = len(s)
    min_len = l
    for n in range(1,l):
        shorted = ""
        tail = n
        now = s[0:tail]
        count = 1
        while tail<=l:
            next_ = s[tail:tail+n]
            if next_ == now:
                count += 1
            else:
                if count == 1:
                    shorted += now
                else:
                    shorted += str(count) + now
                now = next_
                count = 1
            tail = tail+n
        shorted += now
        shorted_len = len(shorted)
        if shorted_len < min_len:
            min_len = shorted_len
    answer = min_len
    return answer