"""
Mcontroller-v7 飞行日志数据读取、预处理、误差计算模块
"""
import pandas as pd
import numpy as np
import os


# 读取文件数据 并做数据预处理
def read_data(_data, vc, cc):
    data = pd.read_csv(_data, sep='\s+')
    data.columns = data.columns.str.strip()  # 去除列名中的前后空格

    data.loc[:, 't_ms'] = data['t_ms'] - data['t_ms'].min()  # 处理时间 t_ms
    data['t_s'] = data['t_ms'] * 0.001  # ms转换为s

    # # 删除 85 <= t_s < 92 的数据
    # mask_to_delete = (data['t_s'] >= 85) & (data['t_s'] < 92)
    # data = data.loc[~mask_to_delete]  # 保留不在该范围内的数据
    # # 标记 92s 之后的部分
    # mask_shift = data['t_s'] >= 92  # 找到 t_s >= 92 的行
    #
    # # 将 92s 之后的数据整体前移 7s
    # data.loc[mask_shift, 't_s'] -= 7
    #
    # # 删除时间点重复的数据，只保留最早的行
    # data = data.drop_duplicates(subset='t_s', keep='first')
    # data['t_s'] -= 35
    #
    # # 为重复时间点增加微小偏移量
    # while data['t_s'].duplicated().any():
    #     duplicated_indices = data[data['t_s'].duplicated()].index
    #     data.loc[duplicated_indices, 't_s'] += 0.001  # 每次加 0.001s

    data['t_out'] = data['t_out'] * 100  # 油门数据 放大为 0 ~ 100

    data['odom_x'] = data['odom_x'] * 0.01  # 单位 cm 变为 m
    data['odom_y'] = data['odom_y'] * 0.01  # 单位 cm 变为 m
    data['tar_x'] = data['tar_x'] * 0.01  # 单位 cm 变为 m
    data['tar_y'] = data['tar_y'] * 0.01  # 单位 cm 变为 m
    data['rf_alt_t'] = data['rf_alt_t'] * 0.01
    data['rf_alt'] = data['rf_alt'] * 0.01

    # # 根据 t_out 条件设置电流和电压系数
    # data['current_coefficient'] = data['t_out'].apply(lambda x: 4 if x < 10 else 1.5)
    # data['voltage_coefficient'] = data['t_out'].apply(lambda x: 2 if x < 10 else 13.7)
    #
    # # 更新电流和电压值
    # data['current'] = data['current'] * data['current_coefficient']
    # data['voltage'] = data['voltage'] * data['voltage_coefficient']

    data['current'] = data['current'] * cc  # current_coefficient 为电流系数
    data['voltage'] = data['voltage'] * vc  # voltage_coefficient 为电压系数
    data['power'] = data['voltage'] * data['current']  # 计算功率 P

    # 计算姿态角误差
    data['pitch_e'] = data['pitch_t'] - data[
        'pitch_log']  # 计算 pitch_t (目标俯仰角) - pitch_log (当前俯仰角), 得到结果记为"pitch_e"并保存到新的一列
    data['roll_e'] = data['roll_t'] - data[
        'roll_log']
    data['yaw_e'] = data['yaw_t'] - data['yaw_log']

    return data


