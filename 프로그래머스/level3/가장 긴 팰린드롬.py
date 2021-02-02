def solution(s):
    def is_palindrome(word):
        if len(word) <= 1:
            return True
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False

    for idx in range(len(s), 0, -1):
        for start in range(0, len(s)):
            word = s[start:start + idx]
            if is_palindrome(word):
                return len(word)
            if start + idx >= len(s):
                break
    return 0


if __name__ == "__main__":
    print(solution("abcdcba"))
    print(solution("abacde"))
