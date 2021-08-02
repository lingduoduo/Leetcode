## Margin Call

```python
from collections import defaultdict
import math

def build(data):
    position = defaultdict(int)
    cash = 1000
    for timestamp, symbol, action, quantity, price in data:
        quantity = int(quantity)
        price = int(price)
        if action == "B":
            position[symbol] += quantity
            cash -= quantity * price
        else:
            position[symbol] -= quantity
            cash += quantity * price
    res = [["CASH", cash]] + sorted(position.items())
    return res


def build1(data):
    def sell(symbol, quantity, price):
        position[symbol] -= quantity
        return quantity * price

    position = defaultdict(int)
    mark = {}
    cash = 1000
    for timestamp, symbol, action, quantity, price in data:
        quantity = int(quantity)
        price = int(price)
        mark[symbol] = price
        if action == "B":
            position[symbol] += quantity
            cash -= quantity * price
            if cash >= 0:
                continue
            tmp = list(position.items())
            tmp.sort(key=lambda x: (mark[x[0]], x[0]), reverse=True)
            for ts, tq in tmp:
                to_sell = min(tq, math.ceil(abs(cash) / mark[ts]))
                cash += sell(ts, to_sell, mark[ts])
                if cash >= 0:
                    break
        else:
            cash += sell(symbol, quantity, price)

    res = [["CASH", cash]] + sorted(position.items())
    return res
```

## Stock Match

```python
from collections import Counter, defaultdict
def stock_matching(house_trades, street_trades):
    house_ct = Counter(house_trades)
    street_ct = Counter(street_trades)
    for trade in house_ct.keys():
        if trade in street_ct:
            m = min(house_ct[trade], street_ct[trade])
            house_ct[trade] -= m
            street_ct[trade] -= m
    house_rem = []
    street_rem = []
    for key, val in house_ct.items():
        house_rem.extend([key] * val)
    for key, val in street_ct.items():
        street_rem.extend([key] * val)
    # res = house_rem + street_rem
    # res.sort()
    # return res

    # Follow up 1
    house_dic = defaultdict(list)
    street_dic = defaultdict(list)
    for trade in house_rem:
        house_dic[trade[:11]].append(trade[12:])
    for trade in street_rem:
        street_dic[trade[:11]].append(trade[12:])
    for _, val in house_dic.items():
        val.sort()
    for _, val in street_dic.items():
        val.sort()
    for trade in house_dic.keys():
        fuzzy = trade[:11]
        if fuzzy in street_dic:
            m = min(len(house_dic[fuzzy]), len(street_dic[fuzzy]))
            house_dic[fuzzy] = house_dic[fuzzy][m:]
            street_dic[fuzzy] = street_dic[fuzzy][m:]
    house_rem = []
    street_rem = []
    for key in house_dic:
        for val in house_dic[key]:
            house_rem.append(key + "," + val)
    for key in street_dic:
        for val in street_dic[key]:
            street_rem.append(key + "," + val)
    res = house_rem + street_rem
    res.sort()
    return res
```
