# Parametros: valorDaConta, percentualGorjeta, valorDaGorjeta

valorDaConta = float(input('Digite o valor da conta: '))

percentualGorjeta = float(input('Digite qual a porcentagem da gorjeta: '))


def gorjeta(valorDaConta, percentualGorjeta):
    valorDaGorjeta = float(valorDaConta * (percentualGorjeta / 100))
    print(f'O valor da gorjeta é: R$ {valorDaGorjeta:.2f}')
    return valorDaGorjeta


gorjeta(valorDaConta, percentualGorjeta)

