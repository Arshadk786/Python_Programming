stocks = {
    "bear market": "It refers to a period in which the prices of equity shares fall consistently. It’s usually a "
                   "condition where share prices fall by 20% from recent hghs.",
    "bull market": "An opposite of the bear market, a bull market is a market where the prices of the stocks are "
                   "increasing over a prolonged period of time. A single stock and a sector can be bullish at one "
                   "time and bearish at another time.",
    "blue chip stock": "These are equity shares of companies which are well-established and financially stable. These "
                       "generally have a relatively high market capitalization. ",
    "dividend yield": "It shows how much a company or firm pays out in dividends every year as compared to the stock "
                      "price. "
}
query = input("Enter your word (Bear Market,Bull Market,Blue Chip Stock): ")
print(query + " :- " + stocks[query.lower()])
