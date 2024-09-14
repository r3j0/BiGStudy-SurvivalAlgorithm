def solution(edges):
    # 1. inDegree, outDegree 카운트
    # 2. 정점 중 inDegree가 0이고 outDegree가 2 이상인 정점이 새로 만든 정점. 
    # 3. in/out 이 0/1 : 막대 그래프, in/out 이 2/2 : 8자 그래프
    # 4. 새로 만든 정점의 outDegree - (막대, 8자 그래프 개수) = 도넛 그래프 개수
    
    answer = [0, 0, 0, 0]
    MAX = 1000001
    on = [0 for _ in range(MAX)]
    inDegree = [0 for _ in range(MAX)]
    outDegree = [0 for _ in range(MAX)]
    
    for e in edges:
        outDegree[e[0]] += 1
        inDegree[e[1]] += 1
    
    for i in range(1, MAX):
        if inDegree[i] == 0 and outDegree[i] >= 2: 
            answer[0] = i
            break
    
    for e in edges:
        if e[0] == answer[0]:
            inDegree[e[1]] -= 1
            
            # 새로 만든 정점을 빼는 과정에서 홀로 남는 정점을 막대 그래프로 카운트
            if inDegree[e[1]] == 0 and outDegree[e[1]] == 0: answer[2] += 1
        
    for i in range(1, MAX):
        if inDegree[i] == 0 and outDegree[i] == 1: answer[2] += 1
        if inDegree[i] == 2 and outDegree[i] == 2: answer[3] += 1
    
    answer[1] += outDegree[answer[0]] - (answer[2] + answer[3])
        
    return answer
