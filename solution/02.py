def solution(nums, k) :
    # nums : 정수 리스트
    # k : 회전 횟수

    n = len(nums)
    k = k % n
    print(k)

    # nums의 마지막 k 개 요소를 앞으로 이동하고, 나머지를 뒤로 이동
    rotated_nums = nums[-k:] + nums[:-k]
    print('nums[-k:]', nums[-k:])
    print('nums[:-k]', nums[:-k])
    return rotated_nums

nums = [1, 2, 3, 4, 5]
k = 2
print(solution(nums, k))
