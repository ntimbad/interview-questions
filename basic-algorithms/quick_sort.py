# Quick Sort using the Lomuto partition scheme (pivot = arr[low]) from lomuto_partition.py.
# After partitioning, the pivot is in its final sorted position, so we recurse on each side of it.
#
# Time:  O(n log n) average, O(n^2) worst case (already sorted input with first-element pivot).
#        Picking a random pivot and swapping it to arr[low] first makes the worst case unlikely.
# Space: O(log n) average recursion depth, O(n) worst case. In-place, not stable.
import random

from lomuto_partition import lomuto_partition


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Randomized pivot to avoid O(n^2) on sorted input; lomuto_partition uses arr[low] as pivot.
        r = random.randint(low, high)
        arr[low], arr[r] = arr[r], arr[low]

        pivot_index = lomuto_partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

    return arr


def main():
    arr = [4, 8, 2, 1, 7, 5, 6, 3, 4]
    print("Sorted:", quick_sort(arr))
    print("Already sorted:", quick_sort(list(range(10))))
    print("Empty:", quick_sort([]))


if __name__ == '__main__':
    main()
