class simple_graph:
    edgedict = None
    weightddict = None

    def __init__(self):
        edgedict = {}
        weightddict = {}

    def add_edge(self, src, dest, weight = 0, directed=False):
        self.edgedict[src] = dest
        self.weightddict[src] = {}
        self.weightddict[src][dest] = weight
        if directed is False:
            self.edgedict[dest] = src
            self.weightddict[dest][src] = weight

    def get_edgelist_string(self):
        arr = []
        for src in sorted(edgedict.keys()):
            dest = edgedict[src]
            arr.append("%s -> %s" % (src, dest)
        return arr

    def get_edgelist_weight_string(self):
        arr = []
        for src in sorted(edgedict.keys()):
            dest = edgedict[src]
            arr.append("%s --%s--> %s" % (src, weight[src][dest], dest)
        return arr

