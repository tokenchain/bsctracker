from core.ceresbinderV3 import dp_result_x, dp_result_eee6
from core.libxx import do_list_contract

from core.refnetwork import bnbscrape


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
    bsd.check_contract(account)
    bsd.scrapeV3()


if __name__ == '__main__':
    extract_v2()
