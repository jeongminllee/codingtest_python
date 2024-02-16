from collections import deque

def solution(n, k) :
    q = deque(range(1, n + 1))
    while len(q) > 1 :
        for _ in range(k - 1) :
            q.append(q.popleft())

        q.popleft()
    return q[0]

# def solution(n, k) :
#     q = [i for i in range(1, n + 1)]
#     while len(q) > 1 :
#         for _ in range(k - 1) :
#             q.append(q.pop(0))

#         q.pop(0)

#     return q[0]

n = 5
k = 2
print(solution(n, k))

