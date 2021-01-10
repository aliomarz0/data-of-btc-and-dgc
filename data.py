from matplotlib import pyplot as plt
import numpy as np

plt.style.use('Solarize_Light2')

btc_x = [2013,2014,2015,2016,2017,2018,2019,2020,2021]
btc_y = [1100,841,355,952,13000,11000,12000,28000,41000]

dgc_x = [2013,2014,2015,2016,2017,2018,2019,2020,2021]
dgc_y = [0.00026,0.001733,0.0019,0.000187,0.003,0.009,0.003,0.0034,0.01]

plt.plot(btc_x,btc_y,'k--' ,label='BTC')
plt.plot(dgc_x,dgc_y, 'r',label = 'DGC')

plt.title("History of Dogecoin and Bitcoin")

plt.ylabel("Price per Coin")
plt.xlabel("Year")
 
plt.legend()

plt.tight_layout()

plt.grid(True)

plt.show()
