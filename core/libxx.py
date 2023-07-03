import requests
import graphviz
import math
from typing import Union
import csv
import asyncio
import glob
import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Union
import signal
import threading
import requests
import itertools as it

file_format = 'data/reports/report_{}.txt'
file_analysis = 'data/analysis/analysis_{}.json'
api_key = "59IISNUG2CR3PIMAJF7MACQTS7DY6WFJDJ"
url = 'https://api.bscscan.com/api'
# url = 'https://luckychain.pro/api'
statement = 'End : {}, IO File {}'
address_blacklist = "https://raw.githubusercontent.com/scamsniffer/scam-database/main/blacklist/address.json"
statement_sum = '\nReport for address {}\nTotal outgoing USDT: {} / count: {}\nTotal incoming USDT: {} / count: {}\nNet {}'
help = """
Please note that the json file {FILENAME} gives the following explaination:
address:  the address transfered to
bal: the total amount to be transfered, positive is the collection address, negative is the upper level collection.
hit: the amount of transactions that is associated to this address
"""


def multiple_file_types(*patterns):
    return it.chain.from_iterable(glob.iglob(pattern) for pattern in patterns)


def find_trans_based_on_coin(user_address: str, contract_address: str) -> Union[dict, int]:
    payload = {
        "module": "account",
        "action": "tokentx",
        "address": user_address,
        "contract": contract_address,
        "apikey": api_key,
    }
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code == 200:
            # print(response.json())
            return response.json()
        else:
            print("error from this request not 200.")
        return 0
    except requests.exceptions.ReadTimeout:
        print(f"got timeout read error from the explorer - {contract_address}")
        return 0
    except ValueError as b:
        print(f"got error from the explorer value error - {contract_address}, {b}")
        return 0
    except Exception as e:
        print(f"got error from the explorer error exception - {contract_address}, {e}")
        return 0


requests.packages.urllib3.disable_warnings()


class WithTags:

    def __init__(self):
        self.tags = {}
        self.dex = {}
        self.black = []

    def tagPre(self):
        with open('tagged.json', newline='') as f:
            document = json.loads(f.read())
            self.tags = document["exchange"]
            self.black = document["blacklist"]
            self.dex = document["dex"]
            print("tagging is loaded.")

    def isDex(self, address: str) -> bool:
        try:
            name = self.dex[address]
            return True
        except KeyError:
            return False

    def isTagged(self, address: str) -> bool:
        try:
            name = self.tags[address]
            return True
        except KeyError:
            return False

    def tagging(self, address: str) -> str:
        if self.isTagged is True:
            return self.tags[address]
        return ""

    def tagdex(self, address: str) -> str:
        if self.isTagged is True:
            return self.dex[address]
        return ""


class Blockscout():
    def __init__(self):
        self.base = "https://luckychain.pro/api/"
        self.start = 0

    def checkAdd(self, addressHash: str):
        payload = {
            "module": "account",
            "action": "txlist",
            "address": addressHash
        }
        headers = {}
        try:
            response = requests.request("GET", self.base, headers=headers, data=payload, verify=False)
            print(response)
            print(response.text)
            return addressHash
        except requests.exceptions.ReadTimeout:
            print(f"got timeout read error from the explorer - {addressHash}")
            return addressHash
        except ValueError as b:
            print(f"got error from the explorer value error - {addressHash}, {b}")
            return addressHash
        except Exception as e:
            print(f"got error from the explorer error exception - {addressHash}, {e}")
            return addressHash


def find_trans(x_hash: str) -> int:
    payload = {
        "module": "transaction",
        "action": "getstatus",
        "txhash": x_hash,
        "apikey": api_key,
    }
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response)
        return x_hash
    except requests.exceptions.ReadTimeout:
        print(f"got timeout read error from the explorer - {x_hash}")
        return x_hash
    except ValueError as b:
        print(f"got error from the explorer value error - {x_hash}, {b}")
        return x_hash
    except Exception as e:
        print(f"got error from the explorer error exception - {x_hash}, {e}")
        return x_hash


