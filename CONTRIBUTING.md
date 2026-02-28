# Contributing to Context Relevance Scorer

## Project Status | 项目状态

This is currently a personal project maintained by Chance Dean. While contributions are welcome, please note that this project is primarily developed and maintained by a single person.

本项目目前由 Chance Dean 个人维护。虽然欢迎贡献，但请注意这是一个主要由个人开发和维护的项目。

---

## How to Report Issues | 如何报告问题

If you encounter any bugs or have feature requests, please:

如果您遇到任何错误或有功能请求，请：

1. Check if the issue already exists in the [Issues](https://github.com/PerryLink/context-relevance-scorer/issues) section
2. If not, create a new issue with:
   - A clear and descriptive title
   - Steps to reproduce the problem
   - Expected behavior
   - Actual behavior
   - Your environment (OS, Python version, etc.)

---

## Development Setup | 开发环境搭建

### Prerequisites | 前置要求

- Python >= 3.8
- pip or Poetry

### Setup Steps | 搭建步骤

```bash
# Clone the repository | 克隆仓库
git clone https://github.com/PerryLink/context-relevance-scorer.git
cd context-relevance-scorer

# Install dependencies | 安装依赖
pip install -e .

# Or using Poetry | 或使用 Poetry
poetry install

# Run tests | 运行测试
pytest tests/ -v
```

---

## Code Standards | 代码规范

This project follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines.

本项目遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 代码风格指南。

### Key Points | 关键要点

- Use 4 spaces for indentation (not tabs)
- Maximum line length: 88 characters (Black formatter default)
- Use meaningful variable and function names
- Add docstrings for public functions and classes
- Write unit tests for new features

### Code Formatting | 代码格式化

We recommend using [Black](https://github.com/psf/black) for code formatting:

我们推荐使用 [Black](https://github.com/psf/black) 进行代码格式化：

```bash
pip install black
black src/ tests/
```

---

## Pull Request Process | 提交 Pull Request 流程

1. **Fork the repository** | **Fork 仓库**
   - Click the "Fork" button on GitHub

2. **Create a feature branch** | **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** | **进行修改**
   - Write clean, well-documented code
   - Add tests for new functionality
   - Ensure all tests pass

4. **Commit your changes** | **提交更改**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

5. **Push to your fork** | **推送到您的 Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** | **创建 Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear description of your changes

### PR Guidelines | PR 指南

- Keep PRs focused on a single feature or fix
- Include tests for new functionality
- Update documentation if needed
- Ensure all tests pass before submitting
- Be responsive to feedback and questions

---

## Questions? | 有问题？

If you have any questions about contributing, feel free to:

如果您对贡献有任何问题，请随时：

- Open an issue for discussion
- Contact the maintainer at novelnexusai@outlook.com

---

Thank you for your interest in contributing to Context Relevance Scorer!

感谢您对 Context Relevance Scorer 项目的贡献兴趣！
