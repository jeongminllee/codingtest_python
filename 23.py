# def solution(genres, plays):
#     answer = []
#     dic1 = {}
#     dic2 = {}

#     for i, (g, p) in enumerate(zip(genres, plays)) :
#         if g not in dic1 :
#             dic1[g] = [(i, p)]
#         else :
#             dic1[g].append((i, p))

#         if g not in dic2 :
#             dic2[g] = p
#         else :
#             dic2[g] += p

#     for (k, v) in sorted(dic2.items(), key = lambda x:x[1], reverse=True) :
#         for (i, p) in sorted(dic1[k], key = lambda x:x[1], reverse=True)[:2] :
#             answer.append(i)

#     return answer

def solution(genres, plays) :
    answer = []
    genres_dict = {}
    plays_dict = {}

    for i in range(len(genres)) :
        genre = genres[i]
        play = plays[i]

        if genre not in genres_dict :
            genres_dict[genre] = []
            plays_dict[genre] = 0

        genres_dict[genre].append((i, play))
        plays_dict[genre] += play

    sorted_genres = sorted(plays_dict.items(), key=lambda x:x[1], reverse=True)

    for genre, _ in sorted_genres :
        sorted_songs = sorted(genres_dict[genre], key=lambda x:(-x[1], x[0]))
        answer.extend([i for i, _ in sorted_songs[:2]])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
'''
문제를 간략하게 만들어 문제를 푸는 데 필요한 부분만 남김
- 총 재생 횟수를 기준으로 장르를 내림차순으로 정렬
- 각 장르별로 2곡씩 선정해서 플레이리스트 만들기

문제를 요약했으니 입출력을 분석
genres = 배열
인덱스는 노래의 고유 번호이고, 배열의 값들은 해당 노래의 장르
고유번호    0           1       2           3       4
곡의장르    "classic", "pop", "classic", "classic", "pop"

재생횟수    500         600     150         800     2500

plays는 genres의 각 곡을 재생한 횟수
plays는 genres와 밀접한 관련이 있어 보임

classic 장르의 고유번호 {0, 2, 3}, 각 곡의 재생 횟수는 500 + 150 + 800 = 1,450
pop은 3,100회 classic은 1,450회 재생되었으므로 pop이 우선순위가 더 높으므로 
pop 장르부터 재생 횟수가 많은 노래순으로 정렬하고 이 장르에서 노래를 2개 뽑는다. 
만약 재생 횟수가 같다면 고유 번호가 낮은 노래를 뽑는다
1. 총 재생 횟수를 기준으로 장르를 정렬. 가장 많이 재생된 pop 장르가 맨 앞
2. 각 장르에서 많이 재생된 곡 순서로 정렬하는 모습. 곡 정보는 {재생 횟수, 고유 번호}
예를 들어 {2500, 4}는 2,500번 재새오딘 고유 번호 4번 곡을 의미함.

! 재생 횟수가 같은 경우 고유 번호순으로 정렬하겠다고 했으나, 지금 입출력 예시에는 이런 부분이 없음.
! 입출력 예시만 보고서 구현하다 보면 이런 부분을 놓치기 쉬움.

정렬이 끝난 상태에서 우선순위가 높은 장르부터 2곡씩 뽑음. 반환값은 고유 번호이므로 [4, 1, 3, 0]
'''