<div align="center">

# Context-Relevance-Scorer

**A relevance scoring tool for RAG pipelines that uses a Cross-Encoder model to score and filter query–document pairs.**

*Ported into [dsh-library](https://github.com/PerryLink/dsh-library) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

`context-relevance-scorer` scores query–document pairs with a Cross-Encoder model
(`cross-encoder/ms-marco-MiniLM-L-6-v2` by default), producing a 0–1 relevance score. Documents at or
above a threshold are marked "Accepted" (green) and the rest "Rejected" (red), which helps filter
low-quality retrieval results in RAG pipelines.

## How it works

1. Concatenate the query and document and pass them to the model
2. The model outputs a relevance score between 0 and 1
3. Compare the score to the threshold to decide whether the document is relevant
4. Display the result with color coding

```
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┓
┃ Query              ┃ Document           ┃ Score ┃  Status   ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━┩
│ What is Python?    │ Python is a...     │ 0.892 │ ✓ Accepted│
│ What is Python?    │ Nice weather       │ 0.123 │ ✗ Rejected│
└────────────────────┴────────────────────┴───────┴───────────┘
```

## Features

- 🎯 Cross-Encoder relevance scoring (0–1)
- 🎨 Color-coded terminal output (red/green)
- 📦 Batch scoring from a JSON file
- 💬 Interactive mode

## Quick start

```bash
pip install context-relevance-scorer
```

## Usage

```bash
# Score a single document
context-relevance-scorer score -q "What is Python?" -d "Python is a programming language"

# Interactive mode
context-relevance-scorer score --interactive

# Custom threshold (default 0.5)
context-relevance-scorer score -q "query" -d "document" --threshold 0.7

# Use a different model
context-relevance-scorer score -q "query" -d "document" --model "cross-encoder/ms-marco-TinyBERT-L-6"
```

### Batch processing

Create a JSON file `input.json`:

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

Then run:

```bash
context-relevance-scorer score --batch input.json --threshold 0.6
```

## Notes

- The first run downloads the model (~80 MB); a network connection is required.
- If access to Hugging Face is restricted, set a mirror:

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

## Project structure

```
context-relevance-scorer/
├── src/context_relevance_scorer/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # python -m entry point
│   ├── cli.py               # CLI interface
│   ├── core.py              # Core scoring logic
│   └── utils.py             # Utility functions
├── tests/test_core.py       # Unit tests
├── pyproject.toml           # Project configuration
├── LICENSE                  # Apache 2.0
└── CONTRIBUTING.md
```

## Tech stack

- **Python** >= 3.8
- **sentence-transformers** — Cross-Encoder model support
- **transformers** — Hugging Face transformers library
- **torch** — PyTorch backend
- **rich** — terminal beautification
- **typer** — CLI framework

## Development

```bash
git clone https://github.com/PerryLink/context-relevance-scorer.git
cd context-relevance-scorer
pip install -e .

pytest tests/ -v
python -m context_relevance_scorer score --help
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Related

- [dsh-library](https://github.com/PerryLink/dsh-library) — the DSH plugin this project was ported into
- [PerryLink](https://github.com/PerryLink) — the PerryLink DSH Plugin Family

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
