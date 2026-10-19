# Sliding Window templates. Both are O(n): each element enters and leaves the window at most once.
#
# FIXED WINDOW (size k is given)
#   - Window is always [right - k + 1, right].
#   - Add arr[right]; once the window reaches size k, record the answer, then remove arr[right - k + 1].
#   - Examples: max sum of subarray of size k, averages of size k, anagrams of p in s.
#
# VARIABLE WINDOW (size depends on a condition)
#   - Expand by moving right every iteration.
#   - While the window is INVALID, shrink by moving left.
#   - Record the answer when the window is valid.
#       * Longest valid window  -> shrink while invalid, then update answer (after the while).
#       * Shortest valid window -> while valid: update answer, then shrink (inside the while).
#   - Requires the condition to be monotonic: shrinking a window can only make it "more valid"
#     (e.g. fewer repeats, smaller sum with non-negative numbers). Doesn't work with negative
#     numbers for sum conditions - use prefix sums + hashmap instead.
#   - Examples: longest substring without repeats, min size subarray sum >= target,
#     longest substring with at most k distinct characters.


# ---------- Fixed window template ----------
def fixed_window(arr, k):
    window_state = 0  # e.g. a running sum, a Counter, etc.
    result = None

    for right in range(len(arr)):
        # 1. Add the element entering the window
        window_state += arr[right]

        # 2. Window has reached size k
        if right >= k - 1:
            # 3. Record answer
            result = window_state if result is None else max(result, window_state)
            # 4. Remove the element leaving the window
            window_state -= arr[right - k + 1]

    return result


# ---------- Variable window template (longest valid window) ----------
def variable_window_longest(s):
    """Longest substring without repeating characters."""
    window = {}  # char -> count
    left = 0
    best = 0

    for right in range(len(s)):
        # 1. Expand: add s[right]
        window[s[right]] = window.get(s[right], 0) + 1

        # 2. Shrink while invalid
        while window[s[right]] > 1:
            window[s[left]] -= 1
            left += 1

        # 3. Window is valid -> update answer
        best = max(best, right - left + 1)

    return best


# ---------- Variable window template (shortest valid window) ----------
def variable_window_shortest(arr, target):
    """Length of the shortest subarray with sum >= target (non-negative numbers). 0 if none."""
    window_sum = 0
    left = 0
    best = float('inf')

    for right in range(len(arr)):
        # 1. Expand
        window_sum += arr[right]

        # 2. While valid: update answer, then shrink to try for something smaller
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return 0 if best == float('inf') else best


def main():
    print("Fixed - max sum of size 3:", fixed_window([2, 1, 5, 1, 3, 2], 3))                  # 9
    print("Variable longest - no repeats:", variable_window_longest("abcabcbb"))             # 3
    print("Variable shortest - sum >= 7:", variable_window_shortest([2, 3, 1, 2, 4, 3], 7))  # 2


if __name__ == '__main__':
    main()
