import networkx as nx

from features_infra.feature_calculators import NodeFeatureCalculator, FeatureMeta


class BetweennessCentralityCalculator(NodeFeatureCalculator):
    def __init__(self, *args, normalized=False, **kwargs):
        super(BetweennessCentralityCalculator, self).__init__(*args, **kwargs)
        self._is_normalized = normalized

    def _calculate(self, include: set):
        self._features = nx.betweenness_centrality(self._gnx, normalized=self._is_normalized)

    def is_relevant(self):
        return True


feature_entry = {
    "betweenness_centrality": FeatureMeta(BetweennessCentralityCalculator, {"betweenness"}),
}

if __name__ == "__main__":
    pass
