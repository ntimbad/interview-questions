Add # Spiral Matrix

## Problem Description

Given an `m x n` matrix, return all elements of the matrix in spiral order.

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Visualization:
1 → 2 → 3
        ↓
4 → 5   6
↑       ↓
7 ← 8 ← 9
```

**Example 2:**
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

---

## Solution: Rotation Approach

### Key Insight
Instead of tracking boundaries and directions, we can:
1. Take the entire top row
2. Rotate the remaining matrix 90° counter-clockwise
3. Repeat until the matrix is empty

### Why This Works
After taking the top row, rotating counter-clockwise transforms:
- The **right column** → becomes the new **top row**
- The **bottom row** → becomes the new **right column**
- The **left column** → becomes the new **bottom row**

This naturally follows the spiral pattern.

### Implementation

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            # Take the entire top row
            result += matrix.pop(0)
            # Rotate remaining matrix 90° counter-clockwise
            matrix = list(zip(*matrix))[::-1]
        return result
```

### How the Rotation Works

`zip(*matrix)` transposes the matrix (swap rows and columns):
```
[[1, 2],     →     [[1, 3],
 [3, 4]]            [2, 4]]
```

`[::-1]` reverses the rows (completes the counter-clockwise rotation):
```
[[1, 3],     →     [[2, 4],
 [2, 4]]            [1, 3]]
```

### Step-by-Step Example

```
Initial: [[1,2,3],[4,5,6],[7,8,9]]

Step 1: Take top row [1,2,3]
Remaining: [[4,5,6],[7,8,9]]

Step 2: Rotate → [[6,9],[5,8],[4,7]]
Take top row [6,9]
Remaining: [[5,8],[4,7]]

Step 3: Rotate → [[8,7],[5,4]]
Take top row [8,7]
Remaining: [[5,4]]

Step 4: Rotate → [[4],[5]]
Take top row [4]
Remaining: [[5]]

Step 5: Take top row [5]
Done!

Result: [1,2,3,6,9,8,7,4,5]
```

---

## Matrix Transformation Cheat Sheet

Understanding matrix transformations is crucial for solving many array problems. Here are the most common operations:

### 1. `list(zip(*matrix))` - Transpose

Swaps rows and columns (reflects across main diagonal).

```python
matrix = [[1, 2, 3],
          [4, 5, 6]]

result = list(zip(*matrix))
# [(1, 4), (2, 5), (3, 6)]

# Convert to lists:
result = [list(row) for row in zip(*matrix)]
# [[1, 4],
#  [2, 5],
#  [3, 6]]
```

**Visualization:**
```
1 2 3       1 4
4 5 6   →   2 5
            3 6
```

**How it works:**
- `*matrix` unpacks the rows: `zip([1,2,3], [4,5,6])`
- `zip` pairs up elements by position: `(1,4), (2,5), (3,6)`

---

### 2. `list(zip(*matrix[::-1]))` - Rotate 90° Clockwise

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = [list(row) for row in zip(*matrix[::-1])]
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
```

**Visualization:**
```
1 2 3       7 4 1
4 5 6   →   8 5 2
7 8 9       9 6 3
```

**Steps:**
1. `matrix[::-1]` reverses rows: `[[7,8,9], [4,5,6], [1,2,3]]`
2. `zip(*)` transposes: `[[7,4,1], [8,5,2], [9,6,3]]`

**Use case:** Rotating images, game boards

---

### 3. `list(zip(*matrix))[::-1]` - Rotate 90° Counter-Clockwise

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = [list(row) for row in zip(*matrix)][::-1]
# [[3, 6, 9],
#  [2, 5, 8],
#  [1, 4, 7]]
```

**Visualization:**
```
1 2 3       3 6 9
4 5 6   →   2 5 8
7 8 9       1 4 7
```

**Steps:**
1. `zip(*matrix)` transposes: `[[1,4,7], [2,5,8], [3,6,9]]`
2. `[::-1]` reverses rows: `[[3,6,9], [2,5,8], [1,4,7]]`

**Use case:** This is what we use in the spiral matrix solution!

---

### 4. `[row[::-1] for row in matrix[::-1]]` - Rotate 180°

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = [row[::-1] for row in matrix[::-1]]
# [[9, 8, 7],
#  [6, 5, 4],
#  [3, 2, 1]]
```

**Visualization:**
```
1 2 3       9 8 7
4 5 6   →   6 5 4
7 8 9       3 2 1
```

**Steps:**
1. `matrix[::-1]` reverses rows: `[[7,8,9], [4,5,6], [1,2,3]]`
2. `row[::-1]` reverses each row: `[[9,8,7], [6,5,4], [3,2,1]]`

**Alternative:** `matrix[::-1][::-1]` (but this is less clear)

---

### 5. `matrix[::-1]` - Flip Vertically

Reverses the order of rows (reflects across horizontal axis).

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = matrix[::-1]
# [[7, 8, 9],
#  [4, 5, 6],
#  [1, 2, 3]]
```

**Visualization:**
```
1 2 3       7 8 9
4 5 6   →   4 5 6
7 8 9       1 2 3
```

**Use case:** Image processing, reversing game states

---

### Summary Table

| Operation | Code | What it does |
|-----------|------|--------------|
| **Transpose** | `list(zip(*matrix))` | Swap rows ↔ columns |
| **Rotate 90° CW** | `list(zip(*matrix[::-1]))` | Clockwise turn |
| **Rotate 90° CCW** | `list(zip(*matrix))[::-1]` | Counter-clockwise turn |
| **Rotate 180°** | `[row[::-1] for row in matrix[::-1]]` | Upside down |
| **Flip Vertical** | `matrix[::-1]` | Reverse row order |
| **Flip Horizontal** | `[row[::-1] for row in matrix]` | Reverse each row |

### Memory Note

All these operations create **new lists**. To modify in-place, you'd need different approaches (usually swapping elements).

---

## Complexity Analysis

- **Time:** O(m × n) - we visit each element exactly once
- **Space:** O(m × n) - the rotation creates new lists

---

## Alternative: Boundary Tracking Approach

If you need O(1) space (excluding output), track four boundaries and adjust them:

```python
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Move right along top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Move down along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Move left along bottom row (if exists)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Move up along left column (if exists)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```

**Trade-offs:**
- Rotation approach: More elegant, easier to understand, but uses extra space
- Boundary approach: More verbose, but uses O(1) space
