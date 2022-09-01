# write your code here!
import requests
import json


def cur_converter(code,amount, code2=None):
    # Use a breakpoint in the code line below to debug your script.
    r = requests.get(f"http://www.floatrates.com/daily/{code.lower()}.json")
    r = json.loads(r.text)
    # popular rates
    for k in r.keys():
        if k in ["eur", "usd"]:
            popular_rates.append(r[k])

    # print(popular_rates)  # Press Ctrl+F8 to toggle the breakpoint.
    print("Checking the cache...")
    # checking cache for rates
    for cur in popular_rates:
        if cur["code"].lower() == code2.lower():
            print("Oh! It is in the cache!")
            rate = float(cur['rate'])
            bal = round(float(amount) * rate, 2)
            return f"You received {bal} {code2.upper()}."

    print("Sorry, but it is not in the cache!")
    # getting rates from websites
    r = requests.get(f"http://www.floatrates.com/daily/{code.lower()}.json")
    r = json.loads(r.text)
    for k in r.keys():
        if r[k]["code"].upper() == code2.upper():
            c = r[k]
            rate = c["rate"]
            bal = round(float(amount) * rate, 2)
            popular_rates.append(c)
            return f"You received {bal} {code2.upper()}."

    return "Can't find rate"


if __name__ == '__main__':
    popular_rates = list()
    currency_code = input()
    while True:
        exchange_code = input()
        if exchange_code == "":
            break
        cur_amount = input()
        if cur_amount == "":
            break
        print(cur_converter(code=currency_code, code2=exchange_code, amount=cur_amount))

