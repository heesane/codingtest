from heapq import heappush,heappop
def solution(scoville, K):
    answer = 0
    heap = []
    for h in scoville:
        heappush(heap,h)
    
    while heap:
        first_score = heappop(heap)
        if len(heap) < 1 and first_score < K:
            return -1
        if first_score >= K:
            return answer
        else:
            answer += 1
            second_score = heappop(heap)
            heappush(heap,first_score + second_score * 2)