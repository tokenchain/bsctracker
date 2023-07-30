#!/usr/bin/python
import json
import os
import re
from lxml import etree, html
import xml.etree.ElementTree as ET
import codecs
import requests
from .libxx import multiple_file_types, Filex

MIST_HEADER = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0'
}


class BaseIn:
    def __init__(self):
        self.workpath = "data/blockscout"

    def report_file_collect(self) -> list:
        os.chdir(self.workpath)
        file_head = "p"
        tmp = []
        for file in multiple_file_types("*.txt"):
            if file[:1] == file_head:
                tmp.append(file)

        parent_folder = os.path.join("../..")
        # parent_folder = os.path.join("/Users/hesdx/Documents/piplines/trongridtracker")
        os.chdir(parent_folder)
        return tmp

    def file_name_path(self) -> str:
        return ""

    def cl(self):
        file_object = open(self.file_name_path(), 'w')
        file_object.write("")
        file_object.close()


class TokenTransferScrap(BaseIn):
    def __int__(self):
        super().__init__()
        self.data = []
        self.work_address = ""

    def file_name_path(self):
        return os.path.join(self.workpath, f"profile_{self.work_address}.txt")

    def add_line(self, lk, usdt):
        content_line = f"{lk}----{usdt}\n"
        file_object = open(self.file_name_path(), 'a')
        file_object.write(content_line)
        file_object.close()

    def read(self, address: str):
        self.work_address = address
        self.cl()
        usdt = 0
        url = f"https://luckychain.pro/address/{address}/token-transfers?type=JSON"
        xpath_1 = "./div/div[2]/span[3]/span"  # lucky
        xpath_2 = "./div/div[2]/div/div/span[2]"  # usdt
        response = requests.get(url, headers=MIST_HEADER, verify=False)
        if response.status_code == 200:
            d = response.json()
            payload = d.get("items")
            for htmlx in payload:
                # text = htmlx.replace("&rarr;", "")
                document_root = html.fromstring(htmlx)
                processed_html = etree.tostring(document_root, encoding='unicode', pretty_print=True)
                # print(text)
                tr_lox = ET.fromstring(processed_html)
                lucky = tr_lox.find(xpath_1).text
                money = tr_lox.find(xpath_2).text
                print("-----")
                money = money.replace(",", "")
                money = money.replace("\n", "")
                lucky = lucky.replace("\n", "")
                lucky = lucky.replace(" ", "")
                usdt = usdt + float(money)
                # perc = tr.find(xpath_3).text
                # tr_list = tree_html.xpath(xpath_list)
                self.add_line(lucky, money)
            self.add_line("total usdt", usdt)
            print(f"total usdt {usdt}")
        else:
            return ""


class TokenHolder(BaseIn):
    def __init__(self):
        super().__init__()
        self.data = []

    def add_line(self, address, money):
        content_line = f"{address} {money}\n"
        file_object = open(self.file_name_path(), 'a')
        file_object.write(content_line)
        file_object.close()

    def file_name_path(self):
        return os.path.join(self.workpath, "analysis_usdt_holders.txt")

    def scan_all(self):
        xpath_1 = "./div/div/span[1]/a/span"
        xpath_2 = "./div/div/span[2]/span"
        # xpath_3 = "./div/div/span[2]"
        file_list = self.report_file_collect()
        file_list.sort(key=lambda f: int(re.sub('\D', '', f)))
        # file_list.sort(key=lambda f: int(filter(str.isdigit, f)))
        print(file_list)
        self.cl()
        for path in file_list:
            fp = os.path.join(self.workpath, path)
            if os.path.isfile(fp) is False:
                return {}
            with open(fp, newline='') as f:
                dat = json.loads(f.read())
                payload = dat.get("items")
                for htmlx in payload:
                    tr = ET.fromstring(htmlx)
                    address = tr.find(xpath_1).attrib['data-address-hash']
                    money = tr.find(xpath_2).text
                    # perc = tr.find(xpath_3).text
                    # tr_list = tree_html.xpath(xpath_list)
                    self.add_line(address, money)


class ScanForSpecificTransactions:
    def __init__(self):
        self.specific_amount = '100000000000000'
        self.url = "https://luckychain.pro/api"
        self.payload = {}
        self.headers = {}
        self.page_d = 1
        self.path_name = "data/blockscout"

    def by_person_name(self, file_name: str):
        path = self.fs_path_dp(file_name)
        addresses = Filex.loadList(path)
        for a in addresses:
            print(a)
            self.by_address(a)

    def have_result(self, tx: list):
        txns = len(tx)
        print(f"total transactions: {txns}")
        for h in tx:
            if h['value'] == self.specific_amount:
                _text = h['input']
                _text = _text.replace("0x", "")
                decode_content = bytes.fromhex(_text).decode('utf-8')
                print(self._account)
                print(decode_content)

    def fs_path(self):
        return os.path.join(self.path_name, f"tx{self._account[:10]}.json")

    def fs_path_dp(self, name: str):
        return os.path.join(self.path_name, f"{name}.txt")

    def by_address(self, acc: str) -> dict:

        self._account = acc
        if Filex.isFileFound(self.fs_path()) is True:
            a = Filex.getJson(self.fs_path())
            message_ed = a['message']
            code_p = int(a['status'])
            print(f"page: {self.page_d}, status {code_p}, message {message_ed}")
            if code_p == 1:
                res_list = a["result"]
                self.have_result(res_list)
            return True

        self.payload = {
            "module": "account",
            "action": "txlist",
            "address": self._account,
            # "page": self.page_d,
            # "offset": 0
        }
        print("----")
        print(self._account)

        try:
            response = requests.request(
                "GET",
                self.url,
                timeout=50,
                headers=self.headers,
                stream=True,
                params=self.payload,
                verify=False
            )
            response.raw.decode_content = True

            if response.status_code != 200:
                print("result is not 200")
                return False

            Filex.writeFile(response.text, self.fs_path())
            a = response.json()

            message_ed = a['message']
            code_p = int(a['status'])
            print(f"page: {self.page_d}, status {code_p}")

            if code_p == 1:
                res_list = a["result"]
                self.have_result(res_list)

            elif code_p == 0:
                print(response)
                print("ERRR")

            if "NOTOK" == message_ed:
                print(message_ed)

            elif "not found" in message_ed:
                print(message_ed)

            elif "no found" in message_ed:
                print(message_ed)

            return True
        except (
                requests.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout,
                ValueError,
                Exception
        ) as fy:
            return False
