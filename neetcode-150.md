# NeetCode 150

The [NeetCode 150](https://neetcode.io/practice) problems with the main hint (crux) for each. Mark `☐` as `☑` when done.

## Arrays & Hashing

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Put items in a set; a repeat means duplicate. |
| ☐ | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Compare character counts (Counter or 26-array). |
| ☐ | [Two Sum](https://leetcode.com/problems/two-sum/) | Hash map of value -> index; look up `target - x` as you go. |
| ☐ | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Hash key = sorted word or 26-count tuple. |
| ☐ | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Count, then bucket sort by frequency (index = count) for O(n). |
| ☐ | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Length-prefix each string: `len#str`, so delimiters in the data don't matter. |
| ☐ | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Prefix product pass, then suffix product pass; no division. |
| ☐ | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Sets per row, column and 3x3 box (box = `(r//3, c//3)`). |
| ☐ | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Set; only start counting from numbers where `n-1` is absent. |

## Two Pointers

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Pointers from both ends, skipping non-alphanumerics. |
| ☐ | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Sorted: sum too big -> move right pointer left, too small -> move left right. |
| ☐ | [3Sum](https://leetcode.com/problems/3sum/) | Sort, fix one number, two-pointer the rest; skip duplicates. |
| ☐ | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Move the pointer at the shorter wall; width shrinks so only a taller wall can help. |
| ☐ | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Water at i = min(maxLeft, maxRight) - h[i]; two pointers track the smaller side's max. |

## Sliding Window

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Track min price so far; best = max(price - min). |
| ☐ | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Window + set/last-index map; shrink left on repeat. |
| ☐ | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Valid if `window - maxFreq <= k`; maxFreq never needs to decrease. |
| ☐ | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Fixed window of len(s1); compare char counts. |
| ☐ | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Expand until all needed chars are covered (`have == need`), then shrink to minimize. |
| ☐ | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Monotonic decreasing deque of indices; front is the max. |

## Stack

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Push openers; a closer must match the top. |
| ☐ | [Min Stack](https://leetcode.com/problems/min-stack/) | Store `(val, minSoFar)` on each push. |
| ☐ | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Push numbers; on operator pop two (order matters for `-` and `/`). |
| ☐ | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Backtrack: add `(` if open < n, add `)` if close < open. |
| ☐ | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Monotonic decreasing stack of indices; pop when a warmer day arrives. |
| ☐ | [Car Fleet](https://leetcode.com/problems/car-fleet/) | Sort by position descending; compute arrival times; a slower car ahead absorbs those behind. |
| ☐ | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Monotonic increasing stack; popped bar's width extends back to its start index. |

## Binary Search

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Binary Search](https://leetcode.com/problems/binary-search/) | Standard lo/hi/mid loop. |
| ☐ | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Treat as flat sorted array: `row = mid // cols`, `col = mid % cols`. |
| ☐ | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Binary search the answer (speed); check feasibility with ceil-sum of hours. |
| ☐ | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Compare mid to right: if `nums[mid] > nums[hi]` min is right, else left (incl. mid). |
| ☐ | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | One half is always sorted; check if target lies in it, else go other way. |
| ☐ | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Per-key list of (timestamp, value); binary search for the last timestamp <= query. |
| ☐ | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Binary search the partition of the smaller array so left halves <= right halves. |

## Linked List

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Keep `prev`, `cur`; flip `cur.next` while advancing. |
| ☐ | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Dummy head; append the smaller node each step. |
| ☐ | [Reorder List](https://leetcode.com/problems/reorder-list/) | Find middle (slow/fast), reverse second half, interleave. |
| ☐ | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Fast pointer n ahead, then move both; dummy head handles removing the first node. |
| ☐ | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Map old node -> new node; two passes (create, then wire next/random). |
| ☐ | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Digit-by-digit with carry; keep going while carry remains. |
| ☐ | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Floyd's: slow +1, fast +2; they meet iff cycle. |
| ☐ | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Treat values as next pointers -> Floyd's cycle; second phase finds the entrance. |
| ☐ | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Hash map + doubly linked list (or OrderedDict); move to front on access, evict tail. |
| ☐ | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Min-heap of heads, or divide-and-conquer pairwise merges. |
| ☐ | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Check k nodes exist, reverse that segment, reconnect with the previous group's tail. |

## Trees

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Swap children recursively. |
| ☐ | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | `1 + max(depth(left), depth(right))`. |
| ☐ | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | At each node, `leftH + rightH`; track global max while returning height. |
| ☐ | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Return height, with a sentinel (-1) if any subtree is unbalanced. |
| ☐ | [Same Tree](https://leetcode.com/problems/same-tree/) | Recurse on both trees in lockstep; both-null is true. |
| ☐ | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | At each node of root, run Same Tree against subRoot. |
| ☐ | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Walk down: both smaller -> left, both larger -> right, else current is LCA. |
| ☐ | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS; process `len(queue)` nodes per level. |
| ☐ | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | BFS, take the last node of each level. |
| ☐ | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | DFS carrying max-so-far; good if `val >= max`. |
| ☐ | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | DFS with (low, high) bounds, not just parent comparison. |
| ☐ | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Inorder traversal gives sorted order; stop at k. |
| ☐ | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Preorder[0] is root; its index in inorder splits left/right sizes. |
| ☐ | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Return best downward path (clamped at 0); update global with `left + right + val`. |
| ☐ | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Preorder with null markers; rebuild with an iterator. |

## Heap / Priority Queue

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Min-heap of size k; top is the kth largest. |
| ☐ | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Max-heap (negate values in Python); smash top two. |
| ☐ | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Heap on squared distance (no sqrt needed). |
| ☐ | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Size-k min-heap, or quickselect for O(n) average. |
| ☐ | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Max-heap + cooldown queue; or formula `(maxFreq-1)*(n+1) + countOfMax`. |
| ☐ | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Per-user tweet lists + follow sets; merge recent tweets with a heap. |
| ☐ | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Two heaps: max-heap for lower half, min-heap for upper; keep sizes balanced. |

## Backtracking

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Subsets](https://leetcode.com/problems/subsets/) | For each index: include or skip. |
| ☐ | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Reuse allowed: recurse on same index after picking; stop when sum exceeds target. |
| ☐ | [Permutations](https://leetcode.com/problems/permutations/) | Track used elements (or swap in place). |
| ☐ | [Subsets II](https://leetcode.com/problems/subsets-ii/) | Sort; skip a value equal to the previous at the same recursion level. |
| ☐ | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Sort; each number once; skip duplicates at the same level. |
| ☐ | [Word Search](https://leetcode.com/problems/word-search/) | DFS from each cell; mark visited, unmark on backtrack. |
| ☐ | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Try every prefix that's a palindrome, recurse on the rest. |
| ☐ | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Digit -> letters map; recurse by digit position. |
| ☐ | [N-Queens](https://leetcode.com/problems/n-queens/) | Place row by row; sets for columns, diag (`r-c`), anti-diag (`r+c`). |

## Tries

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Node = children dict + end flag. |
| ☐ | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | On `.`, recurse into every child. |
| ☐ | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Build a trie of words; one DFS over the grid, prune trie branches once found. |

## Graphs

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | DFS/BFS flood fill, count starts. |
| ☐ | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Flood fill returning area. |
| ☐ | [Clone Graph](https://leetcode.com/problems/clone-graph/) | DFS with map old -> clone to handle cycles. |
| ☐ | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) | Multi-source BFS from all gates. |
| ☐ | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Multi-source BFS by minute; check no fresh remain. |
| ☐ | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Reverse: BFS/DFS uphill from each ocean's border; intersect the sets. |
| ☐ | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Mark O's reachable from the border as safe; flip the rest. |
| ☐ | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Cycle detection in a directed graph (DFS states or Kahn's). |
| ☐ | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Topological order (Kahn's); empty if cycle. |
| ☐ | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Valid iff `edges == n-1` and connected (union-find or DFS). |
| ☐ | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Union-find, decrement count on each successful union. |
| ☐ | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Union-find; the edge whose endpoints already share a root. |
| ☐ | [Word Ladder](https://leetcode.com/problems/word-ladder/) | BFS; neighbors via wildcard patterns (`h*t`) buckets. |

## Advanced Graphs

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hierholzer's: DFS on sorted edges, post-order append, reverse. |
| ☐ | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | MST: Prim's with heap or Kruskal's with union-find. |
| ☐ | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Dijkstra; answer is max distance (or -1 if unreachable). |
| ☐ | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Dijkstra/min-heap where cost = max elevation on path. |
| ☐ | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Edges from first differing char of adjacent words; topo sort; watch prefix-invalid case. |
| ☐ | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Bellman-Ford limited to k+1 rounds (copy the distance array each round). |

## 1-D Dynamic Programming

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Fibonacci: `dp[i] = dp[i-1] + dp[i-2]`. |
| ☐ | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`. |
| ☐ | [House Robber](https://leetcode.com/problems/house-robber/) | `rob = max(prev2 + n, prev1)`. |
| ☐ | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Circle: run House Robber on `nums[1:]` and `nums[:-1]`. |
| ☐ | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Expand around each center (odd and even). |
| ☐ | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Same expand-around-center, count each success. |
| ☐ | [Decode Ways](https://leetcode.com/problems/decode-ways/) | `dp[i]` from 1-digit (non-zero) and 2-digit (10-26) endings. |
| ☐ | [Coin Change](https://leetcode.com/problems/coin-change/) | `dp[a] = 1 + min(dp[a - c])`; unreachable = inf. |
| ☐ | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Track both running max and min (negatives flip them). |
| ☐ | [Word Break](https://leetcode.com/problems/word-break/) | `dp[i]` true if some `dp[j]` true and `s[j:i]` in dict. |
| ☐ | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | O(n^2) dp, or patience sorting with bisect for O(n log n). |
| ☐ | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | 0/1 knapsack for target = sum/2 (odd sum -> false). |

## 2-D Dynamic Programming

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Unique Paths](https://leetcode.com/problems/unique-paths/) | `dp[r][c] = dp[r-1][c] + dp[r][c-1]` (or combinatorics). |
| ☐ | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Match -> `1 + dp[i-1][j-1]`, else max of up/left. |
| ☐ | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | State machine: held / sold / rest. |
| ☐ | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Count combinations: coins in the outer loop, amounts inner. |
| ☐ | [Target Sum](https://leetcode.com/problems/target-sum/) | DP over (index, running sum) with memo, or subset-sum reduction. |
| ☐ | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | `dp[i][j]`: s3[i+j] matches s1[i] or s2[j]. |
| ☐ | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | DFS + memo per cell (no visited needed since strictly increasing). |
| ☐ | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | On match: use it + skip it; on mismatch: skip. |
| ☐ | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Match -> diagonal; else 1 + min(insert, delete, replace). |
| ☐ | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Interval DP; pick the LAST balloon to burst in (l, r). |
| ☐ | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Handle `*` as zero-or-more of previous: skip pair, or consume a char if it matches. |

## Greedy

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Kadane: reset running sum when it goes negative. |
| ☐ | [Jump Game](https://leetcode.com/problems/jump-game/) | Track farthest reachable index; fail if i exceeds it. |
| ☐ | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | BFS-by-levels greedy: extend the window to the farthest reach. |
| ☐ | [Gas Station](https://leetcode.com/problems/gas-station/) | If total gas >= total cost a solution exists; restart start after any negative tank. |
| ☐ | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Counter + min-heap; always start a group at the smallest remaining card. |
| ☐ | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Ignore triplets exceeding target in any slot; check each target slot is hit. |
| ☐ | [Partition Labels](https://leetcode.com/problems/partition-labels/) | Last index per char; cut when i reaches the current window end. |
| ☐ | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Track range [lo, hi] of possible open counts; `*` widens it. |

## Intervals

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Add the ones before, merge the overlapping, add the ones after. |
| ☐ | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Sort by start; merge when `start <= lastEnd`. |
| ☐ | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Sort by start; on overlap, drop the one with the larger end. |
| ☐ | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Sort; any overlap with the previous -> false. |
| ☐ | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Sort starts and ends separately (two pointers) or min-heap of end times. |
| ☐ | [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Sort queries; sweep intervals into a min-heap keyed by size, pop expired ones. |

## Math & Geometry

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Transpose, then reverse each row. |
| ☐ | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Shrink top/bottom/left/right boundaries; guard against single row/col. |
| ☐ | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Use first row/col as markers (track their own zero-ness separately). |
| ☐ | [Happy Number](https://leetcode.com/problems/happy-number/) | Detect the cycle with a set or Floyd's. |
| ☐ | [Plus One](https://leetcode.com/problems/plus-one/) | Walk from the end; 9 -> 0 and carry, else increment and return. |
| ☐ | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Fast exponentiation (square, halve n); handle negative n. |
| ☐ | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | Grade-school: `res[i+j+1] += a*b`, then carry. |
| ☐ | [Detect Squares](https://leetcode.com/problems/detect-squares/) | Count points; for each diagonal point, multiply counts of the two other corners. |

## Bit Manipulation

| Done | Problem | Main Hint |
| :-: | --- | --- |
| ☐ | [Single Number](https://leetcode.com/problems/single-number/) | XOR all; pairs cancel. |
| ☐ | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | `n &= n - 1` clears the lowest set bit. |
| ☐ | [Counting Bits](https://leetcode.com/problems/counting-bits/) | `dp[i] = dp[i >> 1] + (i & 1)`. |
| ☐ | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Shift result left, OR in the lowest bit of n, shift n right; 32 times. |
| ☐ | [Missing Number](https://leetcode.com/problems/missing-number/) | XOR indices with values, or `n(n+1)/2 - sum`. |
| ☐ | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | XOR = sum without carry; `(a & b) << 1` = carry; mask to 32 bits in Python. |
| ☐ | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Pop digit/push digit; check 32-bit overflow before the push. |
