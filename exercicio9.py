quantidade_macas = int(input('Digite a quantidade de maças compradas '))
kg_banana = float(input('Digite a quantidade de kg de bananas compradas '))

custo_maca = quantidade_macas*1.3
custo_banana = kg_banana*5
custo_total = custo_maca+custo_banana

print(f'O custo total da compra é de: {custo_total}')