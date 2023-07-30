# _*_ coding: utf-8 _*_
# @Date:  5:56 下午
# @File: demo.py
# @Author: liyf
import os

import requests
from .libxx import Filex

MIST_HEADER = {
    'Cookie': '_ga_40VGDGQFCB=GS1.1.1688955014.39.1.1688955071.0.0.0; _ga=GA1.1.466492303.1686797482; _bl_uid=hRl3jipawCFjCvodh31n6Cb6Im1k; csrftoken=8a9hO9Zf55puFbZOUs4SAVUrWPgjG0AJ0IcUnERnEhBQBsc2e2cGqxg4heP0Ls7h; _ga_SGF4VCWFZY=GS1.1.1686921655.2.0.1686921656.0.0.0; amp_fef1e8=3ed210e7-9c3e-422a-bf11-5e3191b61433R...1h2ufuqn4.1h2ug37b1.o.1.p; __cuid=66672f75694e40809757e2a3b4dfd68d; sessionid=jfkp0qotbrx5erj5qiwsv5rjlsiohxic',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0'
}


def get_mist_overview(address: str):
    print(f"get side note from {address}")
    url = f'https://dashboard.misttrack.io/api/v1/address_overview?coin=USDT-BEP20&address={address}'
    response = requests.get(url, headers=MIST_HEADER)
    if response.status_code == 200:
        j = response.json()
        if "success" in j and j["success"] is False:
            print(j)
            return ""
        else:
            text = f'\nBalance: {j["balance"]}'
            text += f'\ntx_count: {j["tx_count"]}'
            text += f'\nfirst_tx_time: {j["first_tx_time"]}'
            text += f'\nlast_tx_time: {j["last_tx_time"]}'
            text += f'\ntotal received: {j["total_received"]}'
            text += f'\ntotal spent: {j["total_spent"]}'
            text += f'\nreceived count: {j["received_count"]}'
            text += f'\nspent_count: {j["spent_count"]}'
            return text
    else:
        return ""


def get_mist_graph_api(address: str, filter: list):
    filter_list = ""
    if len(filter) > 0:
        filter_list = f"{filter[0]}%2000:00:00~{filter[1]}%2000:00:00"
    url = f'https://dashboard.misttrack.io/api/v1/address_graph_analysis?coin=USDT-BEP20&address={address}&time_filter={filter_list}'

    response = requests.get(url, headers=MIST_HEADER)
    if response.status_code == 200:
        j = response.json()
        if "success" in j and j["success"] is False:
            print(j)
            return ""
        else:
            return response.text
    else:

        return ""


class MistAcquireDat:
    def __init__(self):
        self.folder = "data/mist"
        self.tmp = {}

    def save(self, address: str, filter: list = []):
        content = get_mist_graph_api(address, filter)
        if content == "":
            return
        file_name = f"{address}-{filter}.json"
        file = os.path.join(self.folder, file_name)
        Filex.writeFile(content, file)

    def overview(self, address: str) -> str:
        if address not in self.tmp:
            self.tmp[address] = get_mist_overview(address)
        return self.tmp[address]
