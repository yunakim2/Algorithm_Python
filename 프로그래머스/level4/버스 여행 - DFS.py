def solution(n,signs):
    def dfs(source, signs, visited_stations):
        if len(visited_stations) == len(signs):
            return
        for destination in range(len(signs)):
            if signs[source][destination] == 1 and destination not in visited_stations:
                visited_stations.add(destination)
                dfs(destination, signs, visited_stations)

    for source in range(n):
        visited_stations = set()
        dfs(source, signs, visited_stations)
        for destination in visited_stations:
            signs[source][destination] = 1
    return signs

if __name__ == "__main__":
    print(solution(3, [[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
    print(solution(3,[[0,0,1],[0,0,1],[0,1,0]]))
