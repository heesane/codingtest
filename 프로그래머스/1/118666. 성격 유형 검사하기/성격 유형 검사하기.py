def solution(survey, choices):
    answer = 0
    survey_dict = {
        'R': 0,
        'T': 0,
        'F': 0,
        'C': 0,
        'M': 0,
        'J': 0,
        'A': 0,
        'N': 0
    }
    for i in range(len(survey)):
        front = survey[i][0]
        back = survey[i][1]
        
        choice = choices[i]
        
        if choice - 4 > 0:
            survey_dict[back] += abs(choice - 4)
        elif choice - 4 < 0:
            survey_dict[front] += abs(choice - 4)
    answer = ""
    
    answer += "R" if survey_dict["R"] >= survey_dict["T"] else "T"
    answer += "C" if survey_dict["C"] >= survey_dict["F"] else "F"
    answer += "J" if survey_dict["J"] >= survey_dict["M"] else "M"
    answer += "A" if survey_dict["A"] >= survey_dict["N"] else "N"
    
    return answer