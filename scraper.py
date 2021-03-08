import requests
from bs4 import BeautifulSoup

def boz_soup():
    response = requests.get("https://boz.zm")
    soup = BeautifulSoup(response.content, "html.parser")
    return soup 

def bank_exchange_rates():
    page = boz_soup()
    bank_table = page.find(id="bank_rates_desktop")
    body = bank_table.tbody
    row = body.tr
    data = []
    for r in row.find_next_siblings("tr"):
        d = {}
        bank = r.th
        d["bank"] = str(bank.string)
        td = r.td
        times = ["09:30", "12:30", "15:30"]
        x = 0
        cur_rows = td.find_next_siblings("td")
        for n,fx in enumerate(cur_rows):
            if 'fx-retail-cell' in fx["class"]:
                if n % 2 == 0:
                    # print(cur_rows[n-1])
                    d[times[x]] = {"buy": str(cur_rows[n-1].string),"sell":str(fx.string)}
                    x+=1
        data.append(d)
    return data


# pprint.pprint(bank_exchange_rates())