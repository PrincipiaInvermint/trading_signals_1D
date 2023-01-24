import pandas as pd
from email_functions import ricci_group_1_emails, telegram_sender, ricci_group_2_emails, principia_1_emails, principia_2_emails

#Riesgo-beneficio, TPs
tp1 = 0.3
tp2 = 0.75
tp3 = 1.2
tp4 = 1.8
SL_fixed = 0.33

def df_trend_calc(list):

    if (list != []):

        # Create dataframe
        df = pd.DataFrame(list)
        #change column names, MAs = TPs
        df.columns = ['Crypto', 'Precio_Entrada']

        df['TP1'] = df.apply(lambda x: x['Precio_Entrada'] + x['Precio_Entrada'] * tp1, axis=1)
        df['TP2'] = df.apply(lambda x: x['Precio_Entrada'] + x['Precio_Entrada'] * tp2, axis=1)
        df['TP3'] = df.apply(lambda x: x['Precio_Entrada'] + x['Precio_Entrada'] * tp3, axis=1)
        df['TP4'] = df.apply(lambda x: x['Precio_Entrada'] + x['Precio_Entrada'] * tp4, axis=1)

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        # Calculate TP/SL% and R/B
        df['Distancia_TP'] = df.apply(lambda x: (x['TP4'] - x['Precio_Entrada']),axis=1)
        df['TP_porcentaje'] = df.apply(lambda x:((x['Distancia_TP'] / x['Precio_Entrada'] * 100)), axis=1)
        df['Precio_SL'] = df.apply(lambda x: x['Precio_Entrada'] - (x['Precio_Entrada'] * SL_fixed), axis=1)
        df['Distancia_SL_porcentaje'] = df.apply(lambda x: (((x['Precio_SL'] / x['Precio_Entrada']) - 1) * 100), axis=1)

        # Drop columns
        df = df.drop(['Distancia_TP', 'Distancia_SL_porcentaje','TP_porcentaje'],axis=1)

        #Final DF signals
        df = df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)
        ricci_group_1_emails.ricci_sender_1(df,'Trend Trades 1DD')
        ricci_group_2_emails.ricci_sender_2(df,'Trend Trades 1D')
        principia_1_emails.principia_sender_1(df,'Trend Trades 1D')
        principia_2_emails.principia_sender_2(df, 'Trend Trades 1D')
        telegram_sender.send_telegram_message_D(df,'Trend Trades 1D')

    else:
        print('no cryptos were found')




