def verificar_senha(senha):
    # tamanho da senha
    if len(senha) < 8:
        print("Senha muito curta, deve conter 8 digitos.")
        return False

    # Se tem numero
    if not any(char.isdigit() for char in senha):
        print("Senha deve conter números")
        return False
    elif not any(char.isalpha() for char in senha):
        print("Senha deve conter letras")
        return False
    return True


while True:
    senha = input("Digite a senha ou sair: ")

    if senha == "sair":
        print("Saindo...")
        break

    if verificar_senha(senha):
        print("Senha válida")
        break
    
    else:
        print("Senha inválida")