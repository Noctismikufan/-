# Python 学习环境搭建

> 本文档记录本项目 Python 学习环境的组成、日常用法与常见问题排查。
> 环境一旦装好就长期有效，日常只需看「日常使用」一节。

---

## 一、环境概览

| 项目 | 内容 |
|------|------|
| Python 版本 | 3.12.10 |
| 解释器路径 | `C:\Users\杨竣堡\AppData\Local\Programs\Python\Python312\python.exe` |
| 虚拟环境 | 项目根目录 `.venv/`（独立隔离，不影响系统） |
| 包管理器 | pip 26.x（已配置清华镜像加速） |
| 编辑器 | VS Code 1.136 + Python / Jupyter 扩展 |
| 交互式编程 | JupyterLab |

### 为什么要用虚拟环境？

虚拟环境（`.venv`）是**项目专属的 Python 仓库**。不同项目对库的版本要求常常冲突，用虚拟环境可以：

- 每个项目用自己的库版本，互不干扰
- 不污染系统 Python，删掉 `.venv` 文件夹就等于彻底卸载
- 换电脑时凭 `requirements.txt` 一条命令重建

**记住一个原则：本项目所有 Python 操作，都走 `.venv`。**

---

## 二、日常使用

### 1. 命令行运行脚本

```bash
# 方式一：直接用虚拟环境里的 python（推荐，无需激活）
.venv/Scripts/python.exe 脚本名.py

# 方式二：先激活环境，之后可以直接用 python
source .venv/Scripts/activate      # Git Bash
.venv\Scripts\activate             # CMD / PowerShell
python 脚本名.py
deactivate                          # 退出环境
```

### 2. VS Code 里写代码

直接用 VS Code 打开项目根目录 `人工智能通识课程`，配置已自动生效：

- 解释器已指定为 `.venv`
- 打开 `.py` 文件按 `F5` 或点击右上角 ▷ 即可运行
- 打开 `.ipynb` Notebook 可直接逐格运行

### 3. 启动 JupyterLab

```bash
.venv/Scripts/python.exe -m jupyter lab
```

浏览器会自动打开 `http://localhost:8888`。

### 4. 环境自检

任何时候怀疑环境有问题，先跑：

```bash
.venv/Scripts/python.exe check_env.py
```

它会逐项检查版本、核心库、绘图和中文字体，并给出缺失项的补装命令。

### 5. 安装新库

```bash
.venv/Scripts/python.exe -m pip install 库名
```

装完记得同步到依赖清单：

```bash
.venv/Scripts/python.exe -m pip freeze > requirements.txt
```

---

## 三、已安装的库

| 库 | 版本 | 用途 |
|----|------|------|
| `numpy` | 2.5.3 | 数值计算：多维数组、矩阵运算、广播机制 |
| `pandas` | **2.3.3** | 表格数据处理：DataFrame、清洗、分组统计 |
| `matplotlib` | 3.11.2 | 绘图与数据可视化 |
| `seaborn` | 0.13.2 | 基于 matplotlib 的统计图表美化 |
| `scipy` | 1.18.1 | 科学计算：统计检验、优化、信号处理 |
| `scikit-learn` | 1.9.1 | 机器学习：分类、回归、聚类、降维 |
| `openpyxl` | 3.1.5 | 读写 Excel 文件 |
| `jupyterlab` | 4.6.4 | 交互式 Notebook 编程 |
| `ipykernel` | 7.3.0 | Jupyter 运行内核 |
| `ipywidgets` | 8.1.9 | Notebook 交互控件 |
| `tqdm` | 4.70.1 | 循环进度条 |
| `requests` | 2.34.2 | 网络请求（获取在线数据集） |

完整版本锁定在项目根目录 `requirements.txt`。

> ⚠️ **pandas 必须留在 2.x，不要升到 3.x。** 原因见下方 Q6。

安装思路是按课程推进顺序配齐：**先数值计算，再数据分析，再到机器学习**，一次装好避免上课时临时缺库。

---

## 四、常见问题

### Q1：图表里的中文显示成方块 □□□

matplotlib 默认字体不含中文。在每个画图脚本开头加上**固定两行**：

```python
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False  # 负号显示异常也一并解决
```

