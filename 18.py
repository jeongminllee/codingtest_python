# def solution(arr, target) :
#     for i in range(len(arr)) :
#         for j in range(i + 1, len(arr)) :
#             if arr[i] + arr[j] == target :
#                 return True
#     return False
#
# arr = [1, 2, 3, 4, 8]
# target = 6
# print(solution(arr, target))
#
# arr = [2, 3, 5, 9]
# target = 10
# print(solution(arr, target))
# -- 개선이 필요한 답안

def count_sort(arr, k) :
    hashtable = [0] * (k + 1)

    for num in arr :
        # 현재 원소의 값이 k 이하인 때에만 처리
        if num <= k :
            # 현재 원소의 값을 인덱스로 해 해당 인덱스의 해시 테이블 값을 1로 설정
            hashtable[num] = 1
    return hashtable

def solution(arr, target) :
    hashtable = count_sort(arr, target)

    for num in arr :
        complement = target - num
        # target에서 현재 원소를 뺀 값이 해시 테이블에 있는지 확인
        if (
            complement != num
            and complement >= 0
            and complement <= target
            and hashtable[complement] == 1
        ) :
            return True
    return False

arr = [1, 2, 3, 4, 8]
target = 6
print(solution(arr, target))

arr = [2, 3, 5, 9]
target = 10
print(solution(arr, target))