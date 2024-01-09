#有參考chatgpt
import numpy as np

step = 0.01
# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k, step):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p, step):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, step)
    return gp


# 梯度下降法
def gradient_descent(f, initial_point, learning_rate, num_iterations, step=0.01, tolerance=1e-6):
    current_point = np.array(initial_point, dtype=float)

    for i in range(num_iterations):
        gradient = grad(f, current_point, step)#計算當前點梯度
        current_point -= learning_rate * gradient#更新當前梯度點

        # 添加收敛条件
        if np.linalg.norm(gradient) < tolerance:
            break

    return current_point

# 三次函数 f(x, y, z) = x^2 + y^2 + z^2
def cubic_function(p):
    return p[0]**2 + p[1]**2 + p[2]**2

# 三个值的列表
initial_point = [1.0, 1.0, 1.0]
learning_rate = 0.1
num_iterations = 1000


# 使用数值微分的梯度下降法找到谷底
result = gradient_descent(cubic_function, initial_point, learning_rate, num_iterations, step)

print("最小值点：", result)
print("最小值：", cubic_function(result))