def load_data(url: str) -> list:
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers)
        print(response)
        return response.json()
    except requests.exceptions.ReadTimeout:
        print(f"got timeout read error from the explorer - {url}")
        return []
    except ValueError as b:
        print(f"got error from the explorer value error - {url}, {b}")
        return []
    except Exception as e:
        print(f"got error from the explorer error exception - {url}, {e}")
        return []


def byValuei(amount: int) -> float:
    _b = 10 ** 18
    return amount / _b


def byValue(amount: str) -> float:
    _b = 10 ** 18
    return int(amount) / _b


def byValueStr(amount: str) -> str:
    _a = int(amount)
    _b = 10 ** 18
    _c = _a / _b

    return str(_c)


class Filex:
    def __init__(self):
        self.relation_file = ""
        self.report_file = ""
        self.intel_file = ""

    @staticmethod
    def writeFile(content, filename):
        fo = open(filename, "w")
        fo.write(content)
        fo.close()
        print(statement.format(time.ctime(), filename))

    def LoadBlackList(self) -> list:
        self.file_name_x = "data/blacklist.json"
        if os.path.isfile(self.file_name_x) is True:
            with open(self.file_name_x, newline='') as f:
                return json.load(f.read())
            return []
        else:
            return load_data(address_blacklist)

    def AppendLineLog(self, content: str):
        file_object = open(self.report_file, 'a')
        file_object.write(content)
        file_object.close()

    def AppendLineTransaction(self, content: str):
        file_object = open(self.report_file, 'a')
        file_object.write(content)
        file_object.close()

    def setup_staking_eeee6(self):
        self.relation_file = "data/report_fund_input.txt"
        print(self.report_file)

    def setup_ceresbinder_v3(self):
        self.relation_file = "data/report_network.txt"
        print(self.report_file)

    # relation related
    def openRelation(self) -> list:
        mlist = []
        self.setup_ceresbinder_v3()
        with open(self.relation_file, newline='') as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                address_p = line.split(" - ")
                mlist.append([f"0x{address_p[0]}", f"0x{address_p[1]}"])

        return mlist

    def AppendLineRelation(self, content: str):
        file_object = open(self.relation_file, 'a')
        file_object.write(content)
        file_object.close()


class CoinList(Filex):
    def __init__(self):
        super().__init__()
        self.data = {}
        self.dec = 18
        self.outgoing = 0
        self.incoming = 0
        self.records = 0
        self.outcount = 0
        self.incount = 0
        self.wallet_address = ""
        self.sym = ""

    def by_user(self, holder: str):
        self.wallet_address = holder
        self.report_file = file_format.format(holder)
        self.intel_file = file_analysis.format(holder)

    def findUsdtFor(self, user: str) -> "CoinList":
        self.dec = 18
        self.by_user(user)
        self.sym = "USDT"
        self.data = find_trans_based_on_coin(user, "0x55d398326f99059ff775485246999027b3197955")
        self.thenAnalysis()
        return self

    def findEthFor(self, user: str) -> "CoinList":
        self.dec = 18
        self.by_user(user)
        self.sym = "WETH"
        self.data = find_trans_based_on_coin(user, "0x2170Ed0880ac9A755fd29B2688956BD959F933F8")
        self.thenAnalysis()
        return self

    def findBNBFor(self, user: str) -> "CoinList":
        self.dec = 18
        self.by_user(user)
        self.sym = "WBNB"
        self.data = find_trans_based_on_coin(user, "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c")
        self.thenAnalysis()
        return self

    def findBUSDFor(self, user: str) -> "CoinList":
        self.dec = 18
        self.by_user(user)
        self.sym = "BUSD"
        self.data = find_trans_based_on_coin(user, "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56")
        self.thenAnalysis()
        return self

    def findUSDCFor(self, user: str) -> "CoinList":
        self.dec = 18
        self.by_user(user)
        self.sym = "USDC"
        self.data = find_trans_based_on_coin(user, "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d")
        self.thenAnalysis()
        return self

    def thenAnalysis(self) -> "CoinList":
        self._analysis(self.data)
        return self

    def _analysis(self, json: any) -> bool:
        if json == 0:
            return False
        if "result" not in json:
            return False

        list_da = json["result"]

        if len(list_da) == 0:
            return False

        for row in list_da:
            if "from" in row and row["from"] == self.wallet_address:
                self.outgoing = self.outgoing + int(row["value"])
                self.outcount = self.outcount + 1

            if "to" in row and row["to"] == self.wallet_address:
                self.incoming = self.incoming + int(row["value"])
                self.incount = self.incount + 1

            self.records = self.records + 1
            self.recordTransactionLine(row)

        self.EndLine()
        return True

    def recordTransactionLine(self, row):
        # readable = datetime.datetime.fromtimestamp(row["timeStamp"]).isoformat()
        ts = int(row["timeStamp"]) / 1000
        readable = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        data = [
            byValueStr(row["value"]),
            row["from"],
            row["to"],
            self.sym,
            row["blockHash"],
            readable,
            "\n"
        ]
        self.AppendLineTransaction(",".join(data))

    def EndLine(self):
        value_out = byValuei(self.outgoing)
        value_in = byValuei(self.incoming)
        net = self.incoming - self.outgoing
        net = byValuei(net)
        self.AppendLineTransaction(
            statement_sum.format(self.wallet_address, value_out, self.outcount, value_in, self.incount, net)
        )


