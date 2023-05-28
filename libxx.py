import requests

api_key = "59IISNUG2CR3PIMAJF7MACQTS7DY6WFJDJ"
url = 'https://api.bscscan.com/api'
statement = 'End : {}, IO File {}'


def list_trans(_account: str, page_d: int = 0):
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
        print(response)
        a = response.json()
        message_ed = a['message']
        code_p = int(a['status'])
        print(f"page: {page_d}")
        if code_p == 1:
            print(response)
            print("OKKKKK")
            res_list = a["result"]
            _dp_result(res_list)
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


class Filex:
    def __init__(self):
        self.file_name = "report_network.txt"

    def AppendLineLog(self, content: str):
        file_object = open(self.file_name, 'a')
        file_object.write(content)
        file_object.close()

    def AppendLineTransaction(self, content: str):
        file_object = open(self.file_name, 'a')
        file_object.write(content)
        file_object.close()


def _dp_result(tx: list):
    file_x = Filex()
    for a in tx:
        data = a["input"]
        method = data[0:9]
        if "0x5fdbfd8" == method:
            child = data[34:74]
            parent = data[98:]
            file_x.AppendLineLog(f"{child} - {parent}\n")
        else:
            print(f"skip -- {method}")
