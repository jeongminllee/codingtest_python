# 10진수를 2진수로 변환하기
def solution(decimal) :
    stack = []
    while decimal > 0 :
        n = decimal % 2     # decimal 을 2로 계속 나누고 그에 대한 나머지 값을 구함
        stack.append(str(n))# 나머지 값을 stack에 추가
        decimal //= 2       # 2로 나눈 decimal 값으로 초기화
    stack.reverse()
    return ''.join(stack)

de = 10
print(solution(de)) # 1010

de = 27
print(solution(de)) # 11011

de = 12345
print(solution(de)) # 11000000111001
'''
10진수를 2진수로 변환하는 과정을 살펴보면, 
10은 10, 5, 2, 1, 0의 몫을 얻고
나머지는 0, 1, 0, 1 을 얻게 된다. 

이를 뒤집어 읽으면 10에 대한 2진수를(1010)을 얻을 수 있다. 
'''