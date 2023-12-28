def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        s,e = queries[i][0],queries[i][1]
        
        for j in range(s,len(arr)):
            if j <= e:
                arr[j] = arr[j]+1
    return arr