# 1.

def area_retangulo():
    base = float(input('Digite o valor da base do retângulo: '))
    altura = float(input('Digite o valor da altura do retângulo: '))
    area = base * altura

    print(f'A área do retângulo é {area} m².')

# 2.

def area_quadrado():
    aresta = float(input('Digite o valor da aresta do quadrado: '))
    area = aresta * 4

    print(f'A área do retângulo é {area} m².')

# 3.

def area_triangulo():
    base = float(input('Digite o valor da base do triângulo: '))
    altura = float(input('Digite o valor da altura do triângulo: '))
    area = base * altura / 2

    print(f'A área do triângulo é {area} m².')

# 4.

def media_aritmetica():
    valor1 = float(input('Digite o valor 1: '))
    valor2 = float(input('Digite o valor 2: '))
    valor3 = float(input('Digite o valor 3: '))
    valor4 = float(input('Digite o valor 4: '))
    media = (valor1 + valor2 + valor3 + valor4) / 4

    print('Média aritmética:', media)

# 5.

def milha_km():
    milha = float(input('Digite o valor em milhas: '))
    convert2km = milha * 1.852

    print(f'Convertendo para quilômetros: {convert2km} km.')

# 6.

def diferente_maior():
    valor1 = float(input('Digite o valor 1: '))
    valor2 = float(input('Digite o valor 2: '))
    
    if valor1 == valor2:
        print('\nDigite números distintos.\n')
        diferente_maior()
    elif valor1 > valor2:
        print('O maior valor:', valor1)
    else:
        print('O maior valor:', valor2)

# 7.

def diferente_menor():
    valor1 = float(input('Digite o valor 1: '))
    valor2 = float(input('Digite o valor 2: '))
    
    if valor1 == valor2:
        print('\nDigite números distintos.\n')
        diferente_menor()
    elif valor1 < valor2:
        print('O menor valor:', valor1)
    else:
        print('O menor valor:', valor2)

# 8.

def area_retangulo_msg():
    base = float(input('Digite o valor da base do retângulo: '))
    altura = float(input('Digite o valor da altura do retângulo: '))
    area = base * altura

    if area > 100:
        print(f'{area} m², terreno grande.')
    else:
        print(f'{area} m², terreno pequeno.')

# 9.

def relacao_imc():
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite a sua altura (m): '))
    relacao = peso / altura ** 2

    if relacao < 20:
        print('Abaixo do peso.')
    elif relacao >= 20 and relacao < 25:
        print('Peso ideal.')
    elif relacao >= 25:
        print('Acima do peso.')

# 10.

def velocidade_final():
    a = float(input('Entre com o valor da aceleração (m/s²): '))
    vi = float(input('Entre com o valor da velocidade inicial (m/s): '))
    t = float(input('Entre com o valor do tempo (s): '))
    vf = vi + a * t

    if vf <= 40:
        print(f'{vf} m/s. Veículo muito lento.')
    elif vf > 40 and vf <= 60:
        print(f'{vf} m/s. Velocidade permitida.')
    elif vf > 60 and vf <= 80:
        print(f'{vf} m/s. Velocidade de cruzeiro.')
    elif vf > 80 and vf <= 120:
        print(f'{vf} m/s. Veículo rápido.')
    elif vf > 120:
        print(f'{vf} m/s. Veículo muito rápido.')