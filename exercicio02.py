"""
Crie um programa que permita a um professor registrar as notas de uma turma.
O programa deve continuar solicitando notas até que o professor digite 'fim'.
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e
continuar solicitando.
No final, deve exibir a média da turma.
"""
listaDeNotas = []


def registroDeNotas():
    # armazenar notas como lista

    while True:
        # coletar notas que o usuário quer inserir
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        if entrada == 'fim':
            print("Encerrando o registro de notas.")
            break
        else:
            try:
                # validar notas inseridas
                nota = float(entrada)
                if 0 <= nota <= 10:
                    listaDeNotas.append(nota)
                else:
                    print("Nota inválida. Digite uma nota entre 0 e 10.\n")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número de 0 a 10 ou 'fim' para encerrar.\n")

    calcularMedia(listaDeNotas)


def calcularMedia(listaDeNotas):
    if listaDeNotas:
        # calcular média
        media = sum(listaDeNotas)/len(listaDeNotas)
        # exibir média
        print("A média da turma é:" + str(media))
    else:
        print("Nenhuma nota válida foi inserida.")


registroDeNotas()