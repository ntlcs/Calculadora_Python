# operação de soma
def soma(a, b):
    return a + b

# operação de subtração
def subtracao(a, b):
    return a - b

# operação de multiplicação
def multiplicacao(a, b):
    return a * b

# operação de divisão
def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return round(a / b, 2)

# operação de porcentagem
def porcentagem(a, percent):
    return (a * percent) / 100

# Função principal
def calculadora():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Porcentagem")

    escolha = input("Digite o número da operação desejada: ")

    num1 = float(input("Digite o primeiro número: "))
    
    if escolha == '5':
        percent = float(input("Informe o % ? "))
    else:
        num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = soma(num1, num2)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
    elif escolha == '4':
        resultado = divisao(num1, num2)
    elif escolha == '5':
        resultado = porcentagem(num1, percent)
    else:
        print("Escolha inválida")
        return

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()