class Analysis(WithTags):
    def __init__(self):
        super().__init__()
        self.hodlr = []
        self.booklegerlist = []
        self.bookleger = dict()
        self.logfile = ""
        self.outfile = ""
        self.line_scan = 0
        self._indent = 4
        self._encoding = "utf-8"
        self.tags = {}
        self.black = []
        self.tagPre()

    def handle_history(self):
        files = self.report_list()
        print(f"local anaylsis total files: {len(files)}")
        for f in files:
            self.start(f)

    def report_list(self) -> list:
        os.chdir("data/reports")
        file_head = "report"
        tmp = []
        for file in multiple_file_types("*.txt"):
            key_len = len(file_head)
            if file[:key_len] == file_head:
                test_ep = file[key_len:(len(file) - len(".txt"))]
                gidchan = str(test_ep).split("_")
                address = gidchan[1]
                tmp.append(address)

        parent_folder = os.path.join("../..")
        # parent_folder = os.path.join("/Users/hesdx/Documents/piplines/trongridtracker")
        os.chdir(parent_folder)
        return tmp

    def _predat(self, address: str):
        # print("Current directory:", os.getcwd())
        self.logfile = file_format.format(address)
        self.outfile = file_analysis.format(address)
        self.hodlr = []
        self.booklegerlist = []
        self.bookleger = dict()
        self.line_scan = 0

    def get_analysis(self, holder_address: str) -> dict:
        self._predat(holder_address)
        path = os.path.join(os.getcwd(), self.outfile)
        if os.path.isfile(path) is False:
            return {}
        with open(path, newline='') as f:
            analysis_open = json.loads(f.read())

        return analysis_open

    def check_valid_data(self, file: str) -> bool:

        fix_last_line = False
        file1 = open(file, 'r')
        _lines = file1.readlines()
        _sum = len(_lines)
        net_count = 0
        _end_line = 0
        ll = 0

        for line in _lines:
            ll += 1
            if "Net" in line and line[0] == "N" and _end_line == 0:
                net_count += 1
                _end_line = ll

                op = line.split(".")
                if len(op) > 0:
                    _lines[ll - 1] = f"{op[0]}.000"
                    fix_last_line = True

        if _sum > _end_line or fix_last_line:
            with open(file, "w") as f:
                new_content = "".join(_lines[:_end_line + 1])
                print("fixed content")
                f.write(new_content)

        return net_count == 1

    def start(self, holder_address: str):
        self._predat(holder_address)
        print(self.logfile)
        ok = self.check_valid_data(self.logfile)
        if ok is False:
            print(f"❌ File {self.logfile} is invalid! will need to remove contain now.")
            Filex.writeFile("", self.logfile)
            return

        file1 = open(self.logfile, 'r')
        _lines = file1.readlines()
        _sum = len(_lines)
        # Strips the newline character
        if _sum == 0:
            return
        # print(f"total lines -> {_sum}")
        net = 0
        t_out = 0
        t_in = 0
        print(f"start line - sum {_sum}")
        for line in _lines:
            self.line_scan += 1
            # print("Line{}: {} \n".format(self.line_scan, line.strip()), end="\r")
            if "Total outgoing" in line:
                a = "Total outgoing USDT: "
                b = line.replace(a, "").split("/")
                t_out = int(float(b[0].strip()))
                continue

            if "Total incoming" in line:
                a = "Total incoming USDT: "
                b = line.replace(a, "").split("/")
                t_in = int(float(b[0].strip()))
                continue

            if "Net" in line and line[0] == "N":
                net = int(float(line.replace("Net ", "")))
                continue

            if len(line) == 0:
                continue
            try:
                self.processLine(line)
            except IndexError:
                continue
        self.ender(net, t_out, t_in)

    def ender(self, net_balance, out, inflo):
        self.hodlr = []
        # self book ledger list book yes
        balance_temp = 0
        for k, v in self.bookleger.items():
            if k not in self.hodlr:
                self.hodlr.append(k)
                self.booklegerlist.append({
                    "address": k,
                    "bal": v["bal"],
                    "hit": v["hit"],
                    "mark": self.tagging(k)
                })
                balance_temp += v["bal"]

        self.booklegerlist = sorted(self.booklegerlist, key=lambda x: -x["bal"])

        with open(self.outfile, 'w') as f:
            json_str = json.dumps({
                "net_balance": balance_temp if net_balance == 0 else net_balance,
                "out": out,
                "in": inflo,
                "ranks": self.booklegerlist
            }, indent=self._indent)
            # data = jsonStr.encode(self._encoding)
            f.write(json_str)
            f.close()
        print(help.format(FILENAME=self.outfile))

    def processLine(self, line: str):
        p = line.strip().split(",")
        # from
        fromadd = p[1]
        # to
        toadd = p[2]
        # value
        val = p[0]
        # once that is done now..
        if fromadd not in self.hodlr:
            self.hodlr.append(fromadd)

        if toadd not in self.hodlr:
            self.hodlr.append(toadd)

        if fromadd not in self.bookleger:
            self.bookleger[fromadd] = {
                "bal": 0,
                "hit": 0
            }

        if toadd not in self.bookleger:
            self.bookleger[toadd] = {
                "bal": 0,
                "hit": 0
            }

        self.bookleger[fromadd]["bal"] -= float(val)
        self.bookleger[fromadd]["hit"] += 1
        self.bookleger[toadd]["bal"] += float(val)
        self.bookleger[toadd]["hit"] += 1


class BigQueue:
    workers = 0
    scan_task = {}
    queue_list = []
    address_scans_ceiling = 30000


class SubLayerAnalysis(WithTags):
    def __init__(self):
        super().__init__()
        self.booklegerlist = []
        self.jsonfile = ""
        self.holdself = ""
        self.coin = ""

    def start(self, address: str, coin="usdt"):
        self.coin = coin
        asyncio.run(self.corstart(address, 10000))

    async def corstart(self, holder_address: str, val_scope: int = 1000):
        self.holdself = holder_address
        self.jsonfile = file_analysis.format(holder_address)
        if os.path.exists(self.jsonfile) is False:
            return
        # if os.path.exists(self.jsonfile) is False:
        #    Path(self.jsonfile).touch()
        with open(self.jsonfile, newline='') as f:
            self.booklegerlist = json.loads(f.read())
            if "ranks" in self.booklegerlist:
                self.booklegerlist = self.booklegerlist["ranks"]
        if len(self.booklegerlist) == 0:
            return
        for ob in self.booklegerlist:
            target_address = ob["address"]
            if abs(ob["bal"]) < val_scope:
                continue
            if target_address == self.holdself:
                continue
            if self.isTagged(target_address) is True:
                continue
                # Start a background thread
            if BigQueue.workers < 10:
                # print(f"On task for scanning address {target_address}")
                x = threading.Thread(target=self.loop_run_coin_marlke, args=[target_address])
                BigQueue.scan_task[target_address] = x
                BigQueue.workers += 1
                x.start()
            else:
                if len(BigQueue.queue_list) < BigQueue.address_scans_ceiling:
                    print(f"Enqueue address {target_address}, total {len(BigQueue.queue_list)}", end="\n")
                    BigQueue.queue_list.append(target_address)

    def signal_handler(self, signum, frame):
        print(f"Signal {signum} received.")

    def loop_run_coin_marlke(self, address_t: str):
        base_coin = CoinList()

        if self.coin == "usdt":
            base_coin.findUsdtFor(address_t)
        if self.coin == "busd":
            base_coin.findBUSDFor(address_t)
        if self.coin == "usdc":
            base_coin.findUSDCFor(address_t)
        Analysis().start(address_t)
        SubLayerAnalysis().start(address_t, coin=self.coin)
        BigQueue.workers -= 1
        self.check_runner()

    def check_runner(self):
        if BigQueue.workers == 0 and len(BigQueue.queue_list) > 0:
            last_address = BigQueue.queue_list.pop()
            x = threading.Thread(target=self.read_coin_only, args=[last_address])
            BigQueue.scan_task[last_address] = x
            BigQueue.workers += 1

    def read_coin_only(self, address_t: str):

        base_coin = CoinList()
        if self.coin == "usdt":
            base_coin.findUsdtFor(address_t)
        if self.coin == "busd":
            base_coin.findBUSDFor(address_t)
        if self.coin == "usdc":
            base_coin.findUSDCFor(address_t)

        BigQueue.workers -= 1
        self.check_runner()

    def fillReport(self, coin="usdt"):
        self.coin = coin
        m = grab_reports()
        base_coin = CoinList()
        for a in m:
            if self.coin == "usdt":
                base_coin.findUsdtFor(a)
            if self.coin == "busd":
                base_coin.findBUSDFor(a)
            if self.coin == "usdc":
                base_coin.findUSDCFor(a)


