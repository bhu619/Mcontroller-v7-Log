# Mcontroller-v7 实验日志分析

项目链接：[bhu619/Mcontroller-v7-Log: Mcontroller-v7的日志分析](https://github.com/bhu619/Mcontroller-v7-Log)

## 说明
文件结构：

```plaintext
LogAnalyze/
│
├── config/                 # 配置模块，用于命令行参数解析
│
├── dataPreprocessing/      # 飞行日志数据读取、预处理、误差计算模块
│
├── main/                   # 主模块，程序的入口点
│
├── plot_module/            # 绘图模块，包含所有绘图相关的函数
│
├── modedrawing/            # 根据机器人不同运动模式，调用相应的绘图函数
│
└── test/                   # 测试模块，用于存储测试脚本
```

## 部署
git clone：

```bash
git clone https://github.com/bhu619/Mcontroller-v7-Log.git
```

进入虚拟环境：

```bash
.\venv\Scripts\activate
```

显示帮助信息：

```bash
python main.py -h
```

```bash
python main.py --help
```

帮助信息说明：

```bash
usage: main.py [-h] [--st float] [--et float] [--tMin float] [--tMax float] [--v float] [--c float]
               Path StartIndex EndIndex

处理日志文件并绘制数据

positional arguments:
  Path          基础路径 (D:\STM32CubeIDE\v7-log\log) 后的日志文件路径, 例如: 20241103
  StartIndex    日志文件的起始索引
  EndIndex      日志文件的结束索引

options:
  -h, --help    show this help message and exit
  --st float    日志分析的起始时间，单位: 秒, 默认为 0.0
  --et float    日志分析的结束时间，单位: 秒, 默认为 200.0
  --tMin float  油门范围的最小值 (0~100), 默认为 0.0
  --tMax float  油门范围的最大值 (0~100), 默认为 100.0
  --v float     电压系数, 默认为 1.115
  --c float     电流系数, 默认为 1.5
```

`positional arguments` 为必需参数，`options` 为可选参数。

退出虚拟环境：

```bash
deactivate
```

