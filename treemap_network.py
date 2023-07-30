from core.graph import graph_building_bsc_relations, MistAnalysis
from core.mistapi import MistAcquireDat


def classical_graph():
    title = "BSC.CeresBinderV3.Relation"
    graph_building_bsc_relations(title)


def mist_graph():
    mma = MistAcquireDat()
    mma.save("0x13f4ea83d0bd40e75c8222255bc855a974568dd4")

    ma = MistAnalysis()
    ma.setThreadHoldUSD(10).start()


if __name__ == '__main__':
    mist_graph()
