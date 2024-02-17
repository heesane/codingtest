# 프로그래머스 레벨 2 주차 요금 계산

def solution(fees, records):
    answer = []
    car = {}
    for record in records:
        time, number, state = record.split()
        if number not in car:
            car[number] = [time]
        else:
            car[number].append(time)
    for key in car:
        if len(car[key]) % 2 != 0:
            car[key].append('23:59')
    car = sorted(car.items())
    for key, value in car:
        time = 0
        for i in range(0, len(value), 2):
            start = value[i].split(':')
            end = value[i+1].split(':')
            time += (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (time - fees[0] + fees[2] - 1) // fees[2] * fees[3])
    return answer