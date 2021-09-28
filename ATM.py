import operator


atm_banknotes = {
    "atm_banknotes": {1: 100, 5: 100, 10: 100, 20: 100, 50: 100},
    }

def cash_withdrawal(bill, amount):
    global atm_banknotes
    bill_dict = atm_banknotes[bill]
    sorted_entries = sorted(bill_dict.items(), key=operator.itemgetter(0))
    sorted_entries.reverse()
    delta_entries = []
    for entry in sorted_entries:
        delta = amount // entry[0]
        if delta > 0:
            resulting_delta = min(delta, entry[1])
            if resulting_delta > 0:
                amount -= resulting_delta * entry[0];
                delta_entries.append((entry[0], resulting_delta))
    if amount == 0:
        for delta_entry in delta_entries:
            bill_dict[delta_entry[0]] -= delta_entry[1]
    return delta_entries


def atm_balance(bill):
    global atm_banknotes
    bill_dict = atm_banknotes[bill]
    res = 0
    for x in bill_dict.items():
        res += x[0] * x[1]
    return res 


print('atm_balance:', atm_balance('atm_banknotes'))
print(atm_banknotes)
print(cash_withdrawal('atm_banknotes', 1330))
print(atm_banknotes)
print('atm_balance:', atm_amount('atm_banknotes'))
