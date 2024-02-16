def solution(N, stages) :
    # 1. 스테이지별 도전자 수 구함
    challenger = [0] * (N + 2)
    for stage in stages :
        challenger[stage] += 1

    # 2. 스테이지별 실패한 사용자 수 계산
    fails = {}
    total = len(stages)

    # 3. 각 스테이지별 순회하며, 실패율 계산
    for i in range(1, N + 1) :
        if challenger[i] == 0 :
            fails[i] = 0
        else :
            fails[i] = challenger[i] / total
            total -= challenger[i]

    result = sorted(fails, key = lambda x : fails[x], reverse=True)
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))