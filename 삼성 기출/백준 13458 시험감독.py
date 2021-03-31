
def super_check():
    sum_super = 0
    for mem in student:
        sum_super += 1
        mem -= all_super
        if mem > 0 :
            if mem % sub_super == 0:
                sum_super += (mem//sub_super)
            else:
                sum_super += (mem // sub_super) +1

    return sum_super


if __name__ == '__main__':
    test_cnt = int(input())

    student = list(map(int, input().split()))
    all_super, sub_super = map(int, input().split())

    print(super_check())
