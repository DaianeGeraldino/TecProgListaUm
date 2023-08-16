altura_parede = float(input("digite a altura da parede: "))
largura_parede = float(input("digite a largura da Parede: "))

altura_azulejo = float(input("digite a altura do Azulejo: "))
largura_azulejo = float(input(" do Azulejo: "))

area_parede = altura_parede*largura_parede
area_azulejo = altura_azulejo*largura_azulejo

quantidade_azulejo = area_parede/area_azulejo

print(f'A quantidade de azulejos necessarias é de: {quantidade_azulejo:.2f}')

