def parse_claim(claim):
    coords = claim.split()[2].split(',')
    x = int(coords[0])
    y = int(coords[1][:coords[1].find(':')])

    area = claim.split()[3].split('x')
    width = int(area[0])
    height = int(area[1])

    return x, y, width, height


with open("input") as f:
    claims = f.read().splitlines()

    # part 1
    fabric = []
    for i in range(1000):
        row = [0] * 1000
        fabric.append(row)

    for claim in claims:
        x, y, width, height = parse_claim(claim)
        for i in range(x, x + width):
            for j in range(y, y + height):
                fabric[i][j] += 1

    overlap = 0
    for i in range(1000):
        for j in range(1000):
            if fabric[i][j] >= 2:
                overlap += 1

    print(overlap)

    # part 2
    for first_claim in claims:
        overlap = False
        first_x, first_y, first_width, first_height = parse_claim(first_claim)
        for second_claim in claims:
            if first_claim == second_claim:
                continue

            second_x, second_y, second_width, second_height = parse_claim(second_claim)

            first_extent_x = first_x + first_width
            first_extent_y = first_y + first_height
            second_extent_x = second_x + second_width
            second_extent_y = second_y + second_height

            if second_x > first_extent_x:
                continue
            if second_y > first_extent_y:
                continue
            if first_x > second_extent_x:
                continue
            if first_y > second_extent_y:
                continue

            overlap = True
            break

        if not overlap:
            print(first_claim)
