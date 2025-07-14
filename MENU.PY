from main import exibir_menu
from main import lista_do_cadastrados


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

        elif escolha == 2:
            print(lista_do_cadastrados)
        
        else:
            print('=======ERROOOOO=======')


