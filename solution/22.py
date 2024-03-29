def solution(record):
    answer = []
    uid = {}

    for line in record :    # record의 각 줄 하나씩 처리
        cmd = line.split(' ')
        if cmd[0] != 'Leave' :  # Enter 또는 Chage인 경우
            uid[cmd[1]] = cmd[2]

    for line in record :    # record의 각 줄 하나씩 처리
        cmd = line.split(' ')
        # 각 상태에 맞는 메시지를 answer에 저장
        if cmd[0] == "Enter" :
            # answer.append("%s님이 들어왔습니다." % uid[cmd[1]])
            answer.append(f"{uid[cmd[1]]}님이 들어왔습니다.")
        elif cmd[0] == "Change" :
            pass
        else :
            # answer.append("%s님이 나갔습니다." % uid[cmd[1]])
            answer.append(f"{uid[cmd[1]]}님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
'''
방 개설자 기준으로 최종으로 채팅방에서 보일 메시지를 반환하는 문제. 
우리가 해결해야할 내용은 중간에 유저 닉네임이 변경될 수 있는데, 
그러면 기존 대화 내용에 있는 닉네임도 새로 수정한 닉네임으로 바뀌어야 한다는 점.

닉네임이 변경되는 경우 살펴보기
- 기존 방에 있던 회원이 나갔다가 다시 들어옴
- 닉네임 변경

이 조건을 처리하려면 어떻게 해야 할까?
닉네임을 변경하려면 이전 닉네임으로 입력한 메시지를 모두 수정함. 
단, 이렇게 하면 시간 복잡도는 O(N^2)입니다. 
recode의 개수가 최대 10만 개이므로 더 효율적인 방법을 찾아야함.

더 효율적으로 해결하기
다음 3가지를 알 수 있음.
- 문제에서 요구하는 것은 최종으로 보는 메시지
- 유저 아이디는 유일
- 닉네임은 유저의 상태가 Enter와 Change인 때만 바뀔 수 있음. 

1. 최종으로 구하고자 하는건 뭐지? -> 최종으로 보는 메시지
2. 입력값 중 수정되지 않는 건 뭐지? -> 유저 아이디
3. 입력값 중 수정되는건 뭐지? -> 닉네임
    3-1. 입력값이 수정될 때 어디가 영향받지? -> 오픈 채팅방의 내용 변경
    3-2. 입력값은 어느 조건에서 수정되지? -> Enter와 Change인 경우

궁극적으로 코딩 테스트를 잘하려면 이렇게 필요한 질문을 하고 스스로 답하는 것이 중요함.
다른 문제를 분석할 때도 이런 과정은 매우 중요함. 코딩 테스트 성과가 좋은 분들은 대부분 이런 과정을 자연스럽게,
잘하는 경우가 많음. 그러고 나서 입력값을 활용해서 문제에 알맞은 자료구조를 골라야 함.
입력값 중에 고정된 값과 그렇지 않은 값이 있을 때는, 고정된 값을 딕셔너리의 키로 지정하면 예외 처리를 줄일 수 있음.
그리고 수정되는 값이 무엇인지 아록 있으면 데이터의 상관관계 및 흐름을 파악하고, 예외사항을 미리 검토할 수 있음.

문제에서 요구하는건 최종으로 보는 메시지.
메시지는 {유저 상태, 유저 아이디, 닉네임}과 같은 구성.
그리고 여기서 유일한 값은 유저 아이디임. 즉, 유저 아이디를 기준으로 각 메시지를 확인해서 유저 상태가
Change, Enter일 때 닉네임을 변경하면 됨. 분석이 끝나니 문제는 매우 단순해짐. 
각 메시지의 연관 관계를 생각하지 않고, 각 메시지의 상태만 확인. 이를 위해 유저 아이디를 키,
닉네임을 값으로 하는 딕셔너리를 생성
'''