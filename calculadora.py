def calculadora():
    # Solicitação dos números a serem calculados
    try:
        num1 = float(input("Digite o primeiro número: "))

        num2 = float(input("Digite o segundo número: "))
        # Solicitação da operação a ser realizada
        operacao = input("Digite a operação desejada (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.\n")
                return calculadora()
            resultado = num1 / num2

        print(f" Resultado: {num1} {operacao} {num2} = {resultado}\n")
    
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números válidos.\n")
        return calculadora()


calculadora()