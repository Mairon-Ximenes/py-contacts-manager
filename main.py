def obter_indice_contato(contatos: list, mensagem: str):
    if not contatos:
        print("Nenhum contato cadastrado.\n")
        return None

    ver_contatos(contatos)
    try:
        indice = int(input(mensagem)) - 1
        if 0 <= indice < len(contatos):
            return indice
        print("\nÍndice fora dos limites da agenda.\n")
    except ValueError:
        print("\nEntrada inválida. Digite um número inteiro\n")
    return None


def excluir_contato(contatos: list):
    indice = obter_indice_contato(contatos, "Digite o número do contato que deseja excluir: ")

    if indice is None:
        return

    removido = contatos.pop(indice)
    print(f"\nContato '{removido['nome']}' excluído com sucesso!\n")


def ver_contatos_favoritos(contatos: list):
    lista_fav = list(c for c in contatos if c["favorito"])
    print("\n========== Lista de Contatos Favoritos ==========\n")

    if not lista_fav:
        print("Nenhum contato marcado como favorito.\n")
        return

    for indice, contato in enumerate(lista_fav, start=1):
        nome = contato["nome"]
        favorito = "(★)" if contato["favorito"] else ""

        if indice != 1: print("-----//-----\n")

        print(f"{indice}. \n- Nome: {nome} {favorito}")
        print(f"- Telefone: {contato['telefone']}")
        print(f"- Email: {contato['email']}\n")


def marcar_desmarcar_favorito(contatos: list):
    indice = obter_indice_contato(contatos, "Digite o número do contato para favoritar/desfavoritar: ")
    if indice is None:
        return

    print("\n==========//==========\n")
    contatos[indice]["favorito"] = not contatos[indice]["favorito"]

    status = "marcado como favorito" if contatos[indice]["favorito"] else "removido dos favoritos"
    print(f"\nContato '{contatos[indice]['nome']}' {status}!\n")


def editar_contatos(contatos: list):
    indice = obter_indice_contato(contatos, "Digite o número do contato que deseja editar: ")
    if indice is None:
        return

    print("\n==========//==========\n")
    print(f"1. Nome: {contatos[indice]['nome']}")
    print(f"2. Telefone: {contatos[indice]['telefone']}")
    print(f"3. Email: {contatos[indice]['email']}")

    escolha = input("\nDigite qual dado deseja editar (1-3): ").strip()
    opcoes = {"1": "nome", "2": "telefone", "3": "email"}

    if escolha not in opcoes:
        print("\nOpção inválida.\n")
        return

    chave = opcoes[escolha]
    novo_valor = input("Digite o novo valor: ")
    contatos[indice][chave] = novo_valor

    print(f"\nCampo '{chave}' alterado com sucesso!\n")


def ver_contatos(contatos: list):
    print("\n========== Lista de Contatos ==========\n")
    if not contatos:
        print("Nenhum contato cadastrado.")

    for indice, contato in enumerate(contatos, start=1):
        nome = contato["nome"]
        favorito = "(★)" if contato["favorito"] else ""

        if indice != 1: print("-----//-----\n")

        print(f"{indice}. \n- Nome: {nome} {favorito}")
        print(f"- Telefone: {contato['telefone']}")
        print(f"- Email: {contato['email']}\n")


def adicionar_contato(contatos: list):
    print("\nPara adicionar um novo contato, precisamos das seguintes informações: ")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    if not nome:
        print("\nO nome do contato não pode ser vazio.\n")
        return

    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"\n{nome} adicionado a lista de contatos com sucesso!\n")


def main():
    contatos = []
    while True:
        print("========== Agenda de contatos ==========")
        print("1. Adicionar contato")
        print("2. Ver contatos")
        print("3. Editar contato")
        print("4. Marcar/desmarcar contato como favorito")
        print("5. Ver contatos favoritos")
        print("6. Apagar contato")
        print("7. Sair")

        escolha = input("Digite o que deseja fazer: ").strip()

        if escolha == "1":
            adicionar_contato(contatos)
        elif escolha == "2":
            ver_contatos(contatos)
        elif escolha == "3":
            editar_contatos(contatos)
        elif escolha == "4":
            marcar_desmarcar_favorito(contatos)
        elif escolha == "5":
            ver_contatos_favoritos(contatos)
        elif escolha == "6":
            excluir_contato(contatos)
        elif escolha == "7":
            break
        else:
            print("\nOpção inválida. Tenta novamente.\n")

    print("\nPrograma finalizado. Obrigado por usar a nossa agenda de contatos!\n")


if __name__ == "__main__":
    main()