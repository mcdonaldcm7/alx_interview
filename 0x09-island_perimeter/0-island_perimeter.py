#!/usr/bin/python3
"""
Tasks

0. Island Perimeter

Create a function def island_perimeter(grid): that returns the perimeter of the
island described in grid:

    - grid is a list of list of integers:
        * 0 represents water
        * 1 represents land
        * Each cell is square, with a side length of 1
        * Cells are connected horizontally/vertically (not diagonally).
        * 'grid' is rectangular, with its width and height not exceeding 100
    - The grid is completely surrounded by water
    - There is only one island (or nothing).
    - The island doesn’t have “lakes” (water inside that isn’t connected to the
    water surrounding the island).

    guillaume@ubuntu:~/0x09$ cat 0-main.py
    #!/usr/bin/python3
    ""
    0-main
    ""
    island_perimeter = __import__('0-island_perimeter').island_perimeter

    if __name__ == "__main__":
        grid = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        print(island_perimeter(grid))

    guillaume@ubuntu:~/0x09$
    guillaume@ubuntu:~/0x09$ ./0-main.py
    12
    guillaume@ubuntu:~/0x09$
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 1:
                perimeter += 4
                if (y - 1) >= 0 and grid[y - 1][x] == 1:
                    perimeter -= 1
                if (y + 1) < rows and grid[y + 1][x] == 1:
                    perimeter -= 1
                if (x - 1) >= 0 and grid[y][x - 1]:
                    perimeter -= 1
                if (x + 1) < cols and grid[y][x + 1]:
                    perimeter -= 1
    return perimeter