# 数据处理
def filter_data(data, folder_path, min_t_out, max_t_out, min_t_s, max_t_s, vc, cc):
    # 筛选 't_out' 的数据
    filtered_data = data[(data['t_out'] >= min_t_out) & (data['t_out'] <= max_t_out)].copy()
    # 筛选出 't_ms' 在 min_t_ms 和 max_t_ms 之间的数据
    filtered_data_2 = filtered_data[
        (filtered_data['t_s'] <= max_t_s) & (filtered_data['t_s'] >= min_t_s)].copy()

    # 计算筛选后数据中油门的最大值
    max_throttle = filtered_data_2['t_out'].max()
    max_pitch = filtered_data_2['pitch_log'].max()
    min_pitch = filtered_data_2['pitch_log'].min()
    max_roll = filtered_data_2['roll_log'].max()
    min_roll = filtered_data_2['roll_log'].min()
    max_yaw = filtered_data_2['yaw_log'].max()
    min_yaw = filtered_data_2['yaw_log'].min()

    max_pitch_e = filtered_data_2['pitch_e'].max()
    min_pitch_e = filtered_data_2['pitch_e'].min()
    max_roll_e = filtered_data_2['roll_e'].max()
    min_roll_e = filtered_data_2['roll_e'].min()
    max_yaw_e = filtered_data_2['yaw_e'].max()
    min_yaw_e = filtered_data_2['yaw_e'].min()

    avg_power = filtered_data_2['power'].mean()
    avg_current = filtered_data_2['current'].mean()
    avg_voltage = filtered_data_2['voltage'].mean()

    file_path_filter = f'{folder_path}\\filter_data.txt'
    # 使用 'with' 和 'open' 创建新文件并写入数据
    with open(file_path_filter, 'w') as file:
        file.write(f"最小时间 : {min_t_s} (s)\n")
        file.write(f"最大时间 : {max_t_s} (s)\n")
        file.write(f"最小油门 : {min_t_out}\n")
        file.write(f"最大油门 : {max_t_out}\n")
        file.write(f"最大Pitch : { max_pitch } (°)\n")
        file.write(f"最小Pitch : { min_pitch } (°)\n")
        file.write(f"最大Roll  : { max_roll } (°)\n")
        file.write(f"最小Roll  : { min_roll } (°)\n")
        file.write(f"最大Yaw   : { max_yaw } (°)\n")
        file.write(f"最小Yaw   : { min_yaw } (°)\n")
        file.write(f"平均功率   : { avg_power:.3f} (W)\n")
        file.write(f"平均电流   : { avg_current:.3f} (A)\n")
        file.write(f"平均电压   : { avg_voltage:.3f} (V)\n")
        file.write(f"电压修正系数   : { vc }\n")
        file.write(f"电流修正系数   : { cc }\n")
        file.write(f"最大Pitch误差 : {max_pitch_e:.3f} (°)\n")
        file.write(f"最小Pitch误差 : {min_pitch_e:.3f} (°)\n")
        file.write(f"最大Roll误差  : {max_roll_e:.3f} (°)\n")
        file.write(f"最小Roll误差  : {min_roll_e:.3f} (°)\n")
        file.write(f"最大Yaw误差   : {max_yaw_e:.3f} (°)\n")
        file.write(f"最小Yaw误差   : {min_yaw_e:.3f} (°)\n")

        file.write(f"飞行中油门的最大值 : {max_throttle}\n")

    print(f"Data has been successfully saved to {file_path_filter}.")

    return filtered_data_2


def set_target_values(data):
     data['pitch_t'] = 0.0
    # data['roll_t'] = 0.0
    # data['yaw_t'] = 0.0


def calc_rmse_mae(data, folder_path):

    # 计算 RMSE
    rmse_pitch = np.sqrt(np.mean(data['pitch_e'] ** 2))
    rmse_roll = np.sqrt(np.mean(data['roll_e'] ** 2))
    rmse_yaw = np.sqrt(np.mean(data['yaw_e'] ** 2))

    # 计算 MAE
    mae_pitch_e = np.mean(np.abs(data['pitch_e']))
    mae_roll_e = np.mean(np.abs(data['roll_e']))
    mae_yaw_e = np.mean(np.abs(data['yaw_e']))

    data['x_e'] = data['tar_x'] - data['odom_x']
    data['y_e'] = data['tar_y'] - data['odom_y']
    data['z_e'] = data['rf_alt_t'] - data['rf_alt']

    rmse_pos = np.sqrt(np.mean(data['x_e']**2 + data['y_e']**2 + data['z_e']**2))

    # print(f"Mean square error of x position: {np.mean(data['x_e']**2)}\n")
    # print(f"Mean square error of y position: {np.mean(data['y_e']**2)}\n")
    # print(f"Mean square error of z position: {np.mean(data['z_e']**2)}\n")

    # 写入文件
    file_path_rmse = os.path.join(folder_path, 'calculate_error.txt')
    try:
        with open(file_path_rmse, 'w') as file:
            file.writelines([
                f"RMSE Pitch : {rmse_pitch:.3f} (°)\n",
                f"RMSE Roll   : {rmse_roll:.3f} (°)\n",
                f"RMSE YAW : {rmse_yaw:.3f} (°)\n\n",
                f"RMSE POS  : {rmse_pos:.3f} (m)\n\n",
                f"MAE  Pitch  : {mae_pitch_e:.3f} (°)\n",
                f"MAE  Roll    : {mae_roll_e:.3f} (°)\n",
                f"MAE  YAW  : {mae_yaw_e:.3f} (°)\n"
            ])
        print(f"Data has been successfully saved to {file_path_rmse}.\n")
    except Exception as e:
        print(f"Failed to write data to file: {e}")
