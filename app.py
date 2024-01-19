import requests


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,CNY-BRL,BRL-USD")
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_yuan = requisicao_dic['CNYBRL']['bid']
    cotacao_brl = requisicao_dic['BRLUSD']['bid']

    text= f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}
    Yuan: {cotacao_yuan}
    Real: {cotacao_brl}
    '''
    print(text)

pegar_cotacoes()