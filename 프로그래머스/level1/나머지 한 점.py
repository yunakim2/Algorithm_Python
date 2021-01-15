def solution(v):
    x_list = dict()
    y_list = dict()
    for x,y in v:
        x_list [x] = x_list.get(x,0)+1
        y_list [y] = y_list.get(y,0)+1

    sort_x = sorted(x_list.items(), key=lambda x: x[1])
    sort_y = sorted(y_list.items(), key = lambda x: x[1])

    answer = [sort_x[0][0], sort_y[0][0]]
    return answer



if __name__ == '__main__':
    print(solution([[1,4],[3,4],[3,10]]))