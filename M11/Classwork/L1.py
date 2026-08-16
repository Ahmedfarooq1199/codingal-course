def subset_from_mask(items, mask):
    subset = []

    for i in range(len(items)):
        if mask & (1 << i):
            subset.append(items[i])

    return subset


def power_set(items):
    result = []
    total_subsets = 1 << len(items)

    for mask in range(total_subsets):
        result.append(subset_from_mask(items, mask))

    return result


def bit_probe(number, position):
    return (number >> position) & 1


def enumerate_subsets(items):
    total_subsets = 1 << len(items)

    for mask in range(total_subsets):
        subset = []

        for i in range(len(items)):
            if (mask >> i) & 1:
                subset.append(items[i])

        print(f"Mask {mask:0{len(items)}b}: {subset}")


def bit_difference(number1, number2):
    return number1 ^ number2


def main():
    items = ["A", "B", "C"]

    print("All Subsets:")
    enumerate_subsets(items)

    print("\nPower Set:")
    subsets = power_set(items)

    for i, subset in enumerate(subsets, start=1):
        print(f"{i}. {subset}")

    print("\nBit Probe:")
    number = 5

    for position in range(3):
        print(f"Bit {position}: {bit_probe(number, position)}")

    print("\nBit Difference:")
    number1 = 5
    number2 = 3

    difference = bit_difference(number1, number2)

    print(f"{number1} XOR {number2} = {difference}")


if __name__ == "__main__":
    main()