import random
import time


def create_random_integer_sequence(amount=10, f=0, to=100):
    res = []
    for i in range(amount):
        res.append(random.randint(f, to))
    return res


CRIS = create_random_integer_sequence


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
    for i in range(amount):
        rnd = random.randint(0, len(words) - 1)
        res.append(words[rnd])

    return "".join(res)


def test_crws():
    print(create_random_word_sequence())
    print(create_random_word_sequence(100, False))


def create_square_of_number_sequence(start=0, end=10):
    for i in range(start, end):
        yield i*i


def test_csons():
    csons = create_square_of_number_sequence()
    for i in csons:
        print(i)


def combinations(sequence: [], k: int) -> [[]]:
    length = len(sequence)
    if (length == 0 or length < k):
        return [[]]
    if (k == 1):
        comb = []
        for i in sequence:
            comb.append([i])
        return comb

    comb = []
    for i in range(length):
        comb_for_i = []
        seq = combinations(sequence[i + 1:], k-1)
        for j in seq:
            if len(j) != 0:
                comb_for_i.append([sequence[i]]+j)
        comb.extend(comb_for_i)
    return comb


def combinations_for_all_length(sequence: []) -> [[]]:
    comb = []
    for i in range(len(sequence) + 1):
        comb.extend(combinations(sequence, i))

    return comb


def test_cos():
    print(combinations_for_all_length(range(3)))


def print_matrix(mat: [[]]):
    for row in mat:
        print(row)


class Trace():
    """
    times: the times code excute.
    i.e., this func will calc the running time and divide by times
    """

    def __init__(self, times: int):
        self.start_time = time.time()
        self.times = times

    def stop(self, prefix="", suffix=""):
        if self.times:
            print(prefix, "use",
                  ((time.time() - self.start_time) / self.times),
                  "seconds in", self.times, "times", suffix)
        else:
            print(prefix, "use",
                  (time.time() - self.start_time), "seconds", suffix)
