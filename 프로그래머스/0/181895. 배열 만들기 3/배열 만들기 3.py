def solution(arr, intervals):
    answer = []
    print(arr[1:3+1]+arr[0:4+1])
    return arr[intervals[0][0]:intervals[0][1]+1] + arr[intervals[1][0]:intervals[1][1]+1]