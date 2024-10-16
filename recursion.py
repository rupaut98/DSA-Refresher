def compute_factorial(n):
    if n <= 1:
        return 1
    
    return n * compute_factorial(n-1)

def fibonacci_seqence(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_seqence(n-1) + fibonacci_seqence(n-2)

def power_of_three(n):
    if n == 1:
        return True
    if n <= 0:
        return False
    
    if n % 3 == 0:
        return power_of_three(n//3)
    
    return False

def reverse_string(n):
    if len(n) == 0 or len(n) == 1:
        return n
    
    return reverse_string(n[1:]) + n[0]

def sum_numbers(n):
    if n < 10:
        return n
    
    return n % 10 + sum_numbers(n // 10)

def count_occurences(number, digit):
    if number == 0:
        return 0
        
    if number % 10 == digit:
        return 1 + count_occurences(number // 10, digit)
    else:
        return count_occurences(number // 10, digit)
    

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    
    rest_max = find_max(arr[1:])

    if arr[0] > rest_max:
        return arr[0]
    else:
        return rest_max
    
def permutation_string(s):
    if len(s) == 1:
        return [s]
    
    permutations = []

    for i in range(len(s)):
        char = s[i]
        remaining_string = s[:i] + s[i+1:]

        remaining_permutations = permutation_string(remaining_string)

        for perm in remaining_permutations:
            permutations.append(char + perm)
        
    return permutations

def sum_target(arr, target):
    if target == 0:
        return True
    
    if target < 0:
        return False
    
    for i in range(len(arr)):
        num = arr[i]
        target_dup = target

        if num <= target_dup:
            target_dup -= num
            found = sum_target(arr[i+1:], target_dup)
            if found:
                return True
            
        found = sum_target(arr[i+1:], target_dup)
        if found:
            return True

    return False

def count_paths(i, j, m, n):
    if i == m-1 and j == n-1:
        return 1
    if i > m-1 or j > n-1:
        return 0
    
    return count_paths(i, j + 1, m, n) + count_paths(i + 1, j, m, n)

def maze_paths(i, j, m, n, maze):
    if i == m-1 and j==n-1:
        return 1
    if i > m-1 or j > n-1 or maze[i][j] == 1:
        return 0
    
    maze[i][j] = 1

    paths = 0

    paths += maze_paths(i, j+1, m, n, maze)
    paths += maze_paths(i+1, j, m, n, maze)
    paths += maze_paths(i-1, j, m, n, maze)
    paths += maze_paths(i, j-1, m, n, maze)

    maze[i][j] = 0

    return paths



def count_islands(m, n, grid):
    islands = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                explore_island(m, n, i, j, grid)
                islands += 1
    return islands

def explore_island(m, n, i, j, grid):
    if i > m-1 or j > n-1 or i < 0 or j < 0:
        return
    if grid[i][j] == 0:
        return
    
    grid[i][j] = 0

    explore_island(m, n, i+1,j, grid)
    explore_island(m, n, i-1,j, grid)
    explore_island(m, n, i,j+1, grid)
    explore_island(m, n, i, j-1, grid)


def distinct_shape_islands(m, n, grid):
    set_shapes = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                island_shape=set()
                i_start, j_start = i, j
                recursive_exploration(m, n, i, j, grid, island_shape, i_start, j_start)
                set_shapes.add(frozenset(island_shape))

    return len(set_shapes)


def recursive_exploration(m, n, i, j, grid, island_shape, i_start, j_start):
    if i > m-1 or j>n-1 or i<0 or j<0:
        return
    if grid[i][j]==0:
        return

    relative_position = (i - i_start, j - j_start)
    island_shape.add(relative_position)

    recursive_exploration(m, n, i+1, j, grid, island_shape, i_start, j_start)
    recursive_exploration(m, n, i-1, j, grid, island_shape, i_start, j_start)
    recursive_exploration(m, n, i, j+1, grid, island_shape, i_start, j_start)
    recursive_exploration(m, n, i, j-1, grid, island_shape, i_start, j_start)







    


        

        




        


    
