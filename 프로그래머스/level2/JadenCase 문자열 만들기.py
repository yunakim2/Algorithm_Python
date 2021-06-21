import re
def solution(s):
    s = s.replace(' ', '-')
    s = list(s.split('-'))
    for idx, item in enumerate(s):
        upper_str = ''
        if item == '':
            continue
        if item[0].isnumeric():
            upper_str = item[0]+ item[1:].lower()
            s[idx] = upper_str
            continue

        upper_str = item[0].upper() + item[1:].lower()
        s[idx] = upper_str

    return ' '.join(s)


if __name__ == "__main__":
    print(solution("tomato"))
    print(solution(' adgagd 3eagdag '))




