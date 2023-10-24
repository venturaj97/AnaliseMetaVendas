import pandas as pd
from twilio.rest import Client
#passo a passo

account_sid = "AC9b58d3e8f621de42ab588c6d9e78b1cb"
auth_token = "07cdf2816ee91e21b71fae8ecc833726"
client = Client(account_sid, auth_token)

#abrir os 6 arquivos em excel

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:   # para cada arquivo:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55 mil

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} a meta foi batida. Vendedor: {vendedor}, Vendas: {vendas}.')
        message = client.messages.create(
            body=f'No mês de {mes} a meta foi batida. Vendedor: {vendedor}, Vendas: {vendas}.',
            from_='+19207538040',
            to='+5521980115136'
        )
        print(message.sid)

#se for maior que 150mil a gente envia um sms pro proprio numero
#caso nao seja maior, nao fazer nada



