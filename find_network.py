from core.blockscout import TokenHolder, TokenTransferScrap, ScanForSpecificTransactions
from core.ceresbinderV3 import dp_result_x, dp_result_eee6
from core.libxx import do_list_contract
from core.graph import MistAnalysis
from core.refnetwork import bnbscrape, OPReadHash


def extract_network():
    # example
    account = "0x50dcBF04Fd54545aB9E6199Ec7a2C824feB251b3"
    for n in range(100, 200):
        do_list_contract(account, n, dp_result_x)


def extract_staking():
    account = "0x8d8cbb435886ade1383b2d3bc4538d5892eeee6d"
    for n in range(0, 2):
        print(f"now it is up {n}")
        do_list_contract(account, n, dp_result_eee6)


def extract_v2():
    account = "0x50dcbf04fd54545ab9e6199ec7a2c824feb251b3"
    bsd = bnbscrape()
    bsd.check_contract(account).maxpages(208).scrapeV3()


def read_op_v2():
    excel = OPReadHash()
    excel.last = "0xad6598510a7cdec125dbccb2401a8952f978f721"
    excel.op_read()


def read_scout():
    ex = TokenHolder()
    ex.scan_all()


def read_scout_token():
    ex = TokenTransferScrap()
    ex.read("0xA39Ba3867d1933Da34aef6F762123C9AbD69f97A")


def read_blkscout_exp():
    ex = ScanForSpecificTransactions()
    ex.by_person_name("孙伯雄地址")


if __name__ == '__main__':
    read_blkscout_exp()
