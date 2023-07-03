import requests
import lxml.html
import logging
from lxml import etree


class bnbscrape:
    def __int__(self):
        self.meta = [

        ]
        self.address = ""

    def check_contract(self, ad: str):
        self.address = ad

    def scrapeV3(self):
        headers = {
            "Cookie": "_ga=GA1.1.1492893560.1623527390; bscscan_cookieconsent=True; _ga_PQY6J2Q8EP=GS1.1.1688356204.75.1.1688360777.0.0.0; bitmedia_fid=eyJmaWQiOiI2NWZiMzE4NzgwYWU1MDExNmVkYmQ3YThiMThhNmFlZiIsImZpZG5vdWEiOiJhMjlmOGZiMzlmM2E3YzEzOTI2YjBkM2VmYTE2M2YzZiJ9; displaymode=dark; _ga_5Q0CRCD3YN=GS1.1.1686655032.4.1.1686655265.0.0.0; __stripe_mid=e4bd3b1a-f45b-4e2f-922e-569633b3210325b3fb; amp_fef1e8=1f438e32-2fa8-4d16-8a01-53f26d1c9870R...1h4d1t4ho.1h4d2005g.13.6.19; cf_clearance=GFwfgQtdJSP4VqwNnlo4XEjilgQxE6Cya6jlY8xiCK0-1688360366-0-150; ASP.NET_SessionId=hg4fvgyvjstjvhqqb44byc0z; __cflb=0H28vyb6xVveKGjdV3CFc257Dfrj7qvXiBZ98zU5obi; __cf_bm=l5JR7kBg3TfY94fN0X18E7ewIGoODBFnp0f8TaNrxh0-1688360108-0-AY+9ZGmcQxj1/ARyU8IktkcMSR+wD6K6JD4q6tM/IE3MLNei+copt4VgzO0JbnljTg==; __stripe_sid=e3c6e54a-a5cb-4268-bd37-9add11c23e25685d14; __cuid=bf01ee9c807e40749169892e2a943909",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0"
        }
        base = "https://bscscan.com/txs"
        payload = {
            "a": self.address,
            "ps": 100,
            "p": 1,
        }

        try:
            response = requests.request("GET", base, headers=headers, data=payload)
        except (
                requests.ConnectionError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectTimeout,
        ) as e:
            print(e)

        response.raw.decode_content = True
        tree = lxml.html.parse(response.raw)
        xpath_list = "/html/body/div[1]/main/div[2]/div/div/div[3]/table/tbody/tr"
        cell = "td[2]/span/a"
        tr_list = tree.xpath(xpath_list)
        # print(tr_list)
        for tr in tr_list:
            a = tr.xpath(cell)[0]
            print(a)
