"""核心打分模块"""
from typing import List, Tuple, Optional
from sentence_transformers import CrossEncoder


class RelevanceScorer:
    """相关性打分器"""

    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2", threshold: float = 0.5):
        self.model_name = model_name
        self.threshold = threshold
        self._model: Optional[CrossEncoder] = None

    def load_model(self):
        """懒加载模型"""
        if self._model is None:
            self._model = CrossEncoder(self.model_name)

    def score_single(self, query: str, document: str) -> float:
        """对单个文档打分"""
        self.load_model()
        score = self._model.predict([(query, document)])[0]
        return float(score)

    def score_batch(self, query: str, documents: List[str]) -> List[Tuple[str, float, bool]]:
        """批量打分,返回 (文档, 分数, 是否通过) 列表"""
        self.load_model()
        pairs = [(query, doc) for doc in documents]
        scores = self._model.predict(pairs)
        return [(doc, float(score), score >= self.threshold)
                for doc, score in zip(documents, scores)]

    def filter_documents(self, query: str, documents: List[str]) -> List[str]:
        """过滤文档,只返回通过阈值的文档"""
        results = self.score_batch(query, documents)
        return [doc for doc, _, passed in results if passed]
