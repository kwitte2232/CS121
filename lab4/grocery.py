


def read_into_dict(filename):
    f = open(filename, 'r')
    lines = f.readlines()

    prices = {}

    for l in lines:
        rem = l.strip('\n')
        product, cost_string = rem.split(" ")
        cost = float(cost_string)
        prices[product] = cost

    return prices

    f.close()

def calc_cost(prices, receipt):

    items = receipt.keys()

    total = 0

    for i in items:
        unit_price = prices[i]
        item_cost = (unit_price)*(receipt[i])
        total = total + item_cost

    return total

def process_receipt(prices, receipt_file):

    receipt = read_into_dict(receipt_file)
    sales_cost = calc_cost(prices, receipt)

    print(sales_cost)

    return sales_cost