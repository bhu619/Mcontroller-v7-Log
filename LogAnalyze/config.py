"""
命令行参数解析
"""
import argparse
import os
import sys


class AnalysisConfig:
    base_path = r'D:\STM32CubeIDE\v7-log\log'  # 类变量

    def __init__(self, path, start_index, end_index, start_time, end_time, throttle_min, throttle_max, voltage_coefficient, current_coefficient):
        self.full_path = os.path.join(AnalysisConfig.base_path, path)
        self.start_index = start_index
        self.end_index = end_index
        self.start_time = start_time
        self.end_time = end_time
        self.throttle_min = throttle_min
        self.throttle_max = throttle_max
        self.voltage_coefficient = voltage_coefficient
        self.current_coefficient = current_coefficient


# 设置命令行参数解析
def parse_args():

    # argparse 模块创建一个命令行解析器
    parser = argparse.ArgumentParser(description="处理日志文件并绘制数据")
    parser.add_argument("Path", type=str,
                        help="基础路径 (D:\\STM32CubeIDE\\v7-log\\log) 后的日志文件路径, 例如: 20241103")
    parser.add_argument("StartIndex", type=int, help="日志文件的起始索引")
    parser.add_argument("EndIndex", type=int, help="日志文件的结束索引")
    parser.add_argument("--st", type=float, metavar='float', default=0.0, help="日志分析的起始时间，单位: 秒, 默认为 0.0")
    parser.add_argument("--et", type=float, metavar='float', default=200.0, help="日志分析的结束时间，单位: 秒, 默认为 200.0")
    parser.add_argument("--tMin", type=float, metavar='float', default=0.0, help="油门范围的最小值 (0~100), 默认为 0.0")
    parser.add_argument("--tMax", type=float, metavar='float', default=100.0, help="油门范围的最大值 (0~100), 默认为 100.0")
    parser.add_argument("--v", type=float, metavar='float', default=1.115, help="电压系数, 默认为 1.115")
    parser.add_argument("--c", type=float, metavar='float', default=1.5, help="电流系数, 默认为 1.5")
    args = parser.parse_args()

    # 检查时间和油门范围的合法性
    if args.st > args.et:
        print("错误: 起始时间不应大于结束时间")
        sys.exit(1)
    if not (0 <= args.tMin <= 100 and 0 <= args.tMax <= 100):
        print("错误: 油门范围应在0到100之间")
        sys.exit(1)
    if args.tMin > args.tMax:
        print("错误: 油门最小值不应大于最大值")
        sys.exit(1)
    if args.st < 0:
        print("错误: 起始时间不能小于0")
        sys.exit(1)

    config = AnalysisConfig(args.Path, args.StartIndex, args.EndIndex, args.st, args.et,
                            args.tMin, args.tMax, args.v, args.c)

    return config


def print_args(config):

    # 输出完整路径进行验证
    print('\n')
    print(f"完整路径: {config.full_path}")
    print(f"日志分析范围: {config.start_index} ~ {config.end_index}")
    print(f"过滤日志文件时间范围: {config.start_time} ~ {config.end_time}")
    print(f"过滤日志文件油门范围: {config.throttle_min} ~ {config.throttle_max}")
    print(f"电压系数: {config.voltage_coefficient}")
    print(f"电流系数: {config.current_coefficient}")
    print('\n')
