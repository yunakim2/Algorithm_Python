def solution(sentence):
    words = sentence.split(" ")
    my_counter = dict()

    for word in words:
        my_counter[word] = my_counter.get(word,0) + 1

    counted = sorted(my_counter.items(), key=lambda x: -x[1])
    return counted[0][0]


if __name__ == '__main__':
    print(solution("demi is very very lazy"))
