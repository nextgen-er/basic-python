if __name__ == "__main__":
    # ------------------------------------------------------------------
    # First Non Repeating Character
    # ------------------------------------------------------------------
    def non_repeating_char(s):
        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        for char in s:
            if frequency[char] == 1:
                return char
        return None

    print(non_repeating_char("i am telling you the truth that i am"))

    # ------------------------------------------------------------------
    # Anagram without sorting
    # ------------------------------------------------------------------
    def is_anagram(s1, s2):
        if len(s1) != len(s2):
            return False

        frequency = {}

        for char in s1:
            frequency[char] = frequency.get(s1, 0) + 1

        for char in s2:
            if char not in frequency:
                return False

            frequency[char] -= 1

            if frequency[char] < 0:
                return False

        return all(value == 0 for value in frequency.values())

    print(is_anagram("silent", "listen"))
