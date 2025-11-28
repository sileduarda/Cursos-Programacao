# Leitura dos dados de entrada
peso = float(input('Qual o peso do produto em toneladas?'))
preco_por_tonelada = (float(input('Qual o valor do produto por tonelada? '))) * 5.32
tipo_cliente = input('Digite uma das opções \n Novo Cliente (N); \n Cliente Fidelizado (F)\n Cliente Premium (P)').upper().strip()

# Criando condição de desconto

descontos = {"N" : 1,
             "F" : 0.5,
             "P" : 0.1 
}

while True: 
    if tipo_cliente in descontos: 
        preco_por_tonelada = (peso * preco_por_tonelada) * descontos[tipo_cliente]
        break
    else: 
        print('Opção inválida! Digite novamente:')
        tipo_cliente = input('Digite uma das opções \n Novo Cliente (N); \n Cliente Fidelizado (F)\n Cliente Premium (P)').upper().strip()

print(f'O valor final a ser pago pelo cliente é de {preco_por_tonelada:.2f}') 
 