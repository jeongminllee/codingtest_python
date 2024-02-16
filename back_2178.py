import sys
sys.stdin = open("./data/input_2178.txt", "r")

# 상하좌우 움직이는 알고리즘을 작성한다
# 이때 좌표가 (1, x)는 위로 더 이상 가지 못하는 코드를 작성해줘야 한다
# (y, 1), (4, x), (y, 6)역시 각 위치마다 상하좌우로 더 이상 움직이지 못한다
# 1은 움직일수 있는 위치이고 0 은 움직이지 못하는 위치이다.
# 1, 1 에서 N, M 까지 움직이는 최소한의 거리를 구하여라.
# 움직인 횟수 + 1를 더해야함. 시작 위치와 도착 위치도 포함.

def bfs(si, sj, ei, ej) :
    q = []
    v = [[0] * M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1

    while q :
        ci, cj = q.pop(0)
        # 정답 처리가 필요한 경우 이자리에서...
        if (ci, cj) == (ei, ej) :
            return v[ei][ej]

        # 4 방향, 범위내, 조건에 맞으면 : arr == 1, v == 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) :  # 상 하 좌 우
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0 :
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

ans = bfs(0, 0, N - 1, M - 1)

print(ans)
