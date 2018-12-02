import itertools

with open("input") as f:
    inputs = f.read().split()

    # part 1
    two_count = 0
    three_count = 0
    for word in inputs:
        count_dict = {}
        for char in word:
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
        for char, val in count_dict.items():
            if val == 2:
                two_count += 1
                break
        for char, val in count_dict.items():
            if val == 3:
                three_count += 1
                break
    print(two_count * three_count)

    # part 2
    for (first, second) in itertools.combinations(inputs, 2):
        diff_pos_set = set()
        for i in range(len(first)):
            if first[i] != second[i]:
                diff_pos_set.add(i)
                if len(diff_pos_set) > 1:
                    break
        if len(diff_pos_set) == 1:
            for val in diff_pos_set:
                print(first[:val] + first[val+1:])
