from deephedge.instruments.brownianstock import BrownianStock

stock = BrownianStock()
stock.simulate()
print(stock.spot)



