#參考Chatgpt
# 檢查在當前位置放置皇后是否安全
def is_safe(board, row, col, n):

    # 檢查同一列是否有皇后
    for i in range(row):
        if board[i][col] == 1:

            return False

    # 檢查左上到右下的對角線是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):

        if board[i][j] == 1:
            return False

    # 檢查右上到左下的對角線是否有皇后
    for i, j in zip(range(row, -1, -1), range(col, n)):

        if board[i][j] == 1:

            return False

    return True

# 用於使用回溯法解決 N 皇后問題的輔助函數
def solve_n_queens_util(board, row, n):

    # 如果所有皇后都放置完畢
    if row == n:
        print_solution(board)
        return

    # 嘗試在當前行的每一列放置皇后
    for col in range(n):

        # 檢查在當前位置放置皇后是否安全
        if is_safe(board, row, col, n):

            # 放置皇后
            board[row][col] = 1

            # 處理下一行
            solve_n_queens_util(board, row + 1, n)

            # 回溯：從當前位置移除皇后
            board[row][col] = 0


def print_solution(board):

    for row in board:
        print(" ".join(map(str, row)))

    print("\n")

# 主函數用於解決 N 皇后問題
def solve_n_queens(n):

    # 將棋盤初始化為全零
    board = [[0] * n for _ in range(n)]

    # 開始遞歸的回溯過程
    solve_n_queens_util(board, 0, n)

# 調用函數解決 8 皇后問題
solve_n_queens(8)
