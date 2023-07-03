from core.libxx import CoinList, Analysis, SubLayerAnalysis, Blockscout


def local_analysis():
    Analysis().handle_history()


def fill_reports(c):
    SubLayerAnalysis().fillReport(coin=c)


if __name__ == '__main__':
    # address_loc = "0x81a53a49566e6efcd18f871d95d635cf92cdea1e"
    # address_loc = "0x973c588b15d36080a219b9418c193ed5b1f254be"
    address_loc = "0x4f3126d5de26413abdcf6948943fb9d0847d9818"
    # CoinList().findBUSDFor(address_loc)
    # CoinList().findUsdtFor(address_loc)
    # Analysis().start(address_loc)
    # SubLayerAnalysis().start(address=address_loc, coin="busd")
    fill_reports("busd")
    local_analysis()
    # Blockscout().checkAdd(address_loc)
