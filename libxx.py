import requests
import graphviz
import math


api_key = "59IISNUG2CR3PIMAJF7MACQTS7DY6WFJDJ"
url = 'https://api.bscscan.com/api'
statement = 'End : {}, IO File {}'

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

    def openRelation(self)->list:
        mlist = []
        with open(self.file_name, newline='') as f:
            for line in f.readlines():
                line = line.replace("\n","")
                address_p = line.split(" - ")
                mlist.append([f"0x{address_p[0]}",f"0x{address_p[1]}"])

        return mlist


def dp_result_x(tx: list):
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

def do_list_contract(_account: str, page_d: int = 0):
    
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
        print(f"page: {page_d}")
        
        if code_p == 1:    
            res_list = a["result"]
            dp_result_x(res_list)

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



def find_key(dictsx:list, address:str)->int:
    for i, item in enumerate(dictsx):
        if item["up"]==address:
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
            container[y]["children"]+=1
            container[y]["down"].append(child)
        else:
            # container[parent]["children"] = 0
            container.append({
                "up":parent,
                "children":0,
                "down":[],
            })
            
    container = sorted(container, key=lambda x: -x["children"])
  
    for c in container:
        up = c["up"]
        for dow in c["down"]:
            dot.edge(up, dow)
    #for level in container:
    #dot.edge(parent, child)
    #print(f"The total edges is 0")
    return dot

def graph_building_bsc_relations(project_name:str):
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

