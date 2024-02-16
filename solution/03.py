def solution(nums) :
    ret = []
    for i in range(len(nums)) :
        for j in range(i + 1, len(nums)) :
            ret.append(nums[i] + nums[j])
            print(ret)
    ret = sorted(set(ret))
    return ret

nums = [2, 1, 3, 4, 1]
print(solution(nums))