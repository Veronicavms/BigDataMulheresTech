class NumeroImparError(Exception):
    """Exceção personalizada para números ímpares."""
    pass

def ler_par_de_numeros():
    """Lê um par de números inteiros do usuário."""
    while True:
        try:
            a = int(input("Digite o primeiro número inteiro: "))
            b = int(input("Digite o segundo número inteiro: "))
            
            # Verifica se os números são ímpares
            if a % 2 != 0 or b % 2 != 0:
                raise NumeroImparError("Um dos números é ímpar. Por favor, insira apenas números pares.")
            
            return a, b
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
        except NumeroImparError as e:
            print(e)

def main():
    somas = []
    
    for i in range(3):
        print(f"\nLendo o par de números {i + 1}:")
        a, b = ler_par_de_numeros()
        soma = a + b
        somas.append(soma)
        print(f"A soma do par {i + 1} é: {soma}")

if __name__ == "__main__":
    main()
