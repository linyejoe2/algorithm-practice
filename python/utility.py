import random


def create_random_word_sequence(amount=10, upper_case=True, lower_case=True):
    upper_case_words = ["A", "B", "C", "D", "E",
                        "F", "G", "H", "I", "J",
                        "K", "L", "M", "N", "O",
                        "P", "Q", "R", "S", "T",
                        "U", "V", "W", "X", "Y", "Z"]
    lower_case_words = ["a", "b", "c", "d", "e",
                        "f", "g", "h", "i", "j",
                        "k", "l", "m", "n", "o",
                        "p", "q", "r", "s", "t",
                        "u", "v", "w", "x", "y", "z"]

    words = []
    if upper_case:
        words.extend(upper_case_words)
    if lower_case:
        words.extend(lower_case_words)

    res = []
    for i in range(10):
        rnd = random.randint(0, len(words))
        res.append(words[rnd])

    return "".join(res)
