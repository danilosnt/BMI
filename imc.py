def calcular_imc(peso, altura):
    if altura <= 0:
        return None
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III (Mórbida)"

def main():
    print("--- Calculadora de IMC (Índice de Massa Corporal) ---")

    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros, ex: 1.75): "))

        if peso <= 0:
            print("Erro: O peso deve ser um valor positivo.")
            return

        imc = calcular_imc(peso, altura)

        if imc is None:
            print("Erro: A altura deve ser um valor positivo.")
        else:
            classificacao = classificar_imc(imc)
            print(f"\nSeu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao}")

    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos para peso e altura.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()