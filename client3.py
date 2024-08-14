import urllib.request


def getdatapoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price

def getratio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    """ Also create some unit tests for this function in client_test.py """
    if (price_b == 0):
            # when price_b is 0 avoid throwing ZeroDivisionError
            return
    return price_a/price_b

# Main
if __name__ == "_main_":
    #Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = josn.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        """ ----
        --------- Update to get the ratio ------------- """
        prices ={}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quotes %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))





