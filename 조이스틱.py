def solution(name):
    if set(name) == {'A'}:
        return 0
    answer = 0
    dic = {}
    for i in range(26):
        dic[chr(i+65)] = min(i,abs(i-26))
    print(dic)
    # 기본 최소 이동 횟수
    min_move = len(name) - 1
    for i in range(len(name)):
        # 해당 알파벳 변동 값 추가
        answer += dic[name[i]]

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽에서 시작 방식, 오른쪽에서 시작 방식 값 비교 및 갱신
        min_move = min([min_move,2*i+len(name)-next,i+2*(len(name)-next)])

        # 알파벳 좌우 이동 값 추가
    answer += min_move

    return answer

print(solution("JEROEN"))