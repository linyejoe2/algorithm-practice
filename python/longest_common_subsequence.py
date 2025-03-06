import utility


def longest_common_subsequence_naive(s1: str, s2: str):
    s1_subsequence = utility.combinations_for_all_level(s1)
    s2_subsequence = utility.combinations_for_all_level(s2)

    res = []
    for sub1 in s1_subsequence:
        for sub2 in s2_subsequence:
            if (sub1 == sub2):
                if (len(sub1) > len(res)):
                    res = sub1
    return res


def longest_common_subsequence_DP(s1, s2):
    matrix = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

    for row in range(1, len(s2) + 1):
        for col in range(1, len(s1) + 1):
            if (s2[row - 1] == s1[col-1]):
                matrix[row][col] = matrix[row-1][col-1] + 1
            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row][col-1])

    print("DP matrix:")
    utility.print_matrix(matrix)
    res = []
    (row, col) = (len(s2), len(s1))
    while (row > 0 and col > 0):
        if (s2[row - 1] == s1[col - 1]):
            res.append(s2[row-1])
            row = row-1
            col = col-1
            continue
        elif (matrix[row-1][col] >= matrix[row][col-1]):
            row = row-1
            continue
        else:
            col = col-1
            continue
    res.reverse()
    return res


def test_LCS():
    print("\n------- %s -------" % "Test case")
    crws1 = utility.create_random_word_sequence(12, False)
    crws2 = utility.create_random_word_sequence(12, False)
    print("crws1:", crws1)
    print("crws2:", crws2)

    print("\n------- %s -------" % "Naive algo")
    t = utility.Trace()
    print("ans:", longest_common_subsequence_naive(crws1, crws2))
    t.stop()

    print("\n------- %s -------" % "DP algo")
    t = utility.Trace()
    print("ans:", longest_common_subsequence_DP(crws1, crws2))
    t.stop()

    # print("------- %s -------" % "edge case testing")
    # print(longest_common_subsequence_DP("zu", "zycfu"))
    # print(longest_common_subsequence_DP("csgew", "ce"))
    # print(longest_common_subsequence_DP("", ""))
