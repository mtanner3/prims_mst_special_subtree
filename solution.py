
class simple_graph:
    edgedict = None
    weightddict = None

    def __init__(self):
        self.edgedict = {}
        self.weightddict = {}

    def add_edge(self, src, dest, weight = 0):
        if src not in self.edgedict.keys():
            self.edgedict[src] = []
            self.weightddict[src] = {}
        self.edgedict[src].append(dest)
        self.weightddict[src][dest] = weight

        if dest not in self.edgedict.keys():
            self.edgedict[dest] = []
            self.weightddict[dest] = {}
        self.edgedict[dest].append(src)
        self.weightddict[dest][src] = weight

    def get_children(self, node):
        rv = set()
        for child in self.edgedict[node]:
            rv.add(child)
        return rv

    def get_nodelist(self):
        arr = set()
        for src in self.edgedict.keys():
            arr.add(src)
        return arr

    def get_weight(self, src, dest):
        try:
            return self.weightddict[src][dest]
        except:
            return None

def main():
    sg = simple_graph()

    nodecount, edgecount = raw_input().split()
    nodecount = int(nodecount)
    edgecount = int(edgecount)
    for idx in range(edgecount):
        ssrc, sdest, sweight = raw_input().split()
        sg.add_edge(int(ssrc), int(sdest), int(sweight))
    start_node = int(raw_input())

    #full_nodelist = sg.get_nodelist()
    done = False
    origins = [start_node]
    total_weight = 0

    #DEBUG = False
    while done is False:
        #if DEBUG: print "-" * 20
        #if DEBUG: print "origins: %s" % origins
        smallest_weight = None
        smallest_destination = None
        for src in origins:
            for dest in sg.get_children(src):
                weight = sg.get_weight(src, dest)
                #if DEBUG: print "%s -> %s... %s" % (src, dest, weight)
                if smallest_weight is None or weight < smallest_weight:
                    if dest not in origins:
                        smallest_weight = weight
                        smallest_destination = dest
            
        #if DEBUG: print "smallest weight was to dest %s" % smallest_destination
        total_weight += smallest_weight
        origins.append(smallest_destination)
        if len(origins) == nodecount:
            done = True
        
    print total_weight

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()', 'stats.dat')
#    main()

