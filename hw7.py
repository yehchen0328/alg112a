#有使用chatgpt做輔助
#參考老師提供教材https://github.com/ccc-py/micrograd/

from micrograd.engine import Value

# 創建三個 Value 實例 a、b、c
a = Value(4.0)  # 將初始值改為正數
b = Value(2.0)
c = Value(1.5)  # 添加第三個變數 c，您可以設置為任何您需要的值

# 設定梯度值
gradient_threshold = 0.001

# 初始化計數器
iteration = 0

# 優化迴圈
while iteration < 2000:  # 次數為 2000

    # 定義目標函數
    target_function = a**2 + b**2 + c**2

    print("a=", a.data, "b=", b.data, "c=", c.data,)
    # 正向傳播
    target_function.backward()


    # 檢查梯度值
    if a.grad < gradient_threshold or b.grad < gradient_threshold or c.grad < gradient_threshold:
        break

    # 更新變數 a、b、c 的值
    a -= a.grad * 0.01  # 使用梯度下降更新參數
    b -= b.grad * 0.01
    c -= c.grad * 0.01
    
 
    
