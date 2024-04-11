import graphviz

# pip install graphviz if package not found

"""
In case no rights for `pip install graphviz` : 
python -m venv graph_visu_env
source graph_visu_env/bin/activate
pip install graphviz
deactivate (when finished)
"""


class DBG:
    def __init__(self, k, sequence=""):
        ''' defines and stores initial values'''

        self.k = k
        self.graph = dict()
        if sequence:
            self.add_sequence(sequence)

    def visualize(self):
        """ Open graph visualization with graphviz representation. """
        g = graphviz.Digraph(comment='DeBruijn graph')
        for node in iter(self.graph.keys()):
            g.node(node, node)
        for pref, suffs in iter(self.graph.items()):
            for suffix in suffs:
                g.edge(pref, suffix)
        g.render(filename='debruijn_graph', format='pdf', view=True)

    def add_sequence(self, sequence):
        """ Add a sequence to the De Bruijn graph."""
        for i in range(len(sequence) - self.k + 1):
            kmer = sequence[i:i + self.k]
            if kmer not in self.graph:
                self.graph[kmer] = set()
            for prev_kmer in self.graph.keys():
                if prev_kmer[1:] == kmer[0:- 1]:
                    self.graph[prev_kmer].add(kmer)

    def right_neighbours(self, node):
        """ Return the right neighbours of a node in the De Bruijn graph."""
        return self.graph.get(node, set())

    def left_neighbours(self, node):
        """ Return the left neighbours of a node in the De Bruijn graph."""
        left_neighbours = set()
        for kmer in self.graph.keys():
            if node in self.graph[kmer]:
                left_neighbours.add(kmer)
        return left_neighbours

    def right_extensions(self, node):
        """ Return the right extensions of a node in the De Bruijn graph."""
        r_kmer = self.right_neighbours(node)
        if len(r_kmer) == 1:
            elem = list(r_kmer)[0]
            if len(self.left_neighbours(elem)) == 1:
                return node + self.right_extensions(elem)[self.k - 1:]
        return node


    def detect_tips(self):
        """Detect tips in the De Bruijn graph."""
        tips = []
        for node in self.graph.keys():
            unitig = self.right_extensions(node)
            print(unitig)
            #print(unitig[-self.k:])
            print(unitig[0:self.k])
            if len(self.right_neighbours(unitig[-self.k])) + len(self.left_neighbours(unitig[0:self.k])) < 2:  # No outgoing edges
                tips.append(unitig)
        return tips


if __name__ == "__main__":
    dbg = DBG(5)

    dbg.add_sequence("AACCGTAT")
    dbg.add_sequence("ACCGTGTA")
    dbg.add_sequence("CCGTATAG")
    dbg.add_sequence("CCGTGTCG")
    dbg.add_sequence("GTGTAGCG")
    dbg.add_sequence("TATAGCGT")

    print(dbg.right_extensions("AACCG"))

    print(dbg.detect_tips())

    #dbg.visualize()
