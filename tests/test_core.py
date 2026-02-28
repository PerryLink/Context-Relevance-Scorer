"""核心模块测试"""
import pytest
from context_relevance_scorer.core import RelevanceScorer


def test_score_single_high_relevance():
    """测试高相关性文档"""
    scorer = RelevanceScorer(threshold=0.5)
    score = scorer.score_single(
        "What is Python?",
        "Python is a high-level programming language"
    )
    assert score > 0.7


def test_score_single_low_relevance():
    """测试低相关性文档"""
    scorer = RelevanceScorer(threshold=0.5)
    score = scorer.score_single(
        "What is Python?",
        "The weather is nice today"
    )
    assert score < 0.3


def test_score_batch():
    """测试批量打分"""
    scorer = RelevanceScorer(threshold=0.5)
    documents = [
        "Python is a programming language",
        "The weather is nice",
        "Python is used for data science"
    ]
    results = scorer.score_batch("What is Python?", documents)

    assert len(results) == 3
    assert results[0][2] is True  # 第一个文档应该通过
    assert results[1][2] is False  # 第二个文档应该不通过
    assert results[2][2] is True  # 第三个文档应该通过


def test_filter_documents():
    """测试文档过滤"""
    scorer = RelevanceScorer(threshold=0.5)
    documents = [
        "Python is a programming language",
        "The weather is nice",
        "Python is used for data science"
    ]
    filtered = scorer.filter_documents("What is Python?", documents)

    assert len(filtered) == 2
    assert "The weather is nice" not in filtered
