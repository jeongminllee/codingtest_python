from collections import deque

def solution(cards1, cards2, goal):
    # cards와 goal을 deque로 변환
    card1 = deque(cards1)
    card2 = deque(cards2)
    goal = deque(goal)

    while goal :
        if card1 and card1[0] == goal[0] :
            card1.popleft()
            goal.popleft()
        elif card2 and card2[0] == goal[0] :
            card2.popleft()
            goal.popleft()
        else :
            return 'No'
    return 'Yes' 

cards1 = ["i", "drink", "water"]	
cards2 = ["want", "to"]	
goal = ["i", "want", "to", "drink", "water"]	
print(solution(cards1, cards2, goal))