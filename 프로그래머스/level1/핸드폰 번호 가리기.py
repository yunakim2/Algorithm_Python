def solution(phone_number):
    leng = len(phone_number)
    phone_number = phone_number[-4:]
    phone_number= phone_number.rjust(leng,'*')

    return phone_number

print(solution("01033334444"))