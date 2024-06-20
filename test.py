from deephedge.instruments.brownianstock import BrownianStock
from deephedge.instruments.derivative import EuropeanCall

stock = BrownianStock()
stock.simulate()
print(stock.spot)

option = EuropeanCall(stock, 1.0)
option.simulate()




