nome = str(input('Digite o nome do cliente: '))
dia = str(input('Digite o dia de vencimento: '))
mes = str(input('Digite o mês de vencimento: '))
valor = str(input('Digite o valor da fatura: '))

print('Olá, {}'.format(nome))
print('A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.'.format(dia, mes, valor))