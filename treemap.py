import graphviz
from libxx import Filex
import math

dot = graphviz.Digraph(
    'ninja',
    comment='Sun',
    engine='dot',
    format='pdf'
)
dot.attr(
    ordering='out',
    k='2.2',
    overlap='prism0',
    rankdir='LR',
    size='1000,250'
)
# dot.attr('node', shape='doublecircle')
# dot.format = 'pdf'
# dot.engine = 'dot'
# dot.engine = 'neato'
def find_key(dictsx:list, address:str)->int:
    for i, item in enumerate(dictsx):
        if item["up"]==address:
            return i
    return -1

def bsc_relation_read(dot):
    a = Filex()
    addresses = a.openRelation()
    d_count = 0
    container = []
    for from_address in addresses:
        child = from_address[0]
        parent = from_address[1]

        y = find_key(container, parent)
        if y > -1:
            container[y]["children"]+=1
            container[y]["down"].append(child)
        else:
            # container[parent]["children"] = 0
            container.append({
                "up":parent,
                "children":0,
                "down":[],
            })
            
    container = sorted(container, key=lambda x: -x["children"])
    # print(container)
    """
    j=0
    for c in container:
        for dow in c["down"]:
            y = find_key(container, dow)
            if y < j:
                #push to top
        j+=1
    """
    for c in container:
        up = c["up"]
        for dow in c["down"]:
            dot.edge(up, dow)
    #for level in container:
    #dot.edge(parent, child)
    #print(f"The total edges is 0")
    return dot

dot = bsc_relation_read(dot)
dot.render(directory='data/charts').replace('\\', '/')
