import pandas as pd
from email_functions import ricci_group_1_emails, telegram_sender, ricci_group_2_emails, principia_1_emails, principia_2_emails, telegram_sender_quant


#Riesgo-beneficio, TPs
rb = 2
SL_fixed = 0.33

def df_reversal_calc(list):

    if (list != []):

        # Create dataframe
        df = pd.DataFrame(list)
        #change column names, MAs = TPs
        df.columns = ['Crypto', 'Precio_Entrada','TP3']


        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        # Calculate TP/SL% and R/B
        df['Distancia_TP'] = df.apply(lambda x: (x['TP3'] - x['Precio_Entrada']),axis=1)
        df['TP2'] = df.apply(lambda x: (x['TP3'] - (x['Distancia_TP'] * 0.3)), axis=1)
        df['TP1'] = df.apply(lambda x: (x['TP3'] - (x['Distancia_TP'] * 0.7)), axis=1)
        df['TP_porcentaje'] = df.apply(lambda x:((x['Distancia_TP'] / x['Precio_Entrada'] * 100)), axis=1)
        df['Precio_SL'] = df.apply(lambda x: x['Precio_Entrada'] - (x['Precio_Entrada'] * SL_fixed), axis=1)
        df['Distancia_SL_porcentaje'] = df.apply(lambda x: (((x['Precio_SL'] / x['Precio_Entrada']) - 1) * 100), axis=1)

        # Drop columns
        df = df.drop(['Distancia_TP', 'Distancia_SL_porcentaje','TP_porcentaje'],axis=1)
        df = df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)

        print('----------------------------------------')
        #ricci_group_1_emails.ricci_sender_1(df, 'Reversal Trades 1D')
        #ricci_group_2_emails.ricci_sender_2(df, 'Reversal Trades 1D')
        #principia_1_emails.principia_sender_1(df, 'Reversal Trades 1D')
        #principia_2_emails.principia_sender_2(df, 'Reversal Trades 1D')
        telegram_sender.send_telegram_message(df, 'Reversal Trades 1D')
        telegram_sender_quant.send_telegram_message(df, 'Reversal Trades 1D')

    else:
        print('no cryptos were found')