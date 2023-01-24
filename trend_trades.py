from df_calculators import trend_calculator

#Empty lists for trend trades
trend_cryptos = []

#Entry prices list
trend_entry_prices = []


#Parametros de Compra Reversal y Trend Trade
RSI_buy = 40
MFI_buy = 25
STOCH_buy = 25

#Alerta cruce del stoch
a = 2.5
b = 7
c = -2.5
d = -7


def trend_trade_detector(dict1, dict2, dict3, dict4,dict5,dict6,dict7,dict8,dict9):

    for (k, v), (k2, v2), (k3, v3), (k4, v4),(k5, v5),(k6, v6), (k7,v7),(k8,v8),(k9,v9) in zip(dict1.items(), dict2.items(), dict3.items(), dict4.items(), dict5.items(),dict6.items(),
                                                                                                                        dict7.items(),dict8.items(),dict9.items()):

        if ((v < RSI_buy) and (v2 < MFI_buy) and (v3 < STOCH_buy) and (v4 < STOCH_buy) and ((v3 - v4) >= a) and ((v3 - v4) <= b) and (v8 >= v7) and (v9 < 40)):

            trend_cryptos.append(k)
            trend_entry_prices.append(v8)

    #
    trend_list = list(zip(trend_cryptos, trend_entry_prices))
    trend_calculator.df_trend_calc(trend_list)

    trend_cryptos.clear()
    trend_entry_prices.clear()

