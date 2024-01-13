from typing import List

def largest_rectangle(matrix: List[List[int]]) -> tuple:
    if not matrix or not matrix[0]:
        return 0, 0

    rows, cols = len(matrix), len(matrix[0])
    max_area = 0
    result_number = None

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != -9:  # Ignore visited cells
                number = matrix[row][col]
                area = 0

                # Calculate the area of the rectangle with the current number
                stack = [(row, col)]
                while stack:
                    r, c = stack.pop()
                    if 0 <= r < rows and 0 <= c < cols and matrix[r][c] == number:
                        area += matrix[r][c]
                        matrix[r][c] = -9  # Mark the cell as visited
                        stack.append((r + 1, c))  # Move down
                        stack.append((r, c + 1))  # Move right
                        stack.append((r - 1, c))  # Move up
                        stack.append((r, c - 1))  # Move left

                # Update the maximum area and result_number
                if area > max_area:
                    max_area = area
                    result_number = number

    return result_number, max_area
