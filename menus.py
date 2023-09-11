import crud
import prints

listajogadores = []


def menuprincipal():
    ativador = int
    while ativador != 0:
        prints.printlinha()
        print(f'Menu de acesso')
        prints.printlinha()
        print(f'Selecione a opçao que voce deseja acessar')
        print(f'1-Cadastrar jogador')
        print(f'2-Alterar jogador')
        print(f'3-Deletar jogador')
        print(f'4-Mostrar a lista de jogadores')
        print(f'0-Sair')
        prints.printlinha()
        ativador = int(input(f'Qual opção do menu você deseja acessar?'))
        prints.printlinha()

        if ativador == 1:
            crud.insere(listajogadores)

        elif ativador == 2:
            crud.edita(listajogadores)

        elif ativador == 3:
            crud.remove(listajogadores)

        elif ativador == 4:
            crud.printlista(listajogadores)


        elif ativador == 0:
            print(f'Sistema finalizado com sucesso')
            break

        else:
            print(f'Numero invalido')
            print(f'Por favor digite um valor valido')
