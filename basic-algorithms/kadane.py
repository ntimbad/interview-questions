# Kadane's Algorithm: maximum sum of a contiguous (non-empty) subarray. O(n) time.
#
# DYNAMIC PROGRAMMING VIEW
#   State:      dp[i] = max sum of a subarray that ENDS exactly at index i.
#   Recurrence: dp[i] = max(arr[i], dp[i-1] + arr[i])
#               Either start a fresh subarray at i, or extend the best one ending at i-1.
#   Answer:     max(dp[0..n-1])  (the best subarray has to end somewhere)
#   Optimal substructure: the best subarray ending at i is built from the best one ending at i-1.
#   Since dp[i] only depends on dp[i-1], the O(n) table collapses to a single variable -> O(1) space.
#
# GREEDY VIEW
#   Walk left to right keeping a running sum. At each element make the locally optimal choice:
#   if the running sum so far is negative, throw it away and start over at the current element.
#   Why that is safe: a negative prefix can only DECREASE the sum of any subarray that follows,
#   so no optimal subarray will ever start with it. Once dropped, we never reconsider it.
#   That is exactly the max(...) in the recurrence above: dp[i-1] < 0  <=>  arr[i] > dp[i-1] + arr[i].
#
# So Kadane's is DP with a space optimization, and the per-step decision happens to be a
# greedy "drop the negative prefix" rule that is provably never wrong.


def kadane_dp(arr):
    """Explicit DP table version - easier to reason about, O(n) space."""
    dp = [0] * len(arr)
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])
    return max(dp)


def kadane(arr):
    """Space-optimized / greedy version - O(1) space."""
    current = best = arr[0]
    for x in arr[1:]:
        # Greedy choice: a negative running sum can only hurt, so restart at x.
        current = max(x, current + x)
        best = max(best, current)
    return best


def kadane_with_indices(arr):
    """Also returns the (start, end) indices of the best subarray."""
    current = best = arr[0]
    start = best_start = best_end = 0
    for i in range(1, len(arr)):
        if current < 0:
            current = arr[i]
            start = i
        else:
            current += arr[i]
        if current > best:
            best = current
            best_start, best_end = start, i
    return best, best_start, best_end


def main():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("DP:", kadane_dp(arr))                    # 6
    print("Greedy:", kadane(arr))                   # 6
    print("With indices:", kadane_with_indices(arr))  # (6, 3, 6) -> [4, -1, 2, 1]
    print("All negative:", kadane([-3, -1, -2]))    # -1


if __name__ == '__main__':
    main()
