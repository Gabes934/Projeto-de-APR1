# -------
# MENUS
# -------
def exibir_menu_principal():
    print("\n===== CONCESSIONÁRIA - TESTE DRIVE =====")
    print("1 - Submenu de Cliente")
    print("2 - Submenu de Veículo")
    print("3 - Submenu de TesteDrive")
    print("4 - Submenu Relatórios")
    print("5 - Sair")
    print("------------------------------")

def exibir_submenu(titulo):
    print("\n===== SUBMENU DE " + titulo + " =====")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    print("0 - Voltar")
    print("------------------------------")

def exibir_menu_relatorios():
    print("\n===== RELATÓRIOS =====")
    print("1 - Avaliações de um veículo")
    print("2 - Clientes que testaram um veículo em uma data")
    print("3 - Veículos testados entre duas datas")
    print("0 - Voltar")
    print("------------------------------")

# --------
# CLIENTE
# --------
def coletar_dados_cliente(clientes):
    cpf = input("CPF: ")

    for cliente in clientes:
        if cliente[0] == cpf:
            print("Já existe um cliente cadastrado com esse CPF!")
            return None

    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    sexo = input("Sexo (M/F): ")
    telefone_fixo = input("Telefone fixo: ")
    celular = input("Celular: ")
    email = input("E-mail: ")

    novo_cliente = [cpf, nome, data_nascimento, sexo, telefone_fixo, celular, email]
    return novo_cliente
# --------
# VEÍCULO
# --------

# ------------
# TESTE DRIVE
# ------------

# -----------
# RELATÓRIOS
# -----------

# --------------------
# PROGRAMA PRINCIPAL
# --------------------
def main():
    clientes = {}
    veiculos = {}
    testes = {}
 
    opcao = ""
    while opcao != "5":
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip() #remove os espaços em branco do começo e do fim do texto
        if opcao == "1":
            submenu_cliente(clientes, testes)
        elif opcao == "2":
            submenu_veiculo(veiculos, testes)
        elif opcao == "3":
            submenu_teste(testes, clientes, veiculos)
        elif opcao == "4":
            submenu_relatorios(testes, clientes, veiculos)
        elif opcao == "5":
            print("Encerrando o programa. Até logo!")
        else:
            print("Opção inválida.")
