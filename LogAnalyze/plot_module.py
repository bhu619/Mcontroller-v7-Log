"""
图片绘制模块, 包含所有需要用到的制图函数
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
import pandas as pd
import numpy as np

# 全局设置
plt.rcParams['font.family'] = 'Times New Roman'  # 设置全局字体为 Times New Roman
label_fontsize = 30   # 控制轴标签的字体大小
axis_fontsize = 25    # 控制坐标轴字体大小
legend_fontsize = 30  # 控制图例的字体大小
text_size = 30        # 控制图标中的字体大小
formatter = ticker.FormatStrFormatter('%.1f')  # 定义格式化函数，保留两位小数


def plot_pitch(data, folder_path, y_min, y_max):
    # 绘制 "pitch_t"、"pitch_log" 随 "t_ms" 变化的折线图
    plt.figure(figsize=(12, 6))

    plt.plot(data['t_s'], data['pitch_t'], label='Desired', color='#3572EF',
             linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['pitch_log'], label='Actual', color='red',
             linestyle='-', linewidth=2)

    plt.xlabel('Time (s)')
    plt.ylabel('Pitch (°)')
    plt.ylim(y_min, y_max)  # 设置纵坐标范围为 -30 到 30
    plt.legend()
    plt.grid(True, alpha=0.5)
    file_name = 'pitch.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_roll(data, folder_path, y_min, y_max):
    # Roll
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['roll_t'], label='Desired', color='#3572EF',
             linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['roll_log'], label='Actual', color='red',
             linestyle='-', linewidth=2)

    plt.xlabel('Time (s)')  # 设置X轴标签
    plt.ylabel('Roll (°)')  # 设置Y轴标签
    plt.ylim(y_min, y_max)  # 设置纵坐标范围为 -30 到 30
    plt.legend()  # 显示图例
    plt.grid(True, alpha=0.5)

    file_name = 'roll.png'  # 定义图片的文件名
    # 保存图像到指定文件夹
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_yaw(data, folder_path, y_min, y_max):
    # Yaw
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['yaw_t'], label='Desired', color='#3572EF',
             linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['yaw_log'], label='Actual', color='red',
             linestyle='-', linewidth=2)

    plt.xlabel('Time (s)')  # 设置X轴标签
    plt.ylabel('Yaw (°)')  # 设置Y轴标签
    plt.legend()  # 显示图例
    plt.grid(True, alpha=0.5)  # 显示网格
    plt.ylim(y_min, y_max)
    file_name = 'yaw.png'  # 定义图片的文件名
    # 保存图像到指定文件夹
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_pitch_error(data, folder_path, y_min, y_max):
    # Pitch_error
    plt.figure(figsize=(12, 6))  # 设置图形的尺寸
    plt.plot(data['t_s'], data['pitch_e'], label='Pitch Error', color='#FF5F00', linestyle='-', linewidth=3)

    plt.xlabel('Time (s)')  # 设置X轴标签
    plt.ylabel('Pitch Error (°)')
    plt.ylim(y_min, y_max)
    plt.legend()  # 显示图例
    plt.grid(True, alpha=0.5)  # 显示网格
    file_name = 'pitch_error.png'  # 定义图片的文件名
    # 保存图像到指定文件夹
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_roll_error(data, folder_path, y_min, y_max):
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['roll_e'], label='Roll Error', color='#FF5F00', linestyle='-', linewidth=3)

    plt.xlabel('Time (s)')
    plt.ylabel('Roll Error (°)')
    plt.legend()
    plt.ylim(y_min, y_max)
    plt.grid(True, alpha=0.5)
    file_name = 'roll_error.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_yaw_error(data, folder_path, y_min, y_max):
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['yaw_e'], label='Yaw Error', color='#FF5F00', linestyle='-', linewidth=3)

    plt.xlabel('Time (s)')  # 设置X轴标签
    plt.ylabel('Yaw Error (°)')  # 设置Y轴标签，因为绘制多种数据类型，使用通用标签
    plt.ylim(y_min, y_max)
    plt.legend()  # 显示图例
    plt.grid(True, alpha=0.5)  # 显示网格
    file_name = 'yaw_error.png'  # 定义图片的文件名
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_x_position(data, folder_path, y_min, y_max):
    # Position_x 里程计x轴位置
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['tar_x'], label='Desired', color='#3572EF',
             linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['odom_x'], label='Actual', color='red',
             linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('X (m)')
    plt.ylim(y_min, y_max)
    plt.legend()
    plt.grid(True, alpha=0.5)
    file_name = 'pos_x.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_y_position(data, folder_path, y_min, y_max):
    # Position_y 里程计y轴位置
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['tar_y'], label='Desired', color='#3572EF',
             linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['odom_y'], label='Actual', color='red',
             linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Y (m)')
    plt.ylim(y_min, y_max)
    plt.legend()
    plt.grid(True, alpha=0.5)
    file_name = 'pos_y.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_z_position(data, folder_path, y_min, y_max):
    # rf_alt: 激光测距仪z轴位置
    # odom_z: 里程计z轴位置
    # alt_t: z轴目标位置
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['rf_alt_t'], label='Desired', color='#3572EF',
             linestyle='-', linewidth=2)
    # plt.plot(data['t_s'], data['odom_z'], label='odom_z', color='red',
    #         linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['rf_alt'], label='Actual', color='red',
             linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Z (m)')
    plt.ylim(y_min, y_max)
    plt.legend()
    plt.grid(True, alpha=0.5)
    file_name = 'pos_z.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_rpy(data, folder_path,
             p_min, p_max, r_min, r_max, yaw_min, yaw_max):
    fig, axs = plt.subplots(3, 1, figsize=(12, 9), sharex=True) # 宽 * 高
    # 设置字体大小
    _label_fontsize = 25
    _title_fontsize = 25
    _legend_fontsize = 20
    _text_fontsize = 28  # 文本字体
    _axis_labelsize = 20  # 坐标轴字体

    # axs[0].plot(data['t_s'], data['pitch_t'], label='Desired', color='#3D00F5',
    #              linestyle='-', linewidth=2)
    axs[0].plot(data['t_s'], data['pitch_log'], label='Pitch', color='red',
                   linestyle='-', linewidth=2)
    axs[0].set_ylabel('Pitch (°)', fontsize=_label_fontsize)
    axs[0].set_ylim(p_min, p_max)
    axs[0].legend(fontsize=_legend_fontsize)
    axs[0].grid(True, alpha=0.5)
    axs[0].yaxis.set_major_formatter(formatter)
    axs[0].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # axs[1].plot(data['t_s'], data['roll_t'], label='Desired', color='#3D00F5',
    #              linestyle='-', linewidth=2)
    axs[1].plot(data['t_s'], data['roll_log'], label='Roll', color='red',
                   linestyle='-', linewidth=2)
    axs[1].set_ylabel('Roll (°)', fontsize=_label_fontsize)
    axs[1].set_ylim(r_min, r_max)
    axs[1].legend(fontsize=_legend_fontsize)
    axs[1].grid(True, alpha=0.5)
    axs[1].yaxis.set_major_formatter(formatter)
    axs[1].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # axs[2].plot(data['t_s'], data['yaw_t'], label='Desired', color='#3D00F5',
    #               linestyle='-', linewidth=2)
    axs[2].plot(data['t_s'], data['yaw_log'], label='Yaw', color='red',
                   linestyle='-', linewidth=2)
    axs[2].set_ylabel('Yaw (°)', fontsize=_label_fontsize)
    axs[2].set_ylim(yaw_min, yaw_max)
    axs[2].legend(fontsize=_legend_fontsize)
    axs[2].grid(True, alpha=0.5)
    axs[2].yaxis.set_major_formatter(formatter)
    axs[2].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # 设置共享的X轴标签
    axs[2].set_xlabel('Time (s)', fontsize=_title_fontsize)
    axs[2].xaxis.set_major_formatter(formatter)
    plt.tight_layout()

    # 保存图像
    file_name = 'rpy.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_rpy_e(data, folder_path,
               pitch_min_e, pitch_max_e,
               roll_min_e, roll_max_e, yaw_min_e, yaw_max_e):
    fig, axs = plt.subplots(3, 1, figsize=(12, 9), sharex=True) # 宽 * 高
    # 设置字体大小
    _label_fontsize = 25
    _title_fontsize = 25
    _legend_fontsize = 20
    _text_fontsize = 28  # 文本字体
    _axis_labelsize = 20  # 坐标轴字体

    # axs[0].plot(data['t_s'], data['pitch_t'], label='Desired', color='#3D00F5',
    #              linestyle='-', linewidth=2)
    axs[0].plot(data['t_s'], data['pitch_e'], label='Pitch Error', color='#FF5F00', linestyle='-', linewidth=2)
    axs[0].set_ylabel('Pitch Error(°)', fontsize=_label_fontsize)
    axs[0].set_ylim(pitch_min_e, pitch_max_e)
    axs[0].legend(fontsize=_legend_fontsize)
    axs[0].grid(True, alpha=0.5)
    axs[0].yaxis.set_major_formatter(formatter)
    axs[0].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # axs[1].plot(data['t_s'], data['roll_t'], label='Desired', color='#3D00F5',
    #              linestyle='-', linewidth=2)
    axs[1].plot(data['t_s'], data['roll_e'], label='Roll Error', color='#FF5F00',
                   linestyle='-', linewidth=2)
    axs[1].set_ylabel('Roll Error(°)', fontsize=_label_fontsize)
    axs[1].set_ylim(roll_min_e, roll_max_e)
    axs[1].legend(fontsize=_legend_fontsize)
    axs[1].grid(True, alpha=0.5)
    axs[1].yaxis.set_major_formatter(formatter)
    axs[1].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # axs[2].plot(data['t_s'], data['yaw_t'], label='Desired', color='#3D00F5',
    #               linestyle='-', linewidth=2)
    axs[2].plot(data['t_s'], data['yaw_e'], label='Yaw Error', color='#FF5F00',
                   linestyle='-', linewidth=2)
    axs[2].set_ylabel('Yaw Error(°)', fontsize=_label_fontsize)
    axs[2].set_ylim(yaw_min_e, yaw_max_e)
    axs[2].legend(fontsize=_legend_fontsize)
    axs[2].grid(True, alpha=0.5)
    axs[2].yaxis.set_major_formatter(formatter)
    axs[2].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # 设置共享的X轴标签
    axs[2].set_xlabel('Time (s)', fontsize=_title_fontsize)
    axs[2].xaxis.set_major_formatter(formatter)
    plt.tight_layout()

    # 保存图像
    file_name = 'rpy_error.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_rpy_transition(data, folder_path,
                        p_min, p_max, r_min, r_max, yaw_min, yaw_max):
    fig, axs = plt.subplots(3, 1, figsize=(12, 9), sharex=True) # 宽 * 高
    # 设置字体大小
    _label_fontsize = 25
    _title_fontsize = 25
    _legend_fontsize = 20
    _text_fontsize = 28  # 文本字体
    _axis_labelsize = 20  # 坐标轴字体

    axs[0].plot(data['t_s'], data['pitch_log'], label='Actual', color='red',
                   linestyle='-', linewidth=2)
    axs[0].set_ylabel('Pitch (°)', fontsize=_label_fontsize)
    axs[0].set_ylim(p_min, p_max)
    axs[0].legend(fontsize=_legend_fontsize)
    axs[0].grid(True, alpha=0.5)
    axs[0].yaxis.set_major_formatter(formatter)
    axs[0].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    def find_nearest_time(target_time):
        # 使用 idxmin() 查找与 target_time 最接近的时间点索引
        idx_nearest = (data['t_s'] - target_time).abs().idxmin()
        return data.loc[idx_nearest]

    # 查找 Time = 41.0 或最接近的点
    closest_to_41 = find_nearest_time(41.0)
    axs[0].scatter(closest_to_41['t_s'], closest_to_41['pitch_log'], color='black', s=60)

    # 使用 annotate 添加带箭头的标注
    axs[0].annotate('Start of mode transition',
                    xy=(closest_to_41['t_s'], closest_to_41['pitch_log']),  # 箭头指向的点
                    xytext=(closest_to_41['t_s'] - 2, closest_to_41['pitch_log'] + 10),  # 文本的位置
                    fontsize=_text_fontsize,
                    arrowprops=dict(facecolor='black', arrowstyle="->", linewidth=3),  # 设置箭头样式
                    ha='center')

    closest_to_50 = find_nearest_time(50.0)
    axs[0].scatter(closest_to_50['t_s'], closest_to_50['pitch_log'], color='black', s=60)

    # 使用 annotate 添加带箭头的标注
    axs[0].annotate('Take off',
                    xy=(closest_to_50['t_s'], closest_to_50['pitch_log']),  # 箭头指向的点
                    xytext=(closest_to_50['t_s'] + 3, closest_to_50['pitch_log'] + 10),  # 文本的位置
                    fontsize=_text_fontsize,
                    arrowprops=dict(facecolor='black', arrowstyle="->", linewidth=3),  # 设置箭头样式
                    ha='center')

    axs[1].plot(data['t_s'], data['roll_log'], label='Actual', color='red',
                   linestyle='-', linewidth=2)
    axs[1].set_ylabel('Roll (°)', fontsize=_label_fontsize)
    axs[1].set_ylim(r_min, r_max)
    axs[1].legend(fontsize=_legend_fontsize)
    axs[1].grid(True, alpha=0.5)
    axs[1].yaxis.set_major_formatter(formatter)
    axs[1].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    axs[2].plot(data['t_s'], data['yaw_log'], label='Actual', color='red',
                   linestyle='-', linewidth=2)
    axs[2].set_ylabel('Yaw (°)', fontsize=_label_fontsize)
    axs[2].set_ylim(yaw_min, yaw_max)
    axs[2].legend(fontsize=_legend_fontsize)
    axs[2].grid(True, alpha=0.5)
    axs[2].yaxis.set_major_formatter(formatter)
    axs[2].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # 设置共享的X轴标签
    axs[2].set_xlabel('Time (s)', fontsize=_title_fontsize)
    axs[2].xaxis.set_major_formatter(formatter)
    plt.tight_layout()

    # 保存图像
    file_name = 'rpy.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_rpy_xyz_pos(data, folder_path,
                     p_min, p_max, r_min, r_max, yaw_min, yaw_max,
                     x_min, x_max, y_min, y_max, z_min, z_max):
    fig, axs = plt.subplots(3, 2, figsize=(18, 9), sharex='col') # 宽 * 高
    # 设置字体大小
    _label_fontsize = 30  # 标签
    _title_fontsize = 25  # 标题
    _legend_fontsize = 17  # 图例
    _axis_labelsize = 20  # 坐标轴字体

    axs[0, 0].plot(data['t_s'], data['pitch_t'], label='Desired', color='#3D00F5',
                   linestyle='-', linewidth=2)
    axs[0, 0].plot(data['t_s'], data['pitch_log'], label='Actual', color='red',
                   linestyle='-', linewidth=2)
    axs[0, 0].set_ylabel('Pitch (°)', fontsize=_label_fontsize)
    axs[0, 0].set_ylim(p_min, p_max)
    axs[0, 0].legend(fontsize=_legend_fontsize)
    axs[0, 0].grid(True, alpha=0.5)
    axs[0, 0].yaxis.set_major_formatter(formatter)
    axs[0, 0].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    axs[1, 0].plot(data['t_s'], data['roll_t'], label='Desired', color='#3D00F5',
                   linestyle='-', linewidth=2)
    axs[1, 0].plot(data['t_s'], data['roll_log'], label='Actual', color='red',
                   linestyle='-', linewidth=2)
    axs[1, 0].set_ylabel('Roll (°)', fontsize=_label_fontsize)
    axs[1, 0].set_ylim(r_min, r_max)
    axs[1, 0].legend(fontsize=_legend_fontsize)
    axs[1, 0].grid(True, alpha=0.5)
    axs[1, 0].yaxis.set_major_formatter(formatter)
    axs[1, 0].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    axs[2, 0].plot(data['t_s'], data['yaw_t'], label='Desired', color='#3D00F5',
                   linestyle='-', linewidth=2)
    axs[2, 0].plot(data['t_s'], data['yaw_log'], label='Actual', color='red',
                   linestyle='-', linewidth=2)
    axs[2, 0].set_ylabel('Yaw (°)', fontsize=_label_fontsize)
    axs[2, 0].set_ylim(yaw_min, yaw_max)
    axs[2, 0].legend(fontsize=_legend_fontsize)
    axs[2, 0].grid(True, alpha=0.5)
    axs[2, 0].yaxis.set_major_formatter(formatter)
    axs[2, 0].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    axs[0, 1].plot(data['t_s'], data['tar_x'], label='Desired', color='#3D00F5',
                    linestyle='-', linewidth=2)
    axs[0, 1].plot(data['t_s'], data['odom_x'], label='Actual', color='red',
                    linestyle='-', linewidth=2)
    axs[0, 1].set_ylabel('Position X (m)', fontsize=_label_fontsize)
    axs[0, 1].set_ylim(x_min, x_max)
    axs[0, 1].legend(fontsize=_legend_fontsize)
    axs[0, 1].grid(True, alpha=0.5)
    axs[0, 1].yaxis.set_major_formatter(formatter)
    axs[0, 1].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    axs[1, 1].plot(data['t_s'], data['tar_y'], label='Desired', color='#3D00F5',
                   linestyle='-', linewidth=2)
    axs[1, 1].plot(data['t_s'], data['odom_y'], label='Actual', color='red',
                   linestyle='-', linewidth=2)
    axs[1, 1].set_ylabel('Position Y (m)', fontsize=_label_fontsize)
    axs[1, 1].set_ylim(y_min, y_max)
    axs[1, 1].legend(fontsize=_legend_fontsize)
    axs[1, 1].grid(True, alpha=0.5)
    axs[1, 1].yaxis.set_major_formatter(formatter)
    axs[1, 1].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    axs[2, 1].plot(data['t_s'], data['rf_alt_t'], label='Desired', color='#3D00F5',
                   linestyle='-', linewidth=2)
    axs[2, 1].plot(data['t_s'], data['rf_alt'], label='Actual', color='red',
                   linestyle='-', linewidth=2)
    axs[2, 1].set_ylabel('Position Z (m)', fontsize=_label_fontsize)
    axs[2, 1].set_ylim(z_min, z_max)
    axs[2, 1].legend(fontsize=_legend_fontsize)
    axs[2, 1].grid(True, alpha=0.5)
    axs[2, 1].yaxis.set_major_formatter(formatter)
    axs[2, 1].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # 设置共享的X轴标签
    for ax in axs[2, :]:  # 仅为最底部的子图设置X轴标签
        ax.set_xlabel('Time (s)', fontsize=_label_fontsize)

    plt.tight_layout()

    # 保存图像
    file_name = 'rpy_xyz.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_power_current_voltage(data, folder_path,
                               p_min, p_max, v_min, v_max, c_min, c_max):
    # 创建一个包含三行一列的图形，所有子图共享X轴
    fig, axs = plt.subplots(3, 1, figsize=(12, 9), sharex=True)  # sharex=True 共享X轴

    # 设置字体大小
    _label_fontsize = 25
    _title_fontsize = 25
    _legend_fontsize = 20
    _text_fontsize = 28  # 文本字体
    _axis_labelsize = 20  # 坐标轴字体

    avg_power = data['power'].mean()
    avg_current = data['current'].mean()
    avg_voltage = data['voltage'].mean()

    axs[0].plot(data['t_s'], data['power'], label='Power', color='red', linestyle='-', linewidth=2)
    axs[0].set_ylabel('Power (W)', fontsize=_label_fontsize)
    axs[0].set_ylim(p_min, p_max)
    axs[0].legend(fontsize=_legend_fontsize)
    axs[0].grid(True, alpha=0.5)
    axs[0].yaxis.set_major_formatter(formatter)  # 设置Y轴刻度格式
    axs[0].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # 在图中显示平均功率
    axs[0].text(0.08, 0.90, f'Average Power: {avg_power:.0f} W',
                transform=axs[0].transAxes, fontsize=_text_fontsize,
                va='top', ha='left')

    # Plot Current
    axs[1].plot(data['t_s'], data['current'], label='Current', color='red', linestyle='-', linewidth=2)
    axs[1].set_ylabel('Current (A)', fontsize=_label_fontsize)
    axs[1].set_ylim(c_min, c_max)
    axs[1].legend(fontsize=_legend_fontsize)
    axs[1].grid(True, alpha=0.5)
    axs[1].yaxis.set_major_formatter(formatter)
    axs[1].tick_params(axis='both', which='major', labelsize=_axis_labelsize)

    # axs[1].text(0.08, 0.90, f'Average Current: {avg_current:.2f} A',
    #             transform=axs[1].transAxes, fontsize=_text_fontsize,
    #             va='top', ha='left')

    # Plot Voltage
    axs[2].plot(data['t_s'], data['voltage'], label='Voltage', color='red', linestyle='-', linewidth=2)
    axs[2].set_ylabel('Voltage (V)', fontsize=_label_fontsize)
    axs[2].set_ylim(v_min, v_max)
    axs[2].legend(fontsize=_legend_fontsize)
    axs[2].grid(True, alpha=0.5)
    axs[2].yaxis.set_major_formatter(formatter)
    axs[2].tick_params(axis='both', which='major', labelsize=_axis_labelsize)
    # axs[2].text(0.08, 0.90, f'Average Voltage: {avg_voltage:.2f} V',
    #             transform=axs[2].transAxes, fontsize=_text_fontsize,
    #             va='top', ha='left')

    # 设置共享的X轴标签
    axs[2].set_xlabel('Time (s)', fontsize=_label_fontsize)
    axs[2].xaxis.set_major_formatter(formatter)
    plt.tight_layout()

    # 保存图像
    file_name = 'power_current_voltage.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_power(data, folder_path, p_min, p_max):
    # Plot Power
    avg_power = data['power'].mean()

    plt.figure(figsize=(12, 7))
    plt.plot(data['t_s'], data['power'], label='Power', color='red', linestyle='-', linewidth=2)
    plt.xlabel('Time (s)', fontsize=label_fontsize)
    plt.ylabel('Power (W)', fontsize=label_fontsize)
    plt.ylim(p_min, p_max)
    plt.legend(fontsize=legend_fontsize)
    plt.grid(True, alpha=0.5)

    if formatter is not None:
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.gca().xaxis.set_major_formatter(formatter)
    plt.tick_params(axis='both', which='both', labelsize=axis_fontsize)

    # 在图中显示平均功率
    plt.text(0.95, 0.90, f'Average Power: {avg_power:.0f} W',
             transform=plt.gca().transAxes, fontsize=text_size,
             va='top', ha='right', bbox=dict(facecolor='white', alpha=0.5))

    plt.tight_layout()
    file_name = 'power.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_power_temp(data, folder_path, p_min, p_max):
    # Plot Power
    avg_power = data['power'].mean()
    text_fontsize = 30

    plt.figure(figsize=(12, 7))
    plt.plot(data['t_s'], data['power'], label='Power', color='red', linestyle='-', linewidth=2)
    plt.xlabel('Time (s)', fontsize=label_fontsize)
    plt.ylabel('Power (W)', fontsize=label_fontsize)
    plt.ylim(p_min, p_max)
    plt.legend(fontsize=legend_fontsize)
    plt.grid(True, alpha=0.5)

    if formatter is not None:
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.gca().xaxis.set_major_formatter(formatter)
    plt.tick_params(axis='both', which='both', labelsize=axis_fontsize)

    # 添加标注函数
    def find_nearest_time(target_time):
        # 查找与 target_time 最接近的时间点
        idx_nearest = (data['t_s'] - target_time).abs().idxmin()
        return data.loc[idx_nearest]

    # 添加 77 秒处的标注
    closest_to_77 = find_nearest_time(41.0)
    plt.scatter(closest_to_77['t_s'], closest_to_77['power'], color='black', s=60)
    plt.annotate('Start of mode transition',
                 xy=(closest_to_77['t_s'], closest_to_77['power']),  # 箭头指向的点
                 xytext=(closest_to_77['t_s'] - 5, closest_to_77['power'] + 39),  # 文本的位置
                 fontsize=text_fontsize,
                 arrowprops=dict(facecolor='black', arrowstyle="->", linewidth=3),
                 ha='center')

    # 添加 92 秒处的标注
    closest_to_92 = find_nearest_time(50.0)
    plt.scatter(closest_to_92['t_s'], closest_to_92['power'], color='black', s=60)
    plt.annotate('Take off',
                 xy=(closest_to_92['t_s'], closest_to_92['power']),  # 箭头指向的点
                 xytext=(closest_to_92['t_s'] + 15, closest_to_92['power'] + 61),  # 文本的位置
                 fontsize=text_fontsize,
                 arrowprops=dict(facecolor='black', arrowstyle="->", linewidth=3),
                 ha='center')

    plt.tight_layout()
    file_name = 'power_temp.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_current(data, folder_path, c_min, c_max):
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['current'], label='Current', color='red', linestyle='-', linewidth=3)
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    plt.ylim(c_min, c_max)
    plt.legend()
    plt.grid(True, alpha=0.5)
    file_name = 'current.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_voltage(data, folder_path, v_min, v_max):
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['voltage'], label='voltage', color='red', linestyle='-', linewidth=3)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.ylim(v_min, v_max)
    plt.legend()
    plt.grid(True, alpha=0.5)
    file_name = 'voltage.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_throttle(data, folder_path):

    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['t_out'], label='Throttle', color='red', linestyle='-', linewidth=3)
    plt.xlabel('Time (s)')
    plt.ylabel('Throttle')
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True, alpha=0.5)

    file_name = 'throttle.png'
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def debug_x_position(data, folder_path):
    # Position_x 里程计x轴位置
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['tar_x'], label='tar_x', color='#3572EF',
             linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['odom_x'], label='odom_x', color='red',
             linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['pos_x_t'], label='pos_x_t', color='#FF9966',
             linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('X (m)')
    plt.legend()  # 显示图例
    plt.grid(True, alpha=0.5)  # 显示网格
    file_name = 'debug_pos_x.png'  # 定义图片的文件名
    plt.savefig(os.path.join(folder_path, file_name))


def debug_y_position(data, folder_path):
    # Position_y 里程计y轴位置
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['tar_y'], label='tar_y', color='#3572EF',
             linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['odom_y'], label='odom_y', color='red',
             linestyle='-', linewidth=2)
    plt.plot(data['t_s'], data['pos_y_t'], label='pos_y_t', color='#FF9966',
             linestyle='-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Y (m)')
    plt.legend()  # 显示图例
    plt.grid(True, alpha=0.5)  # 显示网格
    file_name = 'debug_pos_y.png'  # 定义图片的文件名
    plt.savefig(os.path.join(folder_path, file_name))


def plot_vib_vl(data, folder_path):
    #  机体震动强度, 单位 m/ss
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['vib_vl'], label='vib_vl', color='#3572EF',
             linestyle='-', linewidth=4)
    plt.xlabel('Time (s)')
    plt.ylabel('vib_vl (m/ss)')
    plt.legend()  # 显示图例
    plt.grid(True, alpha=0.5)  # 显示网格
    file_name = 'vib_vl.png'  # 定义图片的文件名
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_vib_ag(data, folder_path):
    #  机体震动角度, 单位 degree
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['vib_ag'], label='vib_ag', color='#3572EF',
             linestyle='-', linewidth=4)
    plt.xlabel('Time (s)')
    plt.ylabel('vib_ag (°)')
    plt.legend()  # 显示图例
    plt.grid(True, alpha=0.5)  # 显示网格
    file_name = 'vib_ag.png'  # 定义图片的文件名
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()


def plot_efz(data, folder_path):
    #  机体震动强度, 单位 m/ss
    plt.figure(figsize=(12, 6))
    plt.plot(data['t_s'], data['efz'], label='efz', color='#3572EF',
             linestyle='-', linewidth=4)
    plt.xlabel('Time (s)')
    plt.ylabel('efz (m/ss)')
    plt.legend()  # 显示图例
    plt.grid(True)  # 显示网格
    file_name = 'efz.png'  # 定义图片的文件名
    plt.savefig(os.path.join(folder_path, file_name))
    plt.close()
