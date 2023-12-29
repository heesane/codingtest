import re
def solution(new_id):
    answer = ''
    check_answer = ''
    can_word = list("-_.~!@#$%^&*()=+[{]}:?,<>/")
    
    # step 1
    new_id = new_id.lower()
    print("step 1 : ",new_id)
    
    # step 2
    filter_list = list("~!@#$%^&*()=+[{]}:?,<>/")
    new_id = [w for w in list(new_id) if w not in filter_list]
    print("step 2 : ",new_id)
    # step 3
    stack = []
    for w in new_id:
        if stack:
            if stack[-1] == w and w == ".":
                continue
            else:
                stack.append(w)
        else:
            stack.append(w)    
    new_id = ("".join(stack))
    print("step 3 : ",new_id)
    
    # step 4 
    new_id = list(new_id)
    
    if new_id[0] == "." and new_id[-1] == ".":
        new_id = new_id[1:-1]
        
    elif new_id[-1] == ".":
        new_id = new_id[:-1]
            
    elif new_id[0] == ".":
        new_id = new_id[1:]
        
    print(new_id)
    new_id = "".join(new_id)
    print("step 4 : ",new_id)
    
    # step 5
    if new_id == "":
        new_id += "a"
    print("step 5 : ",new_id)
    # step 6
    if len(new_id) >= 16:
        new_id = list(new_id)
        for _ in range(len(new_id) - 15):
            new_id.pop()
        if new_id[-1] == ".":
            new_id.pop()
        new_id = "".join(new_id)
    print("step 6 : ",new_id)
    # step 7
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3-len(new_id))
        
    print("step 7 : ",new_id)
    
    return new_id