num = int(input('Digite um número inteiro: '))


dezmilhar = num // 10000
resto_dezmilhar = dezmilhar % 10000
milhar = resto_dezmilhar // 1000
resto_milhar = num % 1000
centena = resto_milhar // 100
resto_centena = resto_milhar % 100
dezena = resto_centena // 10
resto_dezena = resto_centena % 10
# unidade = resto_dezena // 1

# print(milhar)
# # print(resto_milhar)
# print(centena)
# # print(resto_centena)
# print(dezena)
# print(resto_dezena)

print('O dígito das dezenas é {}'.format(dezena))