import numpy as np

# 创建一个二维 NumPy 数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# 沿着水平轴计算二维数组的平均值
mean_value_axis0 = np.mean(arr2d, axis=0)
print(mean_value_axis0)  # 输出：[5.5 6.5 7.5]

# 沿着垂直轴计算二维数组的平均值
mean_value_axis1 = np.mean(arr2d, axis=1)
print(mean_value_axis1)  # 输出：[2. 5. 8. 11.]

