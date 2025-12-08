from aoc2025.utils.utils import read_input
tachyon_splitter = '^'


def solve_tachyon_manifold(manifold_diagram):
    """
    Simulates the tachyon beam paths and counts the total number of splits.

    Args:
        manifold_diagram: A list of strings representing the grid (puzzle input).

    Returns:
        The total number of times the beam is split.
    """
    if not manifold_diagram:
        return 0

    # 1. Initialization and Setup

    # R is the number of rows, C is the number of columns
    R = len(manifold_diagram)
    C = len(manifold_diagram[0])

    # Find the starting column (S is guaranteed to be in the first row, R=0)
    try:
        start_col = manifold_diagram[0].index('S')
    except ValueError:
        # Handle case where 'S' is not found (though unlikely for puzzle input)
        return 0

    # Use a set to track the columns of beams active in the *current* row.
    # This automatically handles merging beams.
    active_beam_cols = {start_col}
    total_splits = 0

    # 2. Simulation (Row-by-Row)

    # Start from the second row (index 1), as the beam enters from row 0
    # and immediately affects row 1, and proceed to the last row (R-1).
    for r in range(1, R):

        # This set holds the column indices for beams that will be active
        # in the *next* row (r + 1).
        next_beam_cols = set()

        # Check all beams that made it to the current row (r)
        for c in active_beam_cols:

            # The current cell content
            cell = manifold_diagram[r][c]

            if cell == '.':
                # Case 1: Empty space ('.'). Beam passes through.
                # It continues straight down to the next row at column c.
                next_beam_cols.add(c)

            elif cell == '^':
                # Case 2: Splitter ('^').

                # The beam is split! Increment the counter.
                total_splits += 1

                # Check for the left-emerging beam (c - 1)
                left_col = c - 1
                if left_col >= 0:
                    # If the column is within bounds, add it to the next row's beams
                    next_beam_cols.add(left_col)

                # Check for the right-emerging beam (c + 1)
                right_col = c + 1
                if right_col < C:
                    # If the column is within bounds, add it to the next row's beams
                    next_beam_cols.add(right_col)

            # Note: Any beams hitting the boundaries of the manifold
            # (either c-1 < 0 or c+1 >= C for a split) simply stop.
            # Any beams hitting the bottom (r == R-1) also stop naturally.

        # Update the active beams for the next iteration (row r+1)
        active_beam_cols = next_beam_cols

    return total_splits


def solve_quantum_manifold(manifold_diagram):
    """
    Calculates the total number of unique timelines by tracking all possible paths.

    Args:
        manifold_diagram: A list of strings representing the grid (puzzle input).

    Returns:
        The total number of different timelines after the particle completes its journey.
    """
    if not manifold_diagram:
        return 0

    R = len(manifold_diagram)
    C = len(manifold_diagram[0])

    # 1. Find Start Column and Initialize DP Table
    try:
        start_col = manifold_diagram[0].index('S')
    except ValueError:
        return 0

    # Initialize Timelines grid: Timelines[r][c] stores the count of timelines
    # that reach column 'c' in row 'r'.
    # We only need to track the current row (r) and the next row (r+1)
    # for memory efficiency, but a full grid is often easier to debug.
    timelines = [[0] * C for _ in range(R)]

    # Base Case: The single particle timeline starts from S and reaches
    # the first processing row (r=1) at the start column.
    if R > 1:
        timelines[1][start_col] = 1
    elif R == 1:
        # If the manifold is only one row, the particle is already at the end.
        return 1

        # 2. Iteration and Propagation (Dynamic Programming)
    # Start from row 1 and proceed up to the second-to-last row (R-2),
    # as propagation from R-2 affects the final row R-1.
    for r in range(1, R - 1):
        for c in range(C):

            # Only process if timelines actually reach this cell
            if timelines[r][c] == 0:
                continue

            num_timelines_here = timelines[r][c]
            cell = manifold_diagram[r][c]

            if cell == '.':
                # Empty space: Timelines propagate straight down
                timelines[r + 1][c] += num_timelines_here

            elif cell == '^':
                # Splitter: Timelines split to left and right

                # Propagate to Left (c - 1)
                left_col = c - 1
                if left_col >= 0:
                    timelines[r + 1][left_col] += num_timelines_here

                # Propagate to Right (c + 1)
                right_col = c + 1
                if right_col < C:
                    timelines[r + 1][right_col] += num_timelines_here

    # 3. Final Answer
    # The total number of timelines is the sum of all timeline counts
    # in the last row (R-1).
    total_timelines = sum(timelines[R - 1])

    return total_timelines
def star1() -> int:
    data = read_input()
    result = solve_tachyon_manifold(data)
    return result


def star2() -> int:
    data = read_input()
    result = solve_quantum_manifold(data)
    return result


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
