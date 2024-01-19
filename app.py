import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,CNY-BRL,BRL-USD")
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_yuan = requisicao_dic['CNYBRL']['bid']
    cotacao_brl = requisicao_dic['BRLUSD']['bid']

    resposta_cotacao['text']= f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}
    Yuan: {cotacao_yuan}
    Real: {cotacao_brl}
    '''
    """ print(text) """


janela = Tk()
janela.title("Cotação Atual de Moedas")
janela.geometry("300x300")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

resposta_cotacao = Label(janela, text="")
resposta_cotacao.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()