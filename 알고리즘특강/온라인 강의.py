
total_h, total_m = map(int, input().split(":"))
s_h,s_m  = map(int, input().split(":"))

if total_m < 50:
    check_m = total_m + 10
    check_h = total_h
else :
    check_h = total_h + 1
    check_m = total_m - 50

if s_h == 0:
    s_h = 24

print(s_h,s_m)

if s_h == total_h and s_m == total_m:
    print(1)
else:
    if s_h >= total_h and s_m >= total_m and s_h <= check_h and s_m <= check_m:
        print(1)
    else:
        if total_h <= s_h <= check_h:
            if s_h>= total_h and s_m >= total_m and s_m <= check_m+60:
                print(1)
            else:
                print(0)
        else:
            print(0)