"""工具函数模块"""
from typing import List, Tuple
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

console = Console()


def display_result(query: str, document: str, score: float, threshold: float):
    """显示单个结果"""
    passed = score >= threshold
    color = "green" if passed else "red"
    status = "✓ Accepted" if passed else "✗ Rejected"

    table = Table(show_header=True, header_style="bold")
    table.add_column("Query", style="cyan")
    table.add_column("Document", style="yellow")
    table.add_column("Score", justify="right")
    table.add_column("Status", justify="center")

    # 截断长文本
    query_display = query[:50] + "..." if len(query) > 50 else query
    doc_display = document[:50] + "..." if len(document) > 50 else document

    table.add_row(
        query_display,
        doc_display,
        f"[{color}]{score:.3f}[/{color}]",
        f"[{color}]{status}[/{color}]"
    )

    console.print(table)


def display_batch_results(results: List[Tuple[str, float, bool]], query: str):
    """显示批量结果"""
    table = Table(show_header=True, header_style="bold")
    table.add_column("#", justify="right", style="dim")
    table.add_column("Document", style="yellow")
    table.add_column("Score", justify="right")
    table.add_column("Status", justify="center")

    for idx, (doc, score, passed) in enumerate(results, 1):
        color = "green" if passed else "red"
        status = "✓ Accepted" if passed else "✗ Rejected"
        doc_display = doc[:60] + "..." if len(doc) > 60 else doc

        table.add_row(
            str(idx),
            doc_display,
            f"[{color}]{score:.3f}[/{color}]",
            f"[{color}]{status}[/{color}]"
        )

    console.print(f"\n[bold cyan]Query:[/bold cyan] {query}\n")
    console.print(table)

    # 统计信息
    accepted = sum(1 for _, _, passed in results if passed)
    console.print(f"\n[bold]Summary:[/bold] {accepted}/{len(results)} documents accepted")


def show_progress(message: str) -> Progress:
    """显示进度条"""
    progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    )
    progress.start()
    progress.add_task(description=message, total=None)
    return progress


def handle_error(error: Exception):
    """显示友好的错误提示"""
    console.print(Panel(
        f"[red bold]Error:[/red bold] {str(error)}",
        title="❌ Error",
        border_style="red"
    ))
