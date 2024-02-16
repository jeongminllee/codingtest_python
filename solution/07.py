# 제한사항 -5 ~ 5 의 x, y 좌표상에서만 움직임
# 움직이는 거 만들고 제한사항 만들고 v 배열을 만들어서 0에서 1로 바꾼 다음에 다 더하면 되지 않을까?
'''
def matrix(nx, ny) :
    return 0 <= nx < 11 and 0 <= ny < 11

def location(x, y, dir_) :
    if dir_ == "U" :
        nx, ny = x, y + 1
    elif dir_ == "D" :
        nx, ny = x, y - 1
    elif dir_ == "L" :
        nx, ny = x - 1, y
    elif dir_ == "R" :
        nx, ny = x + 1, y
    return nx, ny

def solution(dirs):
    x, y = 5, 5
    ans = set()
    for dir_ in dirs :
        nx, ny = location(x, y, dir_)
        if not matrix(nx, ny) :
            continue

        ans.add((x, y, nx, ny))
        ans.add((nx, ny, x, y))
        # 중복처리 -> 원위치 하게 되면

        x, y = nx, ny
    return len(ans) // 2
'''

def solution(dirs) :
    s = set()   # 겹치는 좌표는 1개로 처리하기 위함

    # 명령어를 통해 다음 좌표 결정 - 키-값으로 해결
    d = {'U' : (0,1), 'D' : (0,-1), 'R' : (1,0), 'L' : (-1,0)}

    x, y = 0, 0
    for i in dirs : # 주어진 명령어로 움직이면서 좌표 저장
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5 :    # 좌표 설정
            # A에서 B로 간 경우 B에서 A도 추가해야함.
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny   # 좌표 업데이트
    return len(s) // 2

print(solution("ULURRDLLU"))