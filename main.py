from meuPacote import meuModulo, mensagens, operacoes
import senha as sn

print(meuModulo.saudacao("Edson"))
print(meuModulo.soma(5, 10))


print("-------------------------------------\n")

mensagens.boasVindas()
print("Resultado da multiplicação: ", operacoes.multiplicar(5, 10))
print("Resultado da divisão: ", operacoes.dividir(10, 2))
mensagens.despedida()

sn.verificar_senha("12345678")