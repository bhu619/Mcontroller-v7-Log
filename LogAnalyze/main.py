import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import sys

import config
import dataPreprocessing
import modedrawing


def main():

    myconfig = config.parse_args()
    config.print_args(myconfig)

    for i in range(myconfig.start_index, myconfig.end_index + 1):  # 从 1 到 (x - 1)
        data_file = os.path.join(myconfig.full_path, 'Mlog', f'{i}.txt')
        folder_path = os.path.join(myconfig.full_path, 'Figure', f'{i}')

        # 确保文件夹存在
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        try:
            # 读取数据并预处理
            data = dataPreprocessing.read_data(data_file, myconfig.voltage_coefficient, myconfig.current_coefficient)

            # 过滤数据
            filtered_data = dataPreprocessing.filter_data(data, folder_path,
                                                          myconfig.throttle_min, myconfig.throttle_max,
                                                          myconfig.start_time, myconfig.end_time,
                                                          myconfig.voltage_coefficient, myconfig.current_coefficient)

            dataPreprocessing.calc_rmse_mae(filtered_data, folder_path)


            # print(filtered_data.describe())
            # modedrawing.plot_data_flight(filtered_data, folder_path)
            modedrawing.my_debug(filtered_data, folder_path)

        except Exception as e:
            print(f"Error processing file {data_file}: {e}")


if __name__ == "__main__":
    main()
