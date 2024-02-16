def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0
    
    # progresses 가 0이 되면 종료
    while len(progresses) > 0 :
        # progress 중인 업무를 기준으로 속도만큼 더해서 100이 되면 추출
        if progresses[0] + (speeds[0] * days) >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else :
            if count > 0 :
                answer.append(count)
                count = 0
            days += 1
    answer.append(count)
    return answer

progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]	
print(solution(progresses, speeds))