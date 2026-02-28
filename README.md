# Context Relevance Scorer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A relevance scoring tool for RAG (Retrieval-Augmented Generation) systems using Cross-Encoder models to filter low-quality retrieval results.

RAG 检索结果相关性打分工具 - 使用 Cross-Encoder 模型对 Query-Document 对进行相关性打分，过滤低质量检索结果。

---

## Features | 核心特性

- 🎯 **Accurate Scoring** | **精准打分**: Uses Cross-Encoder model for relevance scoring (0-1 score)
- 🎨 **Visual Feedback** | **视觉化反馈**: Terminal color output - red for rejected, green for accepted
- ⚡ **Ready to Use** | **开箱即用**: CLI tool with minimal configuration
- 📦 **Batch Processing** | **批量处理**: Support for JSON file batch scoring
- 💬 **Interactive Mode** | **交互模式**: Interactive scoring support

---

## Quick Start | 快速开始

### Installation | 安装

```bash
pip install context-relevance-scorer
```

Or using Poetry | 或使用 Poetry:

```bash
poetry add context-relevance-scorer
```

### Basic Usage | 基本用法

**Single document scoring | 单个文档打分:**

```bash
context-relevance-scorer -q "What is Python?" -d "Python is a programming language"
```

**Interactive mode | 交互式模式:**

```bash
context-relevance-scorer --interactive
```

**Batch processing | 批量处理:**

Create a JSON file `input.json` | 创建 JSON 文件 `input.json`:

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

Run batch scoring | 运行批量打分:

```bash
context-relevance-scorer --batch input.json --threshold 0.6
```

**Custom threshold | 自定义阈值:**

```bash
context-relevance-scorer -q "query" -d "document" --threshold 0.7
```

**Use different model | 使用其他模型:**

```bash
context-relevance-scorer -q "query" -d "document" --model "cross-encoder/ms-marco-TinyBERT-L-6"
```

---

## How It Works | 工作原理

This tool uses the Cross-Encoder model (`cross-encoder/ms-marco-MiniLM-L-6-v2`) to score Query-Document pairs for relevance:

本工具使用 Cross-Encoder 模型对 Query-Document 对进行相关性打分：

1. Concatenate Query and Document and input to the model | 将 Query 和 Document 拼接后输入模型
2. Model outputs a relevance score between 0-1 | 模型输出 0-1 之间的相关性分数
3. Determine document relevance based on threshold | 根据阈值判断文档是否相关
4. Display results with color coding | 使用颜色编码显示结果

**Visual Output | 视觉效果:**

```
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
┃ Query              ┃ Document           ┃ Score ┃  Status   ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
│ What is Python?    │ Python is a...     │ 0.892 │ ✓ Accepted│
│ What is Python?    │ Nice weather       │ 0.123 │ ✗ Rejected│
└────────────────────┴────────────────────┴───────┴───────────┘
```

---

## Project Structure | 项目结构

```
context-relevance-scorer/
├── src/context_relevance_scorer/
│   ├── __init__.py          # Package initialization | 包初始化
│   ├── __main__.py          # CLI entry point | CLI 入口
│   ├── cli.py               # CLI interface | CLI 接口
│   ├── core.py              # Core scoring logic | 核心打分逻辑
│   └── utils.py             # Utility functions | 工具函数
├── tests/
│   └── test_core.py         # Unit tests | 单元测试
├── pyproject.toml           # Project configuration | 项目配置
├── README.md                # Project documentation | 项目文档
├── LICENSE                  # Apache 2.0 License | 许可证
└── CONTRIBUTING.md          # Contribution guidelines | 贡献指南
```

---

## Technology Stack | 技术栈

- **Python**: >= 3.8
- **sentence-transformers**: Cross-Encoder model support | Cross-Encoder 模型支持
- **transformers**: HuggingFace transformers library | HuggingFace 变换器库
- **torch**: PyTorch backend | PyTorch 后端
- **rich**: Terminal beautification | 终端美化
- **typer**: Modern CLI framework | 现代化 CLI 框架

---

## Development | 开发

```bash
# Clone repository | 克隆仓库
git clone https://github.com/PerryLink/context-relevance-scorer.git
cd context-relevance-scorer

# Install dependencies | 安装依赖
pip install -e .

# Run tests | 运行测试
pytest tests/ -v

# Run tool | 运行工具
python -m context_relevance_scorer --help
```

---

## Notes | 注意事项

1. **First run requires model download** | **首次运行需要下载模型** (约 80MB)
2. **Network connection required** | **需要网络连接** to access HuggingFace
3. **Configure mirror if needed** | **如果网络受限，可配置镜像**:
   ```bash
   export HF_ENDPOINT=https://hf-mirror.com
   ```

---

## License | 许可证

Apache License 2.0

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

See [LICENSE](LICENSE) file for details.

---

## Contributing | 贡献

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

---

## Contact | 联系方式

- GitHub: [@PerryLink](https://github.com/PerryLink)
- Email: novelnexusai@outlook.com

---

**Built with ❤️ by Chance Dean**
