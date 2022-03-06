def solution(triangle):
    depth = len(triangle)
    for d in range(1, depth):
        for j in range(d+1):
            if j == 0: triangle[d][j] += triangle[d-1][j]
            elif j == d: triangle[d][j] += triangle[d-1][j-1]
            else: triangle[d][j] += max(triangle[d-1][j], triangle[d-1][j-1])
    return max(triangle[depth-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))