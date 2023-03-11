# python3
# Aleksejs Šepeļevs, 221RDB494


def build_heap(data):
    swaps = []
    tests = len(data)
    for i in range(tests//2, -1, -1):
        while(True):
            min_index = i
            first = 2*i+1
            if first < data and data[first] < data[min_index]:
                min_index = first
            second = 2*i+2
            if second < data and data[second] < data[min_index]:
                min_index = second
            if i != min_index:
                swaps.append(i, min_index)
                data[i], data[min_index] = data[min_index], data[i]
                i = min_index
                continue
            break
    return swaps


def main():

    ievade = input()
    if "I" in ievade:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in ievade:
        ievade2 = input()
        if "a" in ievade2:
            return()
        with open ("tests/" + ievade2) as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    else:
        return()

    assert len(data) == n

    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()
