import requests
import emoji

TOKEN = "5316537394:AAH7dsxa4SFQlW4_U1oNb8lTdGZ_q2ZfDaU"
chat_id = "-1934385975"

def send_telegram_message(df,type):
    msg = type + emoji.emojize(":red_exclamation_mark:")
    msg2 = emoji.emojize(":chart_increasing:")
    msg3 = emoji.emojize(":rocket:")
    for i in range(len(df)):
        msg = msg + '\nCrypto: ' + (df['Crypto'].iloc[i]) + '/ USDT' + '\n Entry Price: ' + str((df['Precio_Entrada'].iloc[i])) + '\n TP1: ' + str(
            (df['TP1'].iloc[i])) + '\n TP2: ' + str((df['TP2'].iloc[i])) + '\n TP3: ' + str((df['TP3'].iloc[i])) + '\n SL: ' + str(
            (df['Precio_SL'].iloc[i])) + '\n Rating: ' + (df['Rating'].iloc[i]) + '\n' + msg2 + msg3 + '\n ---------------------'

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    r = requests.get(url)
    print(msg)
    print(r.json())
