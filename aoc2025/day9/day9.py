from aoc2025.utils.utils import read_input
from itertools import combinations
from collections import deque

def build_compressed_grid_from_loop(points_xy):
    """
    Given loop vertices as (x, y) in order, build a compressed grid with:
    - '#' = red tiles (the vertices)
    - 'X' = green tiles (boundary segments + interior via flood fill)

    Returns:
      grid: list[str]
      red_tiles_rc: list[(r, c)] positions of red tiles in grid coordinates
      xs: list of original x-coordinates in order of columns
      ys: list of original y-coordinates in order of rows
    """

    # 1. Collect unique coordinates for compression
    xs = sorted({x for x, y in points_xy})
    ys = sorted({y for x, y in points_xy})

    x_to_c = {x: i for i, x in enumerate(xs)}
    y_to_r = {y: i for i, y in enumerate(ys)}

    H = len(ys)
    W = len(xs)

    # 2. Initialize grid
    grid = [['.' for _ in range(W)] for _ in range(H)]

    # 3. Place red tiles
    red_tiles_rc = []
    for x, y in points_xy:
        r = y_to_r[y]
        c = x_to_c[x]
        grid[r][c] = '#'
        red_tiles_rc.append((r, c))

    # 4. Connect consecutive reds with green lines (boundary)
    n = len(points_xy)
    for i in range(n):
        x1, y1 = points_xy[i]
        x2, y2 = points_xy[(i + 1) % n]  # wrap

        r1, c1 = y_to_r[y1], x_to_c[x1]
        r2, c2 = y_to_r[y2], x_to_c[x2]

        if r1 == r2:
            # horizontal segment
            step = 1 if c2 > c1 else -1
            for cc in range(c1 + step, c2, step):
                if grid[r1][cc] == '.':
                    grid[r1][cc] = 'X'
        elif c1 == c2:
            # vertical segment
            step = 1 if r2 > r1 else -1
            for rr in range(r1 + step, r2, step):
                if grid[rr][c1] == '.':
                    grid[rr][c1] = 'X'
        else:
            raise ValueError("Non-axis-aligned segment between points: "
                             f"{(x1, y1)} -> {(x2, y2)}")

    # 5. Flood fill from the border to find outside region
    H, W = len(grid), len(grid[0])
    outside = [[False] * W for _ in range(H)]
    q = deque()

    def try_start(r, c):
        if 0 <= r < H and 0 <= c < W:
            if grid[r][c] == '.' and not outside[r][c]:
                outside[r][c] = True
                q.append((r, c))

    # start flood from all border '.' cells
    for r in range(H):
        try_start(r, 0)
        try_start(r, W - 1)
    for c in range(W):
        try_start(0, c)
        try_start(H - 1, c)

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W:
                if grid[nr][nc] == '.' and not outside[nr][nc]:
                    outside[nr][nc] = True
                    q.append((nr, nc))

    # 6. Any '.' not marked outside is interior -> green 'X'
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '.' and not outside[r][c]:
                grid[r][c] = 'X'

    grid_strs = [''.join(row) for row in grid]
    return grid_strs, red_tiles_rc, xs, ys

def largest_rectangle_red_green(grid, red_tiles_rc, xs, ys):
    """
    Find largest rectangle whose opposite corners are red (#)
    and which consists only of red/green cells (# or X).

    Area is computed in terms of ORIGINAL coordinates (xs, ys).
    """
    rows = len(grid)
    cols = len(grid[0])

    # valid[r][c] = 1 if cell is red or green
    valid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ('#', 'X'):
                valid[r][c] = 1

    # 2D prefix sum over valid
    ps = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        row_sum = 0
        for c in range(cols):
            row_sum += valid[r][c]
            ps[r + 1][c + 1] = ps[r][c + 1] + row_sum

    def rect_sum(r1, c1, r2, c2):
        return (
            ps[r2 + 1][c2 + 1]
            - ps[r1][c2 + 1]
            - ps[r2 + 1][c1]
            + ps[r1][c1]
        )

    max_area = 0
    n_red = len(red_tiles_rc)

    for i in range(n_red):
        r1, c1 = red_tiles_rc[i]
        for j in range(i + 1, n_red):
            r2, c2 = red_tiles_rc[j]

            # Must form proper rectangle: different rows and columns
            if r1 == r2 or c1 == c2:
                continue

            top    = min(r1, r2)
            bottom = max(r1, r2)
            left   = min(c1, c2)
            right  = max(c1, c2)

            # Check if all cells in this rectangle are red/green
            cell_count = (bottom - top + 1) * (right - left + 1)
            if rect_sum(top, left, bottom, right) != cell_count:
                continue

            # Compute true area in original coordinate system
            # (opposite corners are at (xs[c1], ys[r1]) and (xs[c2], ys[r2]))
            x1, y1 = xs[c1], ys[r1]
            x2, y2 = xs[c2], ys[r2]
            width  = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area   = width * height

            if area > max_area:
                max_area = area

    return max_area


def star1() -> int:
    data = read_input()
    rectangle_edges = []
    rectangles = len(data)
    for d in data:
        x, y = map(int, d.split(","))
        rectangle_edges.append([x, y])
    potential_combos = list(combinations(rectangle_edges, 2))
    max_area=0
    for r1,r2 in potential_combos:
        x1,y1 = r1
        x2,y2 = r2
        area = (abs(x2-x1)+1)*(abs(y2-y1)+1)

        if area>max_area:
            max_area = area
    return max_area

def star2() -> int:
    data = read_input()
    rectangle_edges = []
    for d in data:
        x, y = map(int, d.split(","))
        rectangle_edges.append([x, y])
    grid, red_rc, xs, ys = build_compressed_grid_from_loop(rectangle_edges)
    return largest_rectangle_red_green(grid, red_rc, xs, ys)



if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
