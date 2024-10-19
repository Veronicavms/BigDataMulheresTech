#Atividade Pescador
def calcular_multa(peso_peixes):
    limite = 100 
    multa_por_kg = 20  

    if peso_peixes > limite:
        excesso = peso_peixes - limite
        multa = excesso * multa_por_kg
        return f"A multa a ser paga é de R$ {multa:.2f}."
    else:
        return "Não há multa a ser paga."


peso = 120 
resultado = calcular_multa(peso)
print(resultado)

#Atividade IMC
def calcular_imc(peso, altura):
    """Calcula o IMC."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Classifica o IMC de acordo com a tabela de referência."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    n = int(input("Quantas pessoas você deseja calcular o IMC? "))
    
    resultados = []
    
    for i in range(n):
        print(f"\nDados da pessoa {i + 1}:")
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        resultados.append((imc, classificacao))
    
    print("\nResultados:")
    for i, (imc, classificacao) in enumerate(resultados):
        print(f"Pessoa {i + 1}: IMC = {imc:.2f}, Classificação = {classificacao}")

if __name__ == "__main__":
    main()

#link da tabela https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight

#Atividade Cardápio de um Restaurante
def exibir_cardapio():
    """Exibe o cardápio do restaurante italiano."""
    cardapio = {
        "1": ("Spaghetti Carbonara", 25.00),
        "2": ("Lasagna", 30.00),
        "3": ("Pizza Margherita", 28.00),
        "4": ("Tiramisu", 15.00),
    }
    print("\nCardápio do Restaurante Italiano:")
    for chave, (prato, preco) in cardapio.items():
        print(f"{chave}. {prato} - R$ {preco:.2f}")
    return cardapio

def realizar_pedido(cardapio):
    """Permite ao cliente realizar um pedido."""
    pedido = []
    while True:
        item = input("\nDigite o número do prato que deseja pedir (ou 's' para sair): ")
        if item.lower() == 's':
            break
        elif item in cardapio:
            pedido.append(cardapio[item])
            print(f"{cardapio[item][0]} foi adicionado ao seu pedido.")
        else:
            print("Número do prato inválido. Tente novamente.")
    return pedido

def calcular_conta(pedido):
    """Calcula o total da conta com base no pedido."""
    total = sum(preco for _, preco in pedido)
    return total

def fechar_conta(total):
    """Imprime o total a ser pago."""
    print(f"\nO total da sua conta é R$ {total:.2f}. Obrigado e volte sempre!")

def main():
    cardapio = exibir_cardapio()
    pedido = realizar_pedido(cardapio)
    total = calcular_conta(pedido)
    fechar_conta(total)

if __name__ == "__main__":
    main()
