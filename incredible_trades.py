from df_calculators import incredible_calculator

#Parametros de compra increible -
RSI_inc = 35
MFI_inc = 25
STOCH_inc = 10

#Empty lists for incredible trades
incredible_cryptos = []

#Entry prices list
incredible_prices = []

#Alerta cruce del stoch
a = 2.5
b = 7
c = -2.5
d = -7


def incredible_trade_detector(dict1, dict2, dict3,dict4, dict5, dict6, dict7, dict8, dict9,dict10,dict11):

    for (k, v), (k2, v2), (k3, v3), (k4, v4), (k5, v5), (k6, v6), (k7, v7), (k8, v8), (k9, v9),(k10, v10),(k11, v11) in zip(dict1.items(), dict2.items(),
                            dict3.items(), dict4.items(), dict5.items(),dict6.items(),dict7.items(),dict8.items(),dict9.items(),dict10.items(),dict11.items()):

        if ((v < RSI_inc) and (v2 < MFI_inc) and (v3 < STOCH_inc) and (v4 < STOCH_inc) and ((v3-v4)>=a) and ((v3-v4) <=b) and (v10<STOCH_inc) and (v11<STOCH_inc)):

            incredible_cryptos.append(k)
            incredible_prices.append(v8)

    incredible_list = list(zip(incredible_cryptos, incredible_prices))
    incredible_calculator.df_incredible_calc(incredible_list)

    incredible_cryptos.clear()
    incredible_prices.clear()