### Q2：脚本输出中文乱码

Windows 控制台默认编码常为 GBK。在脚本开头加：

```python
import sys
if hasattr(sys, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
```

VS Code 中若仍乱码，检查右下角编码是否为 `UTF-8`。

### Q3：`ModuleNotFoundError: No module named 'xxx'`

八成是用错了 Python。检查两点：

1. `sys.executable` 是否指向项目里的 `.venv`（跑 `check_env.py` 第 1 节会显示）
2. VS Code 右下角解释器是否为 `.venv`

确认无误后再装库：

```bash
.venv/Scripts/python.exe -m pip install 缺失的库名
```

### Q4：pip 安装卡住 / 超时

环境已配置清华镜像。若是全局 pip（非 `.venv`）需要加速，可临时指定：

```bash
pip install 库名 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q5：提示「无法加载文件 ... 因为在此系统上禁止运行脚本」

PowerShell 执行策略限制所致。改用 Git Bash 或 CMD 执行，或临时放开：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Q6：`ImportError: DLL load failed while importing lib: 应用程序控制策略已阻止此文件。（WinError 4551）`

**这是本机真实踩过的坑，务必看这里。**

症状：装什么都"成功"，但 `import pandas` 直接报 WinError 4551；而 numpy、scipy、matplotlib 都能正常导入。

原因：Windows 11 的**智能应用控制（Smart App Control, SAC）**在起作用。它会在系统层拦截"没有可信数字签名 / 微软信誉库里查不到"的二进制文件。pandas 3.x 属于较新的发行版，其编译扩展 `lib.cp312-win_amd64.pyd` 未能通过信誉校验，于是被系统拦下。

排查方法（判断是不是这个问题）：

```bash
# 单独加载那个 pyd，看错误码
.venv/Scripts/python.exe -c "import ctypes; ctypes.CDLL(r'.venv/Lib/site-packages/pandas/_libs/lib.cp312-win_amd64.pyd')"
# 报 [WinError 4551] 即命中
```

解决办法：**降级 pandas 到 2.x**

```bash
.venv/Scripts/python.exe -m pip install "pandas<3"
```

本项目已验证 `pandas==2.3.3` 可正常导入和使用，功能对课程完全够用。

其他要点：

- 智能应用控制**没有针对单个程序的放行白名单**，不要试图"只允许这一个文件"。
- **不要为了装某个库去关掉智能应用控制** —— 关掉之后无法再开启，除非重装 Windows，代价太大。
- 遇到类似报错的库，优先尝试**换一个更成熟的旧版本**，这通常比动系统设置划算得多。
- 想确认拦截记录，可看事件查看器：`应用程序和服务日志 → Microsoft → Windows → CodeIntegrity → Operational`，事件 3077 会记录拦截详情。

### Q7：`.venv` 可以删除吗？

可以。它只是本地环境，已被 `.gitignore` 忽略、不入库。删掉后按下面步骤重建即可。

---

## 五、环境重建步骤

换电脑或环境损坏时，在项目根目录依次执行：

```bash
# 1. 创建虚拟环境
"C:/Users/杨竣堡/AppData/Local/Programs/Python/Python312/python.exe" -m venv .venv

# 2. 配置国内镜像
.venv/Scripts/python.exe -m pip config set --site global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 3. 安装依赖（版本已锁定，含 pandas 2.x 限制）
.venv/Scripts/python.exe -m pip install -r requirements.txt

# 4. 注册 Jupyter 内核
.venv/Scripts/python.exe -m ipykernel install --user --name python312-venv --display-name "Python 3.12 (.venv)"

# 5. 自检
.venv/Scripts/python.exe check_env.py
```

第 5 步输出「全部检查通过」即完成。

---

## 六、目录约定

| 位置 | 存放内容 |
|------|----------|
| `notebooks/` | 交互式 Notebook（按序号命名，如 `00-`、`01-`） |
| `assignments/` | 课堂作业与实验报告 |
| `projects/` | 综合项目与课程设计 |
| `notes/` | 知识点整理与学习资料 |
| `data/` | 数据集 |
| `check_env.py` | 环境自检脚本 |
| `requirements.txt` | 依赖清单（版本锁定） |

---

*最后更新：2026-09-24*
