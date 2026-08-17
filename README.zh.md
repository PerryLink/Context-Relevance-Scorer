<div align="center">

# Context-Relevance-Scorer

**面向 RAG 流程的相关性打分工具，使用 Cross-Encoder 模型对查询-文档对打分并过滤。**

*已移植到 [dsh-library](https://github.com/PerryLink/dsh-library) —— PerryLink DSH 插件家族的一员。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

`context-relevance-scorer` 使用 Cross-Encoder 模型（默认 `cross-encoder/ms-marco-MiniLM-L-6-v2`）对
查询-文档对打分，输出 0–1 的相关性分数。达到阈值的文档标记为"Accepted"（绿色），其余标记为
"Rejected"（红色），可用于过滤 RAG 流程中的低质量检索结果。

## 特性

- 🎯 Cross-Encoder 相关性打分（0–1）
- 🎨 终端颜色区分输出（红/绿）
- 📦 支持从 JSON 文件批量打分
- 💬 支持交互式模式

## 快速开始

```bash
pip install context-relevance-scorer
```

## 使用方法

```bash
# 对单个文档打分
context-relevance-scorer score -q "What is Python?" -d "Python is a programming language"

# 交互式模式
context-relevance-scorer score --interactive

# 自定义阈值（默认 0.5）
context-relevance-scorer score -q "query" -d "document" --threshold 0.7

# 使用其他模型
context-relevance-scorer score -q "query" -d "document" --model "cross-encoder/ms-marco-TinyBERT-L-6"
```

### 批量处理

创建 JSON 文件 `input.json`：

```json
{
  "query": "What is Python?",
  "documents": [
    "Python is a high-level programming language",
    "The weather is nice today",
    "Python is used for data science and machine learning"
  ]
}
```

然后运行：

```bash
context-relevance-scorer score --batch input.json --threshold 0.6
```

## 注意事项

- 首次运行需要下载模型（约 80 MB），需要网络连接。
- 如果访问 Hugging Face 受限，可配置镜像：

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

## 开发

```bash
pip install -e .
pytest tests/ -v
python -m context_relevance_scorer score --help
```

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
