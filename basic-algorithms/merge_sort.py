# Merge Sort: divide the array in half, sort each half recursively, then merge the two sorted halves.
#
# Time:  O(n log n) in all cases (log n levels of splitting, O(n) merge work per level).
# Space: O(n) for the merged output. Stable (use <= so equal elements keep their original order).


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # One side is exhausted; the remainder of the other is already sorted.
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def main():
    arr = [4, 8, 2, 1, 7, 5, 6, 3, 4]
    print("Sorted:", merge_sort(arr))
    print("Empty:", merge_sort([]))


if __name__ == '__main__':
    main()
