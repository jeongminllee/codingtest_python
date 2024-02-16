def solution(s) :
    stack = []                  # 스택 초기화
    for i in range(len(s)) :
        if s[i] == '(' :
            stack.append(s[i])

        else :
            if '(' in stack :   # stack 에 '(' 이 있다면
                stack.pop()
            else :              # stack에 '(' 이 없다면
                return False

    if len(stack) == 0 :        # 쌍이 알맞게 구성되었다면
        return True
    return False                # 아니라면,

s = "(())()"
print(solution(s))  # True

s = "((())()"
print(solution(s))  # False