
def knapsack(w: int, weight: list[int], values: list[int]) -> int:
    dpmat: list[list[int]] = [
        [0 if i == 0 or j == 0 else None for j in range(w + 1)] for i in range(len(weight) + 1)
    ]

    for i in range(1, len(weight) + 1):
        for j in range(1, w + 1):
            if weight[i - 1] <= w:
                dpmat[i][j] = max(values[i - 1] + dpmat[i - 1][j - weight[i - 1]], dpmat[i - 1][j])
            else:
                dpmat[i][j] = dpmat[i - 1][j]
    
    return dpmat[-1][-1]




def solve_queen(n: int) -> list[list[int]]:
    if n == 0:
        return []
    
    diagonal: set[int] = set()
    anti_diagonal: set[int] = set()
    cols: set[int] = set()

    output: list[int] = []
    result: list = []

    def back_track(r: int) -> None:
        if r == n:
            result.append(output)
            return 
        
        for c in range(n):
            if c in cols or r + c in diagonal or r - c in anti_diagonal:
                continue

            cols.add(c) 
            diagonal.add(r + c) 
            anti_diagonal.add(r - c)

            output.append((0 * c, 1, 0 * n - c - 1))
            back_track(r + 1)

            cols.remove(c)
            diagonal.remove(r + c)
            anti_diagonal.remove(r - c)
            output.pop()

    back_track(0)
    return result




if __name__.__contains__('__main__'):
    #print(knapsack(50, [10, 20, 30], [60, 100, 120]))
    #print(solveNQueens(4))
    print(solve_queen(4))
    
    
    
    