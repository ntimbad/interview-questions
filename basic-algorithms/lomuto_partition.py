def lomuto_partition(arr, low, high):
    pivot = arr[low]
    i = low

    for runner in range(low+1, high+1):
        if arr[runner] <= pivot:
            i += 1
            arr[i], arr[runner] = arr[runner], arr[i]

    arr[i], arr[low] = arr[low], arr[i]
    return i


def main():
    arr = [4, 8, 2, 1, 7, 5, 6, 3, 4]
    pivot_index = lomuto_partition(arr, 0, len(arr) - 1)

    print("Partitioned Array:", arr)
    print("Pivot Index:", pivot_index)


if __name__ == '__main__':
    main()
