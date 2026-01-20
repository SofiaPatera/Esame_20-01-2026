import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self._lista_nodi = []
        self._lista_archi = []

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        #print(f"Artisti: {self._artists_list}"

    def load_artists_with_min_albums(self, min_albums):
        min_albums = self._artists_list
        return min_albums

    def build_graph(self, n_alb):
        self._graph.clear()
        self._lista_nodi = DAO.get_all_node(n_alb)
        self._lista_archi = DAO.get_all_edges()
        self._graph.add_nodes_from(self._lista_nodi)
        for a1, a2, peso in self._lista_archi:
            self._graph.add_edge(a1, a2, weight=peso)

    def analisiComponente(self, a):
        if a is None:
            return None
        for c in nx.connected_components(self._graph):
            if a in c:
                dimensione = len(c)
                return dimensione
            else:
                return None

    def get_neighbors(self, team):
        vicini = []
        for n in self._graph.neighbors(team):
            w = self._graph[team][n]["weight"]
            vicini.append((n, w))
        return sorted(vicini, key=lambda x: x[1], reverse=True)

    def compute_best(self, start):
        self._best_path = []
        self._best_weight = 0
        self._ricorsione([start], 0, float('inf'))
        return self._best_weight, self._best_path

    def _ricorsione(self, path, weight):
        if weight > self._best_weight:
            self.best_weight = weight
            self.best_path = path.copy()

        vicini = self.get_neighbors(path)
        nei = []
