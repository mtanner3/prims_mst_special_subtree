
import sys

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
        sg.add_edge(ssrc, sdest, int(sweight))
    start_node = raw_input().strip()

    total_weight = 0

    origins = [start_node]
    weights = {}
    destination = {}
    for dest in sg.get_children(start_node):
        w = sg.get_weight(start_node, dest)
        weights[dest] = w
        destination[w] = dest

    DEBUG = True
    while True:
        if DEBUG: print "=" * 20
        if DEBUG: print "starting loop with weights:", weights
        if DEBUG: print "starting loop with destinations:", destination
        smallest_weight = sorted(destination.keys())[0]
        smallest_dest = destination[smallest_weight]
        total_weight += smallest_weight
        origins.append(smallest_dest)
        if len(origins) == nodecount:
            break
        del weights[smallest_dest]
        del destination[smallest_weight]
        for d in weights.keys():
            w = weights[d]
            if w in destination.keys() and w < destination[w]:
                destination[w] = d
        if DEBUG: print "removed smallest destination %s (%s)." % (smallest_dest, smallest_weight)
        if DEBUG: print "origins is now %s. Left with:" % origins
        if DEBUG: print "weights:", weights
        #if DEBUG: print "destinations:", destination
        if DEBUG: print "assimilating new destinations"
        for dest in sg.get_children(smallest_dest):
            w = sg.get_weight(smallest_dest, dest)
            if DEBUG: print "looking at %s --%d--> %s" % (smallest_dest, w, dest)
            if dest in origins:
                if DEBUG: print "  already in origins"
                continue
            if dest not in weights.keys():
                if DEBUG: print "  new node. adding"
                weights[dest] = w
                destination[w] = dest
            else:
                if DEBUG: print "  existing node. checking for smallest"
                if w < weights[dest]:
                    weights[dest] = w
                    destination[w] = dest
        if DEBUG: print "ending loop with weights:", weights
        #if DEBUG: print "ending loop with destinations:", destination
        
    print total_weight

if __name__ == "__main__":
    import cProfile
    cProfile.run('main()', 'stats.dat')
#    main()

