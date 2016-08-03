class simple_graph:
    edgedict = None
    weightddict = None
    rev_edgedict = None
    rev_weightddict = None
    directed = False

    def __init__(self):
        self.edgedict = {}
        self.weightddict = {}
        self.rev_edgedict = {}
        self.rev_weightddict = {}

    def add_edge(self, src, dest, weight = 0, directed=False):

        self.directed = directed

        if src not in self.edgedict.keys():
            self.edgedict[src] = []
        self.edgedict[src].append(dest)
        if src not in self.weightddict.keys():
            self.weightddict[src] = {}
        self.weightddict[src][dest] = weight

        if self.directed is False:
            if dest not in self.rev_edgedict.keys():
                self.rev_edgedict[dest] = []
            self.rev_edgedict[dest].append(src)
            if dest not in self.rev_weightddict.keys():
                self.rev_weightddict[dest] = {}
            self.rev_weightddict[dest][src] = weight

    def get_children(self, node):
        rv = []
        if node in self.edgedict.keys():
            for child in self.edgedict[node]:
                rv.append(child)
        if self.directed is False:
            if node in self.rev_edgedict.keys():
                for child in self.rev_edgedict[node]:
                    rv.append(child)
        return rv

    def get_edgelist_string(self):
        arr = []
        for src in self.edgedict.keys():
            for dest in self.edgedict[src]:
                arr.append("%s -> %s" % (src, dest))
        for src in self.rev_edgedict.keys():
            for dest in self.rev_edgedict[src]:
                arr.append("%s -> %s" % (src, dest))
        arr.sort()
        return "\n".join(arr)

    def get_original_edgelist_string(self):
        arr = []
        for src in sorted(self.edgedict.keys()):
            for dest in self.edgedict[src]:
                arr.append("%s -> %s" % (src, dest))
        return "\n".join(arr)

    def get_original_edgelist_weight_string(self):
        arr = []
        for src in sorted(self.edgedict.keys()):
            for dest in self.edgedict[src]:
                arr.append("%s --%s--> %s" % (src, self.weightddict[src][dest], dest))
        return "\n".join(arr)

    def get_nodelist_string(self):
        arr = self.get_nodelist()
        arr = map(str,arr)
        return "\n".join(arr)

    def get_nodelist(self):
        arr = []
        for src in sorted(self.edgedict.keys()):
            arr.append(src)
        return arr

    def get_weight(self, src, dest):
        if src in self.weightddict.keys():
            if dest in self.weightddict[src].keys():
                return self.weightddict[src][dest]
        if src in self.rev_weightddict.keys():
            if dest in self.rev_weightddict[src].keys():
                return self.rev_weightddict[src][dest]
        return None

if __name__ == "__main__":
    sg = simple_graph()

    sg.add_edge(1,2,3)
    sg.add_edge(1,3,4)
    sg.add_edge(4,2,6)
    sg.add_edge(5,2,2)
    sg.add_edge(2,3,5)
    sg.add_edge(3,5,7)

    print "graph:"
    print sg.get_edgelist_string()

    print "children of 1:"
    print sg.get_children(1)

    print "children of 2:"
    print sg.get_children(2)

    print "nodelist:"
    print sg.get_nodelist_string()

    print "nodelist:"
    print sg.get_nodelist()
