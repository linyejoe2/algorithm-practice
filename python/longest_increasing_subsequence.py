import utility


def length_of_longest_increasing_subsequence(sequence: []) -> int:
    dp = [0] * len(sequence)
    for i in range(1, len(sequence)):
        for j in range(len(i)):
            if (sequence[j] < sequence[i]):
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[len(sequence)] + 1


def longest_increasing_subsequence_Binary_search(sequence: []) -> []:
    seq = []
    return


def longest_increasing_subsequence_DP(sequence: []) -> []:
    step = [0 for _ in range(len(sequence))]
    for i in range(1, len(sequence)):
        step[i] = max([(step[k] + 1)
                       for k in range(len(sequence[:i]))
                       if sequence[k] < sequence[i]], default=0)

    max_setp = max(step)
    max_index = step.index(max_setp)
    max_value = sequence[max_index]
    res = [sequence[max_index]]

    next_one = max_value
    for i in reversed(range(max_index)):
        if sequence[i] < next_one:
            res.append(sequence[i])
            next_one = sequence[i]

    return res


def test_LIS():
    times = 50
    testCase = []
    rndSize = utility.CRIS(times, 1, 20)
    for i in range(times):
        testCase.append(utility.CRIS(rndSize[i]))

    t = utility.Trace(times)
    for i in range(times):
        print("------ test case %s ------" % i)
        print(testCase[i])
        print(longest_increasing_subsequence_DP(testCase[i]), "\n")
    t.stop()
