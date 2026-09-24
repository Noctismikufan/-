# -*- coding: utf-8 -*-
"""环境自检脚本 —— 确认 Python 学习环境是否可用。

用法：
    .venv\\Scripts\\python.exe check_env.py

会依次检查：Python 版本、核心库、中文字体、绘图后端。
全部通过会打印 OK，缺库会告诉你怎么装。
"""

import os
import platform
import sys

# Windows 控制台默认可能是 GBK，强制 UTF-8 避免中文乱码
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# (import 名, 显示名, 用途说明)
PACKAGES = [
    ("numpy", "numpy", "数值计算：数组、矩阵运算"),
    ("pandas", "pandas", "表格数据处理：DataFrame"),
    ("matplotlib", "matplotlib", "绘图与数据可视化"),
    ("scipy", "scipy", "科学计算：统计、优化、信号"),
    ("sklearn", "scikit-learn", "机器学习：分类、回归、聚类"),
    ("seaborn", "seaborn", "统计绘图美化"),
    ("openpyxl", "openpyxl", "读写 Excel 文件"),
    ("ipykernel", "ipykernel", "Jupyter 交互式编程内核"),
    ("IPython", "IPython", "增强交互式解释器"),
    ("tqdm", "tqdm", "循环进度条"),
    ("requests", "requests", "网络请求和数据获取"),
]

ok_count = 0
missing = []

print("=" * 60)
print("  Python 学习环境自检")
print("=" * 60)
print()

# ---------- 1. Python 本体 ----------
print("[1] Python 解释器")
print(f"    版本     : {platform.python_version()}")
print(f"    路径     : {sys.executable}")
print(f"    位数     : {platform.architecture()[0]}")
print(f"    虚拟环境 : {'是' if sys.prefix != sys.base_prefix else '否'}")

major, minor = sys.version_info[:2]
if (major, minor) == (3, 12):
    print("    结论     : OK 版本符合课程要求 (3.12)")
    ok_count += 1
elif (major, minor) >= (3, 10):
    print(f"    提示     : 当前 {major}.{minor}，课程推荐 3.12，一般也能跑")
    ok_count += 1
else:
    print("    警告     : 版本过旧，建议使用 Python 3.12")
print()

# ---------- 2. 依赖库 ----------
print("[2] 核心依赖库")
for mod_name, show_name, desc in PACKAGES:
    try:
        module = __import__(mod_name)
        version = getattr(module, "__version__", "已安装")
        print(f"    OK   {show_name:<14} {str(version):<12} {desc}")
        ok_count += 1
    except ImportError:
        print(f"    缺失 {show_name:<14} {'-':<12} {desc}")
        missing.append(show_name)
print()

# ---------- 3. 中文字体 ----------
print("[3] 中文字体支持")
cn_font = None
try:
    from matplotlib import font_manager

    prefer = ["Microsoft YaHei", "SimHei", "SimSun", "KaiTi", "DengXian"]
    available = {f.name for f in font_manager.fontManager.ttflist}
    found = [f for f in prefer if f in available]
    if found:
        cn_font = found[0]
        print(f"    OK   可用中文字体: {', '.join(found)}")
        print(f"    建议 绘图前加: plt.rcParams['font.sans-serif'] = ['{cn_font}']")
    else:
        print("    提示 未找到常见中文字体，图表中文可能显示为方块")
        print("         可改用英文标签，或安装字体后重试")
except Exception as exc:  # noqa: BLE001
    print(f"    跳过 {type(exc).__name__}: {exc}")
print()

# ---------- 4. 绘图功能 ----------
print("[4] 绘图功能")
try:
    import matplotlib

    matplotlib.use("Agg")  # 无窗口环境也能出图
    import matplotlib.pyplot as plt

    # 先应用中文字体，否则下面的中文标题会触发一堆缺字警告
    if cn_font:
        plt.rcParams["font.sans-serif"] = [cn_font]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(4, 2.5))
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16], marker="o")
    ax.set_title("中文测试 / Chinese Test")
    ax.set_xlabel("x 轴")
    ax.set_ylabel("y 轴")
    fig.tight_layout()
    fig.savefig("_env_check_plot.png", dpi=80)
    plt.close(fig)

    size = os.path.getsize("_env_check_plot.png")
    os.remove("_env_check_plot.png")
    print(f"    OK   成功生成测试图 ({size} 字节)，绘图功能正常")
    ok_count += 1
except Exception as exc:  # noqa: BLE001
    print(f"    失败 {type(exc).__name__}: {exc}")
    missing.append("matplotlib(绘图)")
print()

# ---------- 结论 ----------
print("=" * 60)
if missing:
    print(f"  结果：{ok_count} 项正常，以下需补装：")
    for name in sorted(set(missing)):
        print(f"        - {name}")
    print()
    print("  补装命令（在项目根目录执行）：")
    print("    .venv\\Scripts\\python.exe -m pip install " + " ".join(sorted(set(missing))))
else:
    print("  结果：全部检查通过，环境可以正常使用。")
print("=" * 60)
