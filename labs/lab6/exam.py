import gzip
from string import ascii_lowercase as lowercase
import networkx as nx
from itertools import permutations

DATA4 = 'words4_dat.txt.gz'
DATA5 = 'words_dat.txt.gz'


def generate_graph(words, order):
    totaledge = {}
    G = nx.Graph(name="words")
    lookup = dict((c, lowercase.index(c)) for c in lowercase)

    def edit_distance_one(word):
        if order is True:
            for i in range(len(word)):
                left, c, right = word[0:i], word[i], word[i + 1:]
                j = lookup[c]  # lowercase.index(c)
                for cc in lowercase[j + 1:]:
                    yield left + cc + right
        if order is False:
            for i in range(len(word)):
                left, c, right = word[0:i], word[i], word[i + 1:]
                for cc in lowercase:
                    withorder = left + cc + right
                    for perm in permutations(withorder):
                        yield ''.join(perm)

    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word) if cand in words)
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
        if word in totaledge:
            totaledge[word]+=1
        else:
            totaledge[word]=1
    return G, totaledge


def words_graph(length, path, order):
    """Return the words example graph from the Stanford GraphBase"""
    fh = gzip.open(path, 'r')
    words = set()
    for line in fh.readlines():
        line = line.decode()
        if line.startswith('*'):
            continue
        w = str(line[0:length])
        words.add(w)
    return generate_graph(words, order)


if __name__ == '__main__':
    G5, tot = words_graph(5, DATA5, True)
    # G4 = words_graph(4, DATA4, True)
    # GP = words_graph(5, DATA5, False)

    for word, val in tot.items():
        if val > 20:
            print(word, val)

    # print("Loaded words_dat.txt containing 5757 five-letter English words.")
    # print("Two words are connected if they differ in one letter.")
    # print("Graph has %d nodes with %d edges"
    #       % (nx.number_of_nodes(G5), nx.number_of_edges(G5)))
    # print("%d connected components" % nx.number_connected_components(G5))


    # print('5 letter pairs:')
    # maxKey = ''
    # maxVal = 0
    # for (source_, target_) in [('party', 'party')]:
    #     print("Shortest path between %s and %s is" % (source_, target_))
        
    #     try:
    #         sp = nx.shortest_path(G5, source=source_)
    #         for key, value in sp.items():
    #             print(key, len(value))
    #             if len(value)>maxVal:
    #                 maxVal = len(value)
    #                 maxKey = key

    #     except nx.NetworkXNoPath:
    #         print("None")
    # print('........',maxKey, maxVal)
        

    # print('5 letter pairs:')
    # for (source, target) in [('party', 'amigo')]:
    #     print("Shortest path between %s and %s is" % (source, target))
    #     try:
    #         sp = nx.shortest_path(G5, source, target)
    #         for n in sp:
    #             print(n)
    #     except nx.NetworkXNoPath:
    #         print("None")





    # print('5 letter pairs:')
    # for (source, target) in [('chaos', 'order'),
    #                          ('nodes', 'graph'),
    #                          ('moron', 'smart'),
    #                          ('pound', 'marks')]:
    #     print("Shortest path between %s and %s is" % (source, target))
    #     try:
    #         sp = nx.shortest_path(G5, source, target)
    #         for n in sp:
    #             print(n)
    #     except nx.NetworkXNoPath:
    #         print("None")

    # print('\n4 letter pairs:')
    # for (source, target) in [('cold', 'warm'),
    #                          ('love', 'hate')]:
    #     print("Shortest path between %s and %s is" % (source, target))
    #     try:
    #         sp = nx.shortest_path(G4, source, target)
    #         for n in sp:
    #             print(n)
    #     except nx.NetworkXNoPath:
    #         print("None")

    # print('\nfive letter pairs using the unordered implementation')
    # for (source, target) in [('chaos', 'order'),
    #                          ('nodes', 'graph'),
    #                          ('moron', 'smart'),
    #                          ('pound', 'marks')]:
    #     print("Shortest path between %s and %s is" % (source, target))
    #     try:
    #         sp = nx.shortest_path(GP, source, target)
    #         for n in sp:
    #             print(n)
    #     except nx.NetworkXNoPath:
    #         print("None")