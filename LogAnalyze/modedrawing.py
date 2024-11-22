"""
根据机器人不同运动模式，调用相应的绘图函数
"""
import dataPreprocessing
import plot_module


def plot_data_flight(data, folder_path):
    pitch_max = 10
    pitch_min = -10
    roll_max = 10
    roll_min = -10
    yaw_max = 10
    yaw_min = -10

    pitch_max_e = 10
    pitch_min_e = -10
    roll_max_e = 10
    roll_min_e = -10
    yaw_max_e = 10
    yaw_min_e = -10

    pos_x_scope = 2
    pos_y_scope = 2
    pos_z_max = 2
    pos_z_min = 1

    power_max = 500
    power_min = 300
    # power_min = 300
    current_max = 25
    current_min = 17
    voltage_max = 20
    voltage_min = 14

    # plot_module.plot_rpy(data, folder_path, pitch_min, pitch_max, roll_min, roll_max, yaw_min, yaw_max)
    # plot_module.plot_pitch(data, folder_path, pitch_min, pitch_max)
    # plot_module.plot_roll(data, folder_path, roll_min, roll_max)
    # plot_module.plot_yaw(data, folder_path, yaw_min, yaw_max)
    #
    # plot_module.plot_pitch_error(data, folder_path, pitch_min_e, pitch_max_e)
    # plot_module.plot_roll_error(data, folder_path, roll_min_e, roll_max_e)
    # plot_module.plot_yaw_error(data, folder_path, yaw_min_e, yaw_max_e)
    plot_module.plot_rpy_e(data, folder_path, pitch_min_e, pitch_max_e,
                           roll_min_e, roll_max_e, yaw_min_e, yaw_max_e)
    #
    # plot_module.plot_x_position(data, folder_path, -pos_x_scope, pos_x_scope)
    # plot_module.plot_y_position(data, folder_path, -pos_y_scope, pos_y_scope)
    # plot_module.plot_z_position(data, folder_path, pos_z_min, pos_z_max)

    # plot_module.plot_power(data, folder_path, power_min, power_max)
    # plot_module.plot_current(data, folder_path, current_min, current_max)
    # plot_module.plot_voltage(data, folder_path, voltage_min, voltage_max)
    # plot_module.plot_throttle(data, folder_path)

    plot_module.plot_rpy_xyz_pos(data, folder_path,
                                 pitch_min, pitch_max, roll_min, roll_max, yaw_min, yaw_max,
                                 -pos_x_scope, pos_x_scope, -pos_y_scope, pos_y_scope, pos_z_min, pos_z_max)

    # plot_module.plot_power_current_voltage(data, folder_path,
    #                                        power_min, power_max,
    #                                        voltage_min, voltage_max,
    #                                        current_min, current_max)


def plot_data_walk(data, folder_path):
    pitch_max = 30
    pitch_min = -30
    roll_max = 30
    roll_min = -30
    yaw_max = 180
    yaw_min = -180

    pitch_max_e = 10
    pitch_min_e = -10
    roll_max_e = 10
    roll_min_e = -10
    yaw_max_e = 10
    yaw_min_e = -10

    power_max = 400
    power_min = 0
    current_max = 25
    current_min = 17
    voltage_max = 20
    voltage_min = 14

    dataPreprocessing.set_target_values(data)

    plot_module.plot_rpy(data, folder_path, pitch_min, pitch_max, roll_min, roll_max, yaw_min, yaw_max)
    plot_module.plot_rpy_transition(data, folder_path,
                                    pitch_min, pitch_max,
                                    roll_min, roll_max,
                                    yaw_min, yaw_max)
    plot_module.plot_pitch(data, folder_path, pitch_min, pitch_max)
    plot_module.plot_roll(data, folder_path, roll_min, roll_max)
    plot_module.plot_yaw(data, folder_path, yaw_min, yaw_max)

    plot_module.plot_pitch_error(data, folder_path, pitch_min_e, pitch_max_e)
    plot_module.plot_roll_error(data, folder_path, roll_min_e, roll_max_e)
    plot_module.plot_yaw_error(data, folder_path, yaw_min_e, yaw_max_e)
    plot_module.plot_rpy_e(data, folder_path, pitch_min_e, pitch_max_e,
                           roll_min_e, roll_max_e, yaw_min_e, yaw_max_e)

    plot_module.plot_power(data, folder_path, power_min, power_max)
    plot_module.plot_current(data, folder_path, current_min, current_max)
    plot_module.plot_voltage(data, folder_path, voltage_min, voltage_max)
    plot_module.plot_throttle(data, folder_path)

    plot_module.plot_power_current_voltage(data, folder_path,
                                           power_min, power_max,
                                           voltage_min, voltage_max,
                                           current_min, current_max)


def plot_data_assisted_walk(data, folder_path):
    pitch_max = 30
    pitch_min = -30
    roll_max = 30
    roll_min = -30
    yaw_max = 180
    yaw_min = -180

    pitch_max_e = 10
    pitch_min_e = -10
    roll_max_e = 10
    roll_min_e = -10
    yaw_max_e = 10
    yaw_min_e = -10

    pos_x_scope = 2
    pos_y_scope = 2
    pos_z_max = 2
    pos_z_min = 0

    power_max = 400
    power_min = 300
    current_max = 25
    current_min = 17
    voltage_max = 20
    voltage_min = 14

    dataPreprocessing.set_target_values(data)


def my_debug(data, folder_path):
    pitch_max = 30
    pitch_min = -30
    roll_max = 30
    roll_min = -30
    yaw_max = 180
    yaw_min = -180

    pos_x_scope = 2
    pos_y_scope = 2
    pos_z_max = 2
    pos_z_min = 0

    power_max = 400
    power_min = 0
    current_max = 25
    current_min = 17
    voltage_max = 20
    voltage_min = 14

    # plot_module.debug_x_position(data, folder_path)
    # plot_module.debug_y_position(data, folder_path)
    # plot_module.plot_z_position(data, folder_path)
    # plot_module.plot_rpy(data, folder_path, pitch_min, pitch_max, roll_min, roll_max, yaw_min, yaw_max)
    # plot_module.plot_power_current_voltage(data, folder_path,
    #                                        power_min, power_max,
    #                                        voltage_min, voltage_max,
    #                                        current_min, current_max)
    # plot_module.plot_rpy_xyz_pos(data, folder_path,
    #                              pitch_min, pitch_max,
    #                              roll_min, roll_max,
    #                              yaw_min, yaw_max,
    #                              -pos_x_scope, pos_x_scope,
    #                              -pos_y_scope, pos_y_scope,
    #                              pos_z_min, pos_z_max)
    # plot_module.plot_vib_ag(data, folder_path)
    # plot_module.plot_vib_vl(data, folder_path)
    # plot_module.plot_efz(data, folder_path)
    plot_module.plot_power_temp(data, folder_path, power_min, power_max)
