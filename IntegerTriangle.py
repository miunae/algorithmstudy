def solution(triangle):
    triangle.reverse()
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])-1):
            triangle[i+1][j] += max(triangle[i][j],triangle[i][j+1])
    return triangle[len(triangle)-1][0]