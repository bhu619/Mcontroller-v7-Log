import pandas as pd
import numpy as np

# 创建一个示例DataFrame
data = pd.DataFrame({
    'tar_x': [1.0, 2.0, 3.0],
    'odom_x': [1.1, 2.1, 2.9],
    'tar_y': [1.0, 2.0, 3.0],
    'odom_y': [0.9, 2.0, 3.1],
    'tar_z': [1.0, 2.0, 3.0],
    'odom_z': [1.0, 2.0, 2.8]
})

# 计算误差
data['x_e'] = data['tar_x'] - data['odom_x']
data['y_e'] = data['tar_y'] - data['odom_y']
data['z_e'] = data['tar_z'] - data['odom_z']

# 计算RMSE
rmse_pos = np.sqrt(np.mean(data['x_e']**2 + data['y_e']**2 + data['z_e']**2))
print()
print(f"RMSE of position: {rmse_pos}")