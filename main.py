lista_do_cadastrados = []

def menu():
    while True:
        print('''ESCOLHA UM ENTRE AS OPÇÕES ABAIXO
 1 --- CADASTRAR
 2 --- VER CADASTRADOS
 3 --- SAIR DO MENU''')
        
        escolha = int(input('====> '))

        if escolha == 3:
            print('==========SAINDO==========')
            break
            
        elif escolha == 1:
            exibir_menu()
            nome, idade, cpf, email, senha = solicitar_dados()
            if validar_dados(nome, idade, cpf, email, senha):
                print('✅ Cadastro válido!')
                lista_do_cadastrados.append({
                    "nome": nome,
                    "idade": idade,
                    "cpf": cpf,
                    "email": email,
                    "senha": senha
                })

        elif escolha == 2:
             if not lista_do_cadastrados:
                print('📭 Nenhum usuário cadastrado ainda.')
             else:
                print('\n==== USUÁRIOS CADASTRADOS ====')
                for i, usuario in enumerate(lista_do_cadastrados, 1):
                    print(f"{i}. {usuario['nome']} - {usuario['email']}")

    else:
        print('=======ERROOOOO=======')


def exibir_menu():
    print('====== CADASTRO BORGES ENTERPRISE ======')

def solicitar_dados():
    nome = input('NOME COMPLETO: ').title()
    idade = input('IDADE (XX/XX/XXXX) : ')
    cpf = input('DIGITE SEU CPF (XXXXXXXXX-XX) : ')
    email = input('DIGITE SEU E-MAIL: ')
    senha = input('DIGITE SUA SENHA (minímo de 6 carácteres) : ')
     
    return nome, idade, cpf, email, senha

def validar_dados(nome, idade, cpf, email, senha):
    if len(senha) < 6:
        print('NÚMERO DE CARÁCTERES INSUFICIENTE')
        return False
    
    if '@' not in email:
        print('E-MAIL INVÁLIDO')
        return False
    
    return True

menu()

