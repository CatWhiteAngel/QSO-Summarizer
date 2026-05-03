# QSO-Summarizer

一个用于总结业余无线电 ADIF 日志的小型本地 CLI 工具。

它会读取 `.adi` 日志文件，解析 QSO 记录，计算基础统计信息，然后调用大语言模型生成一段自然语言总结。

## 功能

- 读取 ADIF / `.adi` 日志文件
- 解析 QSO 记录
- 统计通联数量、日期范围、频段、模式等信息
- 调用本地 LLM 生成操作日总结
- 在终端输出结果

## 数据流

```text
.adi 文件
  ↓
parser.py 解析
  ↓
stats.py 统计
  ↓
narrator.py 调用大语言模型
  ↓
终端输出总结
```

## 依赖

- Python 3.13+
- 本地或局域网中可访问的 Ollama 实例
- Ollama 中已安装目标模型（默认 qwen3:14b）

## 安装

本项目使用 [uv](https://github.com/astral-sh/uv) 管理依赖。

```bash
git clone https://github.com/CatWhiteAngel/qso-summarizer.git
cd qso-summarizer
uv sync
```

## 命令参数

```bash
uv run python -m src.main <adi文件路径> [选项]
```

| 参数 | 说明 | 默认值 |
|---|---|---|
| `path` | ADIF / `.adi` 文件路径 | 必填 |
| `-e`, `--endpoint` | LLM API 地址 | `http://localhost:11434/v1/chat/completions` |
| `-m`, `--model` | 使用的模型名称 | `qwen3:14b` |
| `-p`, `--promptfile` | prompt 文件路径 | `narrate.md` |

## 示例

使用默认模型：

```bash
uv run python -m src.main samples/example.adi
```

完整示例：

```bash
uv run python -m src.main samples/example.adi \
  -e http://localhost:11434/v1/chat/completions \
  -m qwen3:14b \
  -p narrate.md
```

## 示例输出

 ``` 
读取日志: samples/example.adi  
解析完成: 17 条 QSO  
调用 qwen3:14b 中...  
========= 日志总结 =========  
2024年3月5日至3月8日共完成17次通联，使用QQ0TST呼号进行操作。FT8和SSB为主要模式，20M与10M是主要频段，其中20M通联次数最多。3月5日为最活跃日期，当日完成5次通联。日志中包含17个不同对方呼号记录，所有记录均未标明网格、距离或DXCC信息。
 ``` 

## 状态

v0.1 - 基本功能可用。这是一个练手项目，并非生产级工具。

Licensed under the MIT License - see LICENSE for details.