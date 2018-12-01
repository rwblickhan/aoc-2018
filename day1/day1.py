with open("input") as f:
    freqs = f.read().split()

    # part 1
    count = 0
    for freq in freqs:
        count += int(freq)
    print("Part 1: " + str(count))

    # part 2
    curr_count = 0
    found = False
    seen_freqs = set()
    while not found:
        for freq in freqs:
            curr_count += int(freq)
            if curr_count in seen_freqs:
                print("Part 2: " + str(curr_count))
                exit(0)
            seen_freqs.add(curr_count)
