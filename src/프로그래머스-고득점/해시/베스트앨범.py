def solution(genres, plays):
    answer = []

    import heapq
    l = len(genres)
    music = {}
    tmp = {}

    for i in range(l):
        genre = genres[i]
        play = plays[i]
        if not music.get(genre):
            music[genre] = 0
            tmp[genre] = []
        music[genre] += play
        heapq.heappush(tmp[genre], (-play, i))
    
    for genre in sorted(music.keys(), key = lambda x: -music[x]):
        answer.extend([num for _, num in heapq.nsmallest(2, tmp[genre])])
    
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])

# 다른 사람 풀이
# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort = sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer