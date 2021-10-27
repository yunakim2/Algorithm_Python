import math

def check_date(in_time, out_time):
    in_hour, in_min = in_time.split(':')
    out_hour, out_min = out_time.split(':')
    if out_hour > in_hour:
        return True
    else:
        if out_min >= in_min:
            return True
    return False

def sum_time(in_time, out_time):
    in_hour, in_min = map(int,in_time.split(':'))
    out_hour, out_min = map(int, out_time.split(':'))
    if in_min > out_min:
        out_hour -= 1
        out_min += 60

    total = (out_hour - in_hour) * 60 + (out_min - in_min)
    return total

def solution(fees, records):
    answer = []
    in_car = dict()
    out_car = dict()

    for record in records:
        time, car_num, checking = record.split()
        if checking == 'IN':
            if car_num in in_car:
                in_car[car_num].append(time)
            else:
                in_car[car_num] = [time]
        else:
            if car_num in out_car:
                out_car[car_num].append(time)
            else:
                out_car[car_num] = [time]

    in_car = sorted(in_car.items(), key=lambda x: x[0])
    for item, in_list in in_car:
        total = 0
        for idx, in_time in enumerate(in_list):
            out_time = '23:59'
            if item in out_car.keys():
                if idx < len(out_car[item]):
                    if check_date(in_time, out_car[item][idx]):
                        out_time = out_car[item][idx]
            total += sum_time(in_time, out_time)

        if total <= fees[0]:
            answer.append(fees[1])
        else:
            total -= fees[0]
            total = math.ceil(total/fees[2])
            answer.append(fees[1]+ (total*fees[3]))

    return answer


if __name__ == "__main__":
    print(solution([180, 5000, 10, 600],
                   ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                    "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
