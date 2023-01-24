from df_calculators import reversal_calculator

#Parametros de Compra Reversal y Trend Trade
RSI_buy = 35
MFI_buy = 25
STOCH_buy = 25

#Empty lists for reversal trades

reversal_cryptos = []

#Entry prices list
reversal_entry_prices = []

#TP MA 200
MA200 = []

#Alerta cruce del stoch
a = 2.5
b = 7
c = -2.5
d = -7



#Reversal Detector
def reversal_trade_detector(dict1, dict2, dict3, dict4,dict5,dict6,dict7, dict8, dict9, dict10, dict11):

    for (k, v), (k2, v2), (k3, v3), (k4, v4),(k5, v5),(k6, v6), (k7,v7),(k8,v8),(k9,v9), (k10,v10), (k11,v11) in zip(dict1.items(), dict2.items(), dict3.items(), dict4.items(), dict5.items(),dict6.items(),
                                                                                               dict7.items(),dict8.items(),dict9.items(), dict10.items(), dict11.items()):


        if ((v < RSI_buy) and (v2 < MFI_buy) and (v3 < STOCH_buy) and (v4 < STOCH_buy) and ((v3-v4)>=a) and ((v3-v4) <=b) and (v7 > v5) and (v7 > v6) and (v6 > v5) and (v8 < v5) and (v10<10) and (v11<10)):

            reversal_cryptos.append(k)
            reversal_entry_prices.append(v8)
            MA200.append(v7)

    reversal_list = list(zip(reversal_cryptos, reversal_entry_prices, MA200))
    reversal_calculator.df_reversal_calc(reversal_list)

    reversal_cryptos.clear()
    reversal_entry_prices.clear()
    MA200.clear()