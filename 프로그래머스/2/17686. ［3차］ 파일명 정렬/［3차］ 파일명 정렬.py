def solution(files):
    answer = []
    
    
    for file in files:
        head,number,tail = '','',''
        number_check = False
        
        for f in range(len(file)):
            if file[f].isdigit():
                number += file[f]
                number_check = True
            elif not number_check:
                head += file[f]
            else:
                tail += file[f:]
                break
        answer.append((head, number, tail))
    answer.sort(key=lambda x : (x[0].lower(),int(x[1])))
    
    return [''.join(x) for x in answer]