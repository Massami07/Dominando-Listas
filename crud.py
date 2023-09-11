def insere(listajogadores):
    d = int
    while d != 0:
        print('Esta e a lista atual')
        printlista(listajogadores)
        print(f'Digite 1 para adicionar na ultima posicao')
        print(f'Digite 2 para escoler em qual posicoa voce deseja adicionar')
        print(f'Digite 0 para voltar ao menu anterior')
        d = int(input(f"Qual a Voce escolhe??"))

        if d == 1:
                jogador = input(f"Qual jogador voce deseja adicionar")
                listajogadores.append(jogador)
                print(f"O jogador Adicionado foi o ", listajogadores[len(listajogadores) - 1])

        elif d == 2:
            if len(listajogadores) == 0:
                print("A lista esta vazia")
                p = 0
                jogador = input(f"Qual jogador voce deseja adicionar?")
                listajogadores.insert(p - 1, jogador)
                print(f"O jogador Adicionado foi o ", listajogadores[p - 1], 'na posicao', p+1)
            else:
                    p = int(input(f"Qual a posicao que voce deseja adicionar?"))
                    if p > len(listajogadores) :
                        print("Essa posição é maior que a lista de jogadores, o jogador será incluído na última posição da lista.")
                        jogador = input(f"Qual jogador voce deseja adicionar?")
                        listajogadores.append(jogador)
                    else:
                        jogador = input(f"Qual jogador voce deseja adicionar?")
                        listajogadores.insert(p - 1, jogador)
                        print(f"O jogador Adicionado foi o ", listajogadores[p - 1], 'na posicao', p -1 )

        elif d == 0:
            break

        else:
            print(f"Numero invalido")


def edita(listajogadores):
    if len(listajogadores) == 0:
        print(f"A lista esta vazia")
    else:
        print('Esta e a lista atual')
        printlista(listajogadores)
        p = int(input(f"Qual a posicao da lista que voce deseja alterar?"))
        jogadorremovido = listajogadores[p - 1]
        listajogadores[p - 1] = input(f"Qual jogador voce deseja adicionar?")
        print(f"O jogador ", jogadorremovido, " foi alterado para o jogador ", listajogadores[p - 1])


def remove(listajogadores):
    d = int
    while d != 0:
        print('Esta e a lista atual')
        printlista(listajogadores)
        print(f'Digite 1 para excluir o ultimo jogador')
        print(f'Digite 2 para escoler qual posicoa voce deseja excluir')
        print(f'Digite 0 para voltar ao menu anterior')
        d = int(input(f"Qual a Voce escolhe??"))

        if d == 1:
            if len(listajogadores) == 0:
                print("A lista esta vazia")
            else:
                jogadorremovido = listajogadores.pop()
                print(f"O jogador deletado foi o ", jogadorremovido)

        elif d == 2:
            if len(listajogadores) == 0:
                print("A lista esta vazia")
            else:
                p = int(input(f"Qual a posicao que voce deseja deletar?"))
                if p > len(listajogadores):
                    print(
                        "Essa posição é maior que a lista de jogadores, o jogador será deletado na última posição da lista.")
                    jogadorremovido = listajogadores.pop()
                    print(f"O jogador deletado foi o ", jogadorremovido)
                else:
                    jogadorremovido = listajogadores.pop(p - 1)
                    print(f"O jogador deletado foi o ", jogadorremovido)

        elif d == 0:
            break

        else:
            print(f"Numero invalido")


def printlista(listajogadores):
    print(listajogadores)