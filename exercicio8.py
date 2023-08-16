espaco_inicial = 2
veloc_inicial = 3
aceleracao = 10


tempo = float(input('Digite o tempo '))

espaco_percorrido = espaco_inicial+(veloc_inicial*tempo)+(0.5*aceleracao*(tempo*tempo))

print(f'O espaço total percorrido é de: {espaco_percorrido:.2f}')