def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    corr_set = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    isComma = False
    for l in new_id:
        if l not in corr_set:
            pass
        elif l == ".":
            if isComma:
                pass
            else:
                isComma=True
                answer += l
        else:
            isComma = False
            answer += l

    """
        while '..' in answer:
        answer = answer.replace('..', '.')
        이걸로 하면 . 제거 다 됨...
    """

    if answer and answer[0] == ".":
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]
    if answer == "":
        answer = 'a'
    if len(answer) >= 15:
        answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:-1]
    while len(answer) <= 2:
        answer += answer[-1]

    return answer