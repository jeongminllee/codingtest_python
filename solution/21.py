def solution(want, number, discount):
    # 총 일수를 계산할 변수 초기화
    answer = 0

    # want 리스트를 딕셔너리로 변환
    want_dic = {}
    for i in range(len(want)) :
        want_dic[want[i]] = number[i]

    # 특정일 i에 회원가입 시 할인받을 수 있는 품목 체크
    for i in range(len(discount) - 9) :
        discount_10d = {}   # i일 회원가입 시 할인받는 제품 및 개수를 담을 딕셔너리

        # i일 회원가입 시 할인받는 제품 및 개수로 딕셔너리 구성
        for j in range(i, i + 10) :
            if discount[j] in want_dic :
                discount_10d[discount[j]] = discount_10d.get(discount[j], 0) + 1

            # 할인하는 상품의 개수가 원하는 수량과 일치하면 정답 변수에 1 추가
            if discount_10d == want_dic :
                answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(['apple'], [10], ['banana','banana','banana','banana','banana','banana','banana','banana','banana','banana']))

'''
회원을 대상으로 매일 한 가지 제품을 할인함 - 하루에 하나씩만 구매 가능
나는 내가 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치하는 경우에 맞춰서 회원가입을 하려고 함

특정일에 회원 강비을 해 그날부터 10일간 쇼핑을 할 때 구매하려는 제품을 모두 할인받아 살 수 있는지 확인하고 
특정일을 세어 반환하면 됨. 문제를 풀기 전에 입력값부터 분석

want : 구매하고자 하는 제품
number : want를 얼마나 사고 싶은지
discount : 마트에서 각 날짜마다 할인하는 제품 정보

want : number 는 서로 깊은 연관이 있어보임
want[0] = 'banana'
number[0] = 3

이를 연결지어 생각하면 number[want[0]] = 3

특정 일에 회원가입을 함녀 할인받을 수 있는 품목과 품목의 개수를 딕셔너리로 만들기
문제를 풀려면 특정 일에 회원가입 시 할인받을 수 있는 제품과 제품의 개수가 필요함. 첫 번째 입출력 예를 기준으로
첫 번째, 두 번째 날 할인받을 수 있는 품목과 품목의 개수를 딕셔너리로 만들면 됨.

우리가 딕셔너리로 표현한 것은 다음 두 가지 항목
- 내가 사려고 하는 품목과 품목의 개수
- n일 차에 회원가입을 하면 할인받아 살 수 있는 품목과 품목의 개수
두 항목은 딕셔너리이므로 == 연산자로 둘이 일치하는지 비교 후 True, False를 return

그것에 대해 가입일을 리턴하면 됨. 
'''