def solution(participant, completion):
    participant.sort()
    completion.sort()
    idx = 0
    for member in completion:
        if member == participant[idx]:
            idx += 1
    return participant[idx]

if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))