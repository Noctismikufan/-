# 大数据与人工智能 课程仓库

> 本仓库用于记录与整理「大数据与人工智能」课程的学习内容、作业与实践项目。

## 📁 目录结构

| 目录 | 用途 |
|------|------|
| `notes/` | 课程笔记与知识点整理 |
| `notebooks/` | 交互式 Notebook（按序号命名） |
| `assignments/` | 课堂作业与实验报告 |
| `projects/` | 综合项目与课程设计 |
| `data/` | 课程使用/练习的数据集 |
| `references/` | 参考资料与延伸阅读 |

## 🚀 快速开始

本项目使用 **Python 3.12** 作为主要开发语言，配合 Jupyter / VS Code 进行数据科学与机器学习实践。

### 环境状态

环境已搭建完成，开箱即用。虚拟环境位于项目根目录 `.venv/`（已被 git 忽略，不入库）。

```bash
# 运行脚本
.venv/Scripts/python.exe 脚本名.py

# 环境自检
.venv/Scripts/python.exe check_env.py

# 启动 JupyterLab
.venv/Scripts/python.exe -m jupyter lab
```

VS Code 打开本项目后会自动使用 `.venv` 解释器，直接按 `F5` 运行即可。

**已安装**：numpy 2.5.3、pandas 2.3.3、matplotlib 3.11.2、seaborn 0.13.2、scipy 1.18.1、scikit-learn 1.9.1、openpyxl、jupyterlab 4.6.4、ipykernel、tqdm、requests

> ⚠️ **pandas 请保持在 2.x，不要升级到 3.x。** 本机 Windows 11 的「智能应用控制」会拦截 pandas 3.x 的编译扩展，报 `WinError 4551`。排查过程见 [`notes/Python环境搭建.md`](notes/Python环境搭建.md) 的 Q6。

> 完整搭建说明、常见问题排查、环境重建步骤见 [`notes/Python环境搭建.md`](notes/Python环境搭建.md)。

### 环境要求
- Python 3.12+
- Git
- VS Code（建议安装 Python、Jupyter 扩展）

## 📝 学习进度

- [ ] 课程笔记持续更新中

---

*Created by Noctismikufan · 大数据与人工智能课程*
