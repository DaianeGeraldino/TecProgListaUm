anos = int(input('Digite sua idade de anos '))
meses = int(input('Digite a quantidade meses de vida '))
dias = int(input('Digite a quantidade de dias '))

quantidade_anos = anos * 365
quantidade_meses = meses * 30

print(f'A quantidade de dias total é: {quantidade_anos+quantidade_meses+dias}')