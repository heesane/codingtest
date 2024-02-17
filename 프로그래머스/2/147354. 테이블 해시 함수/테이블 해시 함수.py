def solution(data, col, row_begin, row_end):
    hash_value = 0
    data.sort(key=lambda x : (x[col-1],-x[0]))
    rows = zip(range(row_begin, row_end+1), data[row_begin - 1: row_end])
    
    for idx,row in rows:
        _sum = 0
        for r in row:
            _sum += r % idx
        hash_value ^= _sum
    return hash_value
