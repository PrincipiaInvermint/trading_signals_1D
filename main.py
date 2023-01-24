from binance.client import Client
import configparser
import pandas as pd
import talib
import time
import incredible_trades
import reversal_trades
import trend_trades

# Cargar contraseñas API binance
config = configparser.ConfigParser()
config.read_file(open('conexion_API.cfg'))
api = config.get('BINANCE', 'API')
key = config.get('BINANCE', 'KEY')

#Conexion con binance para extraer datos
client = Client(api, key)

#Crypto List
symbols = ('BTC', 'ETH', 'DOT', 'SOL', 'MATIC', 'ATOM', 'FTM',
'SAND', 'BNB', 'XRP','KSM','NEAR','ADA','AVAX','LINK','ALGO','UNI','MANA','XLM','FIL','EGLD','VET','THETA','HNT','AAVE','TRX','DOGE','ENJ')

#Parametros para las señales 1 dia
run_interval_seconds = 43200

#Ciclo While que se ejecuta cada 15 minutos buscando las condiciones para los 3 tipos de trades

while True:

    RSI_list_1d = []
    RSI_list_1week = []

    STOCH_RSI_list_1d_fastd = []
    STOCH_RSI_list_1d_fastk = []

    STOCH_RSI_list_1week_fastd = []
    STOCH_RSI_list_1week_fastk = []

    MFI_list_1d = []

    MA_50_list_1D = []
    MA_100_list_1D = []
    MA_200_list_1D = []

    closing_list = []

    for symbol in symbols:
        candles_1d = client.get_klines(symbol=symbol + 'USDT', interval=Client.KLINE_INTERVAL_1DAY)
        candles_1week = client.get_klines(symbol=symbol + 'USDT', interval=Client.KLINE_INTERVAL_1WEEK)

        df_1d = pd.DataFrame(candles_1d)
        df_1week = pd.DataFrame(candles_1week)

        # 1D chart data
        open_1d = df_1d.iloc[:, 1]
        closings_1d = df_1d.iloc[:, 4]
        high_1d = df_1d.iloc[:, 2]
        low_1d = df_1d.iloc[:, 3]
        volume_1d = df_1d.iloc[:, 5]

        #last clossing prices
        close = (closings_1d.iloc[-1])


        #Moving averages
        MA_50 = talib.SMA(closings_1d, timeperiod=50)
        MA_100 = talib.SMA(closings_1d, timeperiod=100)
        MA_200 = talib.SMA(closings_1d, timeperiod=200)

        last_MA50 = MA_50.iloc[-1]
        last_MA100 = MA_100.iloc[-1]
        last_MA200 = MA_200.iloc[-1]

        # RSI and STOCH RSI 1 day
        rsi_1d = talib.RSI(closings_1d, timeperiod=14)
        fastk_1d, fastd_1d = talib.STOCH(rsi_1d, rsi_1d, rsi_1d, fastk_period=14, slowk_period=3, slowd_period=4,
                                         slowd_matype=0)

        last_fastk_1d = fastk_1d.iloc[-1]
        last_fastd_1d = fastd_1d.iloc[-1]

        last_RSI_1d = rsi_1d.iloc[-1]

        # MFI 1 day
        MFI_1d = talib.MFI(high_1d, low_1d, closings_1d, volume_1d, timeperiod=12)
        last_MFI_1d = MFI_1d.iloc[-1]

        # 3D chart data
        open_1week = df_1week.iloc[:, 1]
        closings_1week = df_1week.iloc[:, 4]
        high_1week = df_1week.iloc[:, 2]
        low_1week = df_1week.iloc[:, 3]
        volume_1week = df_1week.iloc[:, 5]

        # last clossing prices
        close_1week = (closings_1week.iloc[-1])

        # RSI 3 day
        rsi_1week = talib.RSI(closings_1week, timeperiod=14)

        fastk_1week, fastd_1week = talib.STOCH(rsi_1week, rsi_1week, rsi_1week, fastk_period=14, slowk_period=3, slowd_period=4,
                                         slowd_matype=0)

        last_fastk_1week = fastk_1week.iloc[-1]
        last_fastd_1week = fastd_1week.iloc[-1]


        last_RSI_1week = rsi_1week.iloc[-1]

        #Append last MA values in a dedicates list
        MA_50_list_1D.append(last_MA50)
        MA_100_list_1D.append(last_MA100)
        MA_200_list_1D.append(last_MA200)


        # Append last RSI values for each chart in a dedicated list
        RSI_list_1d.append(last_RSI_1d)
        RSI_list_1week.append(last_RSI_1week)

        # Append last STOCH RSI Values for each chart in a dedicated list
        STOCH_RSI_list_1d_fastk.append(last_fastk_1d)
        STOCH_RSI_list_1d_fastd.append(last_fastd_1d)

        STOCH_RSI_list_1week_fastk.append(last_fastk_1week)
        STOCH_RSI_list_1week_fastd.append(last_fastd_1week)


        # Append last MFI values for each chart in a dedicated list
        MFI_list_1d.append(last_MFI_1d)

        #Append last closing values
        closing_list.append(float(close))

        # Dictionary for better visualization
        dict_1d = dict(zip(symbols, RSI_list_1d))
        dict_1week = dict(zip(symbols, RSI_list_1week))
        dict_1d_closes = dict(zip(symbols,closing_list))
        dict_1d_STOCHRSI_k = dict(zip(symbols, STOCH_RSI_list_1d_fastk))
        dict_1d_STOCHRSI_d = dict(zip(symbols, STOCH_RSI_list_1d_fastd))
        dict_1d_MFI = dict(zip(symbols, MFI_list_1d))
        dict_1D_50MA = dict(zip(symbols,MA_50_list_1D))
        dict_1D_100MA = dict(zip(symbols, MA_100_list_1D))
        dict_1D_200MA = dict(zip(symbols, MA_200_list_1D))

        dict_1week_STOCHRSI_k = dict(zip(symbols, STOCH_RSI_list_1week_fastk))
        dict_1week_STOCHRSI_d = dict(zip(symbols, STOCH_RSI_list_1week_fastd))

    print(dict_1d_closes)

    print('Excellent trades:')
    incredible_trades.incredible_trade_detector(dict_1d, dict_1d_MFI, dict_1d_STOCHRSI_k, dict_1d_STOCHRSI_d,dict_1D_50MA, dict_1D_100MA, dict_1D_200MA,
                                                dict_1d_closes,dict_1week,dict_1week_STOCHRSI_k,dict_1week_STOCHRSI_d)

    print('-------------------------------------------------------------------')

    print('Reversal trades:')
    reversal_trades.reversal_trade_detector(dict_1d, dict_1d_MFI, dict_1d_STOCHRSI_k, dict_1d_STOCHRSI_d,dict_1D_50MA, dict_1D_100MA, dict_1D_200MA,
                                                dict_1d_closes,dict_1week,dict_1week_STOCHRSI_k,dict_1week_STOCHRSI_d)
    print('-------------------------------------------------------------------')

    #print('Trend trades:')
    #trend_trades.trend_trade_detector(dict_1d, dict_1d_MFI, dict_1d_STOCHRSI_k, dict_1d_STOCHRSI_d, dict_1D_50MA,dict_1D_100MA, dict_1D_200MA,
    #                               dict_1d_closes,dict_3d)

    print('-------------------------------------------------------------------')
    time.sleep(run_interval_seconds)
