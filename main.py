import nsepy
import pprint
symbol = "infy"
url = ("https://www.nseindia.com/get-quotes/equity?symbol=INFY")


def data(symbol):
    data_live = {}

    data_live[symbol] = {"Open": float(nsepy.get_quote(symbol)["data"][0]["open"].replace(",", "")),
                         "High": float(nsepy.get_quote(symbol)["data"][0]["dayHigh"].replace(",", "")),
                         "Low": float(nsepy.get_quote(symbol)["data"][0]["dayLow"].replace(",", "")),
                         "Date": (nsepy.get_quote(symbol)["data"][0]["secDate"].replace(",", "")),
                         "Vwap": float(nsepy.get_quote(symbol)["data"][0]["averagePrice"].replace(",", "")),
                         "Ltp": float(nsepy.get_quote(symbol)["data"][0]["lastPrice"].replace(",", "")),
                         "Name": (nsepy.get_quote(symbol)["data"][0]["companyName"].replace(",", "")),
                         "Symbol": (nsepy.get_quote(symbol)["data"][0]["symbol"].replace(",", "")),
                         "Isin": (nsepy.get_quote(symbol)["data"][0]["isinCode"].replace(",", "")),
                        }
    print(url)
    pprint.pprint(data_live)
    


data(symbol)