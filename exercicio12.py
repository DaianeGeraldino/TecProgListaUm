carros_vendidos = float(input('Digite a quantidade de carros vendidos '))
valor_total = float(input('Digite o valor total de vendas '))
salario_fixo = float(input('Digite o valor do salario fixo '))
comissão = float(input('Digite o valor da comissão '))

salario_final = salario_fixo+(comissão*carros_vendidos)+((5*valor_total)/100)

print(f'Seu salário final é igual a {salario_final}')