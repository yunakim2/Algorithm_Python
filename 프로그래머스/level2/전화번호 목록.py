
def solution(phone_book):
    phone_book.sort()
    phone_book = dict([(index, list(phone)) for index, phone in enumerate(phone_book)])
    for i in range(len(phone_book)):
        size = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if len(phone_book[j]) >= size:
                if phone_book[j][0:size] == phone_book[i]:
                    return False
    else:
        return True


if __name__ == "__main__":
    print(solution(["0", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))
    print(solution(["123", "456", "4567", "999"]))
    print(solution(["113","44","4544"]))
