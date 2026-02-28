"""CLI 接口"""
import json
from typing import Optional
import typer
from .core import RelevanceScorer
from .utils import display_result, display_batch_results, show_progress, handle_error, console

app = typer.Typer(help="RAG 检索结果相关性打分工具")


@app.command()
def score(
    query: Optional[str] = typer.Option(None, "--query", "-q", help="查询文本"),
    document: Optional[str] = typer.Option(None, "--document", "-d", help="文档文本"),
    threshold: float = typer.Option(0.5, "--threshold", "-t", help="相关性阈值 (0-1)"),
    model_name: str = typer.Option(
        "cross-encoder/ms-marco-MiniLM-L-6-v2",
        "--model",
        "-m",
        help="模型名称"
    ),
    batch: Optional[str] = typer.Option(None, "--batch", "-b", help="批量处理 JSON 文件路径"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="交互式模式"),
):
    """对 Query-Document 对进行相关性打分"""

    try:
        scorer = RelevanceScorer(model_name=model_name, threshold=threshold)

        # 批量处理模式
        if batch:
            with open(batch, 'r', encoding='utf-8') as f:
                data = json.load(f)

            query_text = data.get('query', '')
            documents = data.get('documents', [])

            if not query_text or not documents:
                console.print("[red]JSON 文件必须包含 'query' 和 'documents' 字段[/red]")
                raise typer.Exit(1)

            progress = show_progress("正在加载模型并打分...")
            results = scorer.score_batch(query_text, documents)
            progress.stop()

            display_batch_results(results, query_text)
            return

        # 交互式模式
        if interactive:
            console.print("[bold cyan]交互式相关性打分工具[/bold cyan]")
            console.print("输入 'quit' 或 'exit' 退出\n")

            while True:
                query_text = console.input("[bold]Query:[/bold] ").strip()
                if query_text.lower() in ['quit', 'exit']:
                    break

                console.print("[dim]Document (输入完成后按 Enter):[/dim]")
                doc_text = console.input().strip()

                if not query_text or not doc_text:
                    console.print("[yellow]Query 和 Document 不能为空[/yellow]\n")
                    continue

                progress = show_progress("正在打分...")
                score_value = scorer.score_single(query_text, doc_text)
                progress.stop()

                display_result(query_text, doc_text, score_value, threshold)
                console.print()

            return

        # 单个文档打分模式
        if query and document:
            progress = show_progress("正在加载模型并打分...")
            score_value = scorer.score_single(query, document)
            progress.stop()

            display_result(query, document, score_value, threshold)
            return

        # 参数不足
        console.print("[red]请提供 --query 和 --document,或使用 --interactive 或 --batch 模式[/red]")
        console.print("使用 --help 查看帮助")
        raise typer.Exit(1)

    except Exception as e:
        handle_error(e)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
