import requests
import lxml.html
import logging
from lxml import etree

from core.libxx import Filex


class bnbscrape:
    def __init__(self):
        self.meta = []
        self.address = ""
        self.page = 1
        self.max_page = 1
        self.hn_file = "data/re_collect_ceretx.txt"

    def check_contract(self, ad: str):
        self.address = ad
        return self

    def maxpages(self, max: int):
        self.max_page = max
        return self

    def next(self):
        self.page += 1

    def ifnext(self):
        if self.page < self.max_page:
            self.next()
            print(f"now page at {self.page}")
            self.scrape_list_tx()
        else:
            print("Now page is reached to end")

    def _addlog_re(self, content: str):
        file_object = open(self.hn_file, 'a')
        file_object.write(content)
        file_object.close()

    def scrape_list_tx(self):
        headers = {
            "Cookie": "_ga=GA1.1.1492893560.1623527390; bscscan_cookieconsent=True; _ga_PQY6J2Q8EP=GS1.1.1688356204.75.1.1688360777.0.0.0; bitmedia_fid=eyJmaWQiOiI2NWZiMzE4NzgwYWU1MDExNmVkYmQ3YThiMThhNmFlZiIsImZpZG5vdWEiOiJhMjlmOGZiMzlmM2E3YzEzOTI2YjBkM2VmYTE2M2YzZiJ9; displaymode=dark; _ga_5Q0CRCD3YN=GS1.1.1686655032.4.1.1686655265.0.0.0; __stripe_mid=e4bd3b1a-f45b-4e2f-922e-569633b3210325b3fb; amp_fef1e8=1f438e32-2fa8-4d16-8a01-53f26d1c9870R...1h4d1t4ho.1h4d2005g.13.6.19; cf_clearance=GFwfgQtdJSP4VqwNnlo4XEjilgQxE6Cya6jlY8xiCK0-1688360366-0-150; ASP.NET_SessionId=hg4fvgyvjstjvhqqb44byc0z; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvXiBZ98zU5obi; __cf_bm=l5JR7kBg3TfY94fN0X18E7ewIGoODBFnp0f8TaNrxh0-1688360108-0-AY+9ZGmcQxj1/ARyU8IktkcMSR+wD6K6JD4q6tM/IE3MLNei+copt4VgzO0JbnljTg==; __stripe_sid=e3c6e54a-a5cb-4268-bd37-9add11c23e25685d14; __cuid=bf01ee9c807e40749169892e2a943909",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0"
        }
        base = "https://bscscan.com/txs"
        payload = {
            "a": self.address,
            "ps": 100,
            "p": self.page,
        }
        try:
            response = requests.request("GET", base, headers=headers, params=payload, stream=True, timeout=5)
        except (
                requests.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout,
        ) as e:
            print(e)
            self.scrape_list_tx()
            return

        # print(response.raw)
        response.raw.decode_content = True
        tree = lxml.html.parse(response.raw)
        xpath_list = "/html/body/div[1]/main/div[2]/div/div/div[3]/table/tbody/tr"
        cell = "td[2]/span/a"
        tr_list = tree.xpath(xpath_list)
        # print(tr_list)
        for tr in tr_list:
            a = tr.xpath(cell)[0]
            tx_hash = a.text
            print(tx_hash)
            self._addlog_re(tx_hash + "\n")
        self.ifnext()

    def scrape_tx(self, tx_hash: str):
        headers = {
            "Cookie": "_ga=GA1.1.1492893560.1623527390; bscscan_cookieconsent=True; _ga_PQY6J2Q8EP=GS1.1.1688356204.75.1.1688360777.0.0.0; bitmedia_fid=eyJmaWQiOiI2NWZiMzE4NzgwYWU1MDExNmVkYmQ3YThiMThhNmFlZiIsImZpZG5vdWEiOiJhMjlmOGZiMzlmM2E3YzEzOTI2YjBkM2VmYTE2M2YzZiJ9; displaymode=dark; _ga_5Q0CRCD3YN=GS1.1.1686655032.4.1.1686655265.0.0.0; __stripe_mid=e4bd3b1a-f45b-4e2f-922e-569633b3210325b3fb; amp_fef1e8=1f438e32-2fa8-4d16-8a01-53f26d1c9870R...1h4d1t4ho.1h4d2005g.13.6.19; cf_clearance=GFwfgQtdJSP4VqwNnlo4XEjilgQxE6Cya6jlY8xiCK0-1688360366-0-150; ASP.NET_SessionId=hg4fvgyvjstjvhqqb44byc0z; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvXiBZ98zU5obi; __cf_bm=l5JR7kBg3TfY94fN0X18E7ewIGoODBFnp0f8TaNrxh0-1688360108-0-AY+9ZGmcQxj1/ARyU8IktkcMSR+wD6K6JD4q6tM/IE3MLNei+copt4VgzO0JbnljTg==; __stripe_sid=e3c6e54a-a5cb-4268-bd37-9add11c23e25685d14; __cuid=bf01ee9c807e40749169892e2a943909",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0"
        }
        base = f"https://bscscan.com/tx/{tx_hash}"
        try:
            response = requests.request("GET", base, headers=headers, stream=True, timeout=15)
        except (
                requests.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout,
                requests.RequestException,
                requests.ReadTimeout,
                ConnectionResetError
        ) as e:
            print(e)
            self.scrape_tx()
            return

        # print(response.raw)
        response.raw.decode_content = True
        tree = lxml.html.parse(response.raw)
        xpath_list = '//*[@id="rawinput"]'
        doc_content = tree.xpath(xpath_list)
        return doc_content[0].text


url = 'https://api.bscscan.com/api'
api_key = "59IISNUG2CR3PIMAJF7MACQTS7DY6WFJDJ"
rpc_bsc = 'https://bsc-dataseed1.binance.org'


class OPReadHash(bnbscrape):
    def __init__(self):
        super().__init__()
        self.last = ""

    def _get_hash1(self, x_hash: str):
        payload = {
            "module": "transaction",
            "action": "getstatus",
            "txhash": x_hash,
            "apikey": api_key,
        }
        headers = {}
        try:
            response = requests.request("GET", url, headers=headers, params=payload)
            print(response)
        except (
                requests.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout,
        ) as e:
            print(e)
            return
        return response.json()

    def _get_hash2(self, x_hash: str):
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getTransactionByHash",
            "params": [x_hash],
            "id": 1,
        }
        print(payload)
        headers = {}
        try:
            response = requests.request("POST", rpc_bsc, headers=headers, data=payload)
            print(response)

        except (
                requests.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout,
        ) as e:
            print(e)
            return
        return response.json()

    def op_read(self):
        file_x = Filex()
        file_x.setup_ceresbinder_v3()
        with open(self.hn_file, newline='') as f:
            for line in f.readlines():
                hash = line.replace("\n", "")
                if self.last != "":
                    if self.last != hash:
                        continue

                    if self.last == hash:
                        self.last = ""

                print(hash)
                data = self.scrape_tx(hash)
                method = data[0:9]
                if "0x5fdbfd8" == method:
                    child = data[34:74]
                    parent = data[98:]
                    file_x.AppendLineRelation(f"{child} - {parent}\n")
                else:
                    print(f"skip -- {method}")

    def filter_add_relation(self, tx: dict, file_x_instance: Filex):
        for a in tx:
            data = a["input"]
            method = data[0:9]
            if "0x5fdbfd8" == method:
                child = data[34:74]
                parent = data[98:]
                file_x_instance.AppendLineRelation(f"{child} - {parent}\n")
            else:
                print(f"skip -- {method}")
