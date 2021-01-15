import collections


def solution(sentence):
    my_list = sentence.split()
    my_counter = collections.Counter(my_list).most_common()

    return my_counter[0][0]


if __name__ == '__main__':
    print(solution("demi is very very lazy"))
