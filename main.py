from libxx import CoinList, Analysis, SubLayerAnalysis


def local_analysis():
    Analysis().handle_history()


def fill_reports():
    SubLayerAnalysis().fillReport()


if __name__ == '__main__':
    address_loc = "0x81a53a49566e6efcd18f871d95d635cf92cdea1e"
    # CoinList().findUsdtFor(address_loc)
    # Analysis().start(address_loc)
    # SubLayerAnalysis().start(address=address_loc)
    fill_reports()
    local_analysis()
