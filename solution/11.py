def solution(s) :
    stack = []
    for i in s :
        if stack and i == stack[-1] :   # stack이 비어있지 않고, 마지막 문자가 i와 같다면
            stack.pop()
        else :
            stack.append(i)

    return int(not stack)   # stack이 비었으면 1, 아니라면 0

s = 'baabaa'
print(solution(s))  # 1

s = 'cdcd'
print(solution(s))  # 0