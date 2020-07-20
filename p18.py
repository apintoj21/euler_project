"""Maximum path sum I
Problem statement:

By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""
grid_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def str_grid_list(string1):
    grid_lines = string1.split("\n")
    grid_tri = []
    for x in range(15):
        grid_tri.append(grid_lines[x].split(" "))
    return grid_tri


# def maxi_path_sum(grid, num_rows):
#     row_index = 0
#     sum_path = int(grid[0][0])
#     for i in range(1, num_rows):
#         if grid[i][row_index] > grid[i][row_index + 1]:
#             sum_path += int(grid[i][row_index])
#             print(sum_path)
#         else:
#             sum_path += int(grid[i][row_index + 1])
#             row_index += 1
#             print(sum_path)
#     print(sum_path)
#     return sum_path
def maxi_path_sum(grid, num_rows):
    for i in range(num_rows - 2, -1, -1):
        for j in range(i + 1):
            grid[i][j] = int(grid[i][j]) + max(int(grid[i + 1][j]), int(grid[i + 1][j + 1]))
    return grid[0][0]


def main():
    grid1 = str_grid_list(grid_str)
    path_sum = maxi_path_sum(grid1, 15)
    print(path_sum)


if __name__ == "__main__":
    main()
