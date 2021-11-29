#!C:/Python39/python

import json
import requests


key = 'YKMR1NX75O2HJ165'

def getStockData(stock):
    
    stock = stock.upper()
    url = (f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&interval=5min&apikey={key}')
    call = requests.get(url).text
    
    # Prints JSON format response string, a la Project Deliverable example
    print("\nJSON response string")
    print(call)
    
    # Per PD, the following should technically be a separate method or within main. But it makes more sense this way.
    quote = json.loads(call)
    
    # "Converts" JSON to Python dictionary, though nested
    price = (quote['Global Quote']['05. price'])
    print(f"The current price of {stock} is: ${price}\n")
    

    return call


def main():
    
    symbol = ""
    
    with open('japi.out', 'a') as f:
        while(symbol.upper() != "QUIT"):
            if(symbol != ""):
                s = getStockData(symbol)
                #Not sure if you wanted whole quote or just price quote
                f.write(s)
            symbol = input("What stock would you like to check? (Quit to exit): ")
        f.close()
        
        
    
main()