"""
making some dp functions
"""


def grab_reports() -> list:
    os.chdir("data/reports")
    tmp = []
    for file in multiple_file_types("*.txt"):
        file1 = open(file, 'r')
        _lines = file1.readlines()
        _sum = len(_lines)
        checked = False
        for line in _lines:
            if "Net" in line and line[0] == "N":
                checked = True
                continue

        if checked is True:
            continue

        if os.path.getsize(file) > 0 or checked is False:
            Filex.writeFile("", file)

        address = file.replace(".txt", "").replace("report_", "")
        tmp.append(address)

    parent_folder = os.path.join("../..")
    os.chdir(parent_folder)

    return tmp


def do_list_contract(_account: str, page_d: int = 0, callback=None):
    payload = {
        "module": "account",
        "action": "txlist",
        "address": _account,
        "page": page_d,
        "offset": 0,
        "sort": "asc",
        "apikey": api_key,
    }
    headers = {}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        a = response.json()
        message_ed = a['message']
        code_p = int(a['status'])
        print(f"page: {page_d}, status {code_p}")

        if code_p == 1:
            res_list = a["result"]
            if callback is not None:
                callback(res_list)

        elif code_p == 0:
            print(response)
            print("ERRR")

        if "NOTOK" == message_ed:
            print(message_ed)

        elif "not found" in message_ed:
            print(message_ed)

        elif "no found" in message_ed:
            print(message_ed)

    except requests.exceptions.ReadTimeout:
        print(f"got timeout read error from the explorer -> {_account}")
        return _account
    except ValueError as b:
        print(f"got error from the explorer value error -> {_account}, {b}")
        return _account
    except Exception as e:
        print(f"got error from the explorer error exception -> {_account}, {e}")
        return _account


def find_key(dictsx: list, address: str) -> int:
    for i, item in enumerate(dictsx):
        if item["up"] == address:
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
            container[y]["children"] += 1
            container[y]["down"].append(child)
        else:
            # container[parent]["children"] = 0
            container.append({
                "up": parent,
                "children": 0,
                "down": [],
            })

    container = sorted(container, key=lambda x: -x["children"])

    for c in container:
        up = c["up"]
        for dow in c["down"]:
            dot.edge(up, dow)
    # for level in container:
    # dot.edge(parent, child)
    # print(f"The total edges is 0")
    return dot


def graph_building_bsc_relations(project_name: str):
    dot = graphviz.Digraph(
        project_name,
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
    dot = bsc_relation_read(dot)
    dot.render(directory='data/charts').replace('\\', '/')


def build_bot_tpl(name: str, iter: int):
    dot = graphviz.Digraph(
        f"{name}-{iter}",
        comment='Blockchain address tracking',
        engine='dot',
        format='pdf'
    )
    dot.attr(
        ordering='out',
        k='2.2',
        overlap='prism0',
        rankdir='LR',
        size='1000,25'
    )
    return dot


class Graph(WithTags):
    def __init__(self):
        super().__init__()
        self.tagPre()

    def graph_building_bsc_analysis_read(self, project_name, scope: int = 1000):
        a = Analysis()
        addresses = a.report_list()
        edges = 0
        file_count = 0
        sum_edges = 0
        dot = build_bot_tpl(project_name, file_count)
        for from_address in addresses:
            data = a.get_analysis(from_address)

            balance_net = 0
            if "balance" in data:
                balance_net = data["balance"]
            if "ranks" in data:
                ranks = data["ranks"]
                if len(ranks) > 0:
                    for m in ranks:
                        to_address = m["address"]
                        balance = m["bal"]
                        hit = m["hit"]
                        special = m["mark"]

                        if abs(balance) < scope:
                            continue

                        content_label = f"{hit} 笔, {abs(balance)}"
                        line_color = "black"

                        if balance > 0:

                            if self.isTagged(to_address):
                                # from_address = special + " user \n" + from_address
                                content_label += "\nTo " + special
                                line_color = "red"
                                dot.node(from_address, shape='box', fillcolor="firebrick1", style="filled")
                            elif self.isDex(to_address):
                                dot.node(from_address, shape='box', fillcolor="darkslategray2", style="filled",
                                         fontcolor="darkviolet")

                            a1 = from_address
                            a2 = to_address
                        else:

                            if self.isTagged(to_address):
                                content_label += "\nFrom " + special
                                line_color = "blue"
                                dot.node(to_address, shape='box', fillcolor="deepskyblue1", style="filled")
                            elif self.isDex(to_address):
                                dot.node(from_address, shape='box', fillcolor="darkslategray2", style="filled",
                                         fontcolor="darkviolet")

                            a1 = to_address
                            a2 = from_address

                        dot.edge(a1, a2, color=line_color, label=content_label)
                        edges += 1

            if edges > 3000:
                print("Over 3000 edges will now need to cut off for another chart")
                dot.render(directory='data/charts').replace('\\', '/')
                file_count += 1
                sum_edges += edges
                edges = 0
                dot = build_bot_tpl(name=project_name, iter=file_count)

            # if edges > 10:
            #    break
        if edges > 0:
            print("end game final chart.")

            # add a legend row
            """with dot.subgraph() as s:
                s.attr(rank='same')
                s.node('legend1', label='Legend 1')
                s.node('legend2', label='Legend 2')
                s.node('legend3', label='Legend 3')
                
            """

            dot.render(directory='data/charts').replace('\\', '/')
            sum_edges += edges

        print(f"The total edges is {sum_edges}")
