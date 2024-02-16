def solution1(board, moves):
    stack = []
    answer = 0

    for i in moves :
        for j in range(len(board)) :
            if board[j][i - 1] != 0 :
                stack.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(stack) > 1 :
                    if stack[-1] == stack[-2] :
                        stack.pop()
                        stack.pop()
                        answer += 2
                break

    return answer

def solution2(board, moves) :
    # 1. 각 열에 대한 스택을 생성
    lanes = [[] for _ in range(len(board[0]))]

    # 2. board를 역순으로 탐색하며, 각 열의 인형을 lanes에 추가합니다.
    for i in range(len(board) - 1, -1, -1) :
        for j in range(len(board[0])) :
            if board[i][j] :
                lanes[j].append(board[i][j])

    # 3. 인형을 담을 bucket을 생성
    bucket = []

    # 4. 사라진 인형의 총 개수를 저장할 변수를 초기화합니다.
    answer = 0


    # 5. moves를 순회하며, 각 열에서 인형을 뽑아 bucket에 추가합니다
    for m in moves :
        if lanes[m - 1] :   # 해당 열에 인형이 있는 경우
            doll = lanes[m - 1].pop()

            if bucket and bucket[-1] == doll : # 6. 바구니에 인형이 있고,
        # 가장 위에 있는 인형과 같은 경우
                bucket.pop()
                answer += 2
            else :  # 7. 바구니에 인형이 없거나, 가장 위에 있는 인형과 다른 경우
                bucket.append(doll)

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution1(board, moves))
print(solution2(board, moves))