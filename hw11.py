#參考chatgpt
import numpy as np

def solve_polynomial(coefficients):
    # 使用 numpy.roots 函數解 n 次多項式的方程
    roots = np.roots(coefficients)
    return roots

# 使用者輸入多項式的係數（由高次到低次且空格分隔）
coefficients = list(map(float, input("輸入多項式的係數（由高次到低次，空格分隔）: ").split()))

# 調用函數解方程並輸出結果
solution = solve_polynomial(coefficients)
print("方程的解為:", solution)
