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
#clientes: chave = CPF(texto)
#valor = [nome, data_nascimento, sexo, telefone_fixo, celular, email]
#posição:  0         1             2      3              4       5
def coletar_dados_cliente(clientes):
    cpf = input("CPF: ")

    # se p CPF ja é uma chave do dicionário, não deixa cadastrar de novo
    if cpf in clientes:
        print("Já existe um cliente cadastrado com esse CPF!")
        return

    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    sexo = input("Sexo (M/F): ")
    telefone_fixo = input("Telefone fixo: ")
    celular = input("Celular: ")
    email = input("E-mail: ")

    #guarda no dicionario: CPF é a chave, o resto vai numa lista
    clientes[cpf] = [nome, data_nascimento, sexo, telefone_fixo, celular, email]
    print('Cliente cadastrado com sucesso!')

def exibir_cliente(cpf, dados):
    # recebe o cpf(chave) e a lista de dados e mostra tudo formatado
    print('CPF:',cpf)
    print('Nome:', dados[0])
    print('Data de nascimento:', dados[1])
    print('Sexo:', dados[2])
    print('Telefone_fixo:', dados[3])
    print('Celular:', dados[4])
    print('E-mail:', dados[5])
    print('-'*32)

def lista_todos_clientes(clientes):
    if len(clientes) == 0:          #dicionario vazio
        print('Nenhum cliente cadastrado.')
        return

    for cpf in clientes:         # o for percorre as chaves (CPFs)
        exibir_cliente(cpf, clientes[cpf])

def lista_um_cliente(clientes):
    cpf = input('CPF do cliente: ')

    if cpf not in clientes:
        print('Cliente não encontrado!')
        return

    exibir_cliente(cpf, clientes[cpf])

def alterar_clientes(clientes):
    cpf = input('CPF do cliente que deseja alterar: ')

    if cpf not in clientes:
        print('Cliente não encontrado.')
        return
    #o cpf é a chave e nao muda; pede só os outros dados
    nome = input('Novo nome: ')
    data_nascimento = input('Nova data de nascimento')
    sexo = input('Novo sexo (M/F)')
    telefone_fixo = input('Novo telefone fixo: ')
    celular = input('Novo celular: ')
    email = input('Novo e-mail: ')
    #atribuuir na mesma chave substitui o valor antigo
    clientes[cpf] = [nome, data_nascimento, sexo, telefone_fixo, celular, email]
    print('Cliente alterado com sucesso!')

def excluir_clientes(clientes):
    cpf = input('CPF do mcliente que deseja excluir: ')

    if cpf not in clientes:
        print('Cliente não encontrado!')
        return
    del clientes[cpf]       #remove a chave e os dados dela
    print('Cliente excluido com sucesso')


def submenu_clientes(clientes, testes):
    opcao = ''
    while opcao != '0':
        exibir_submenu('CLIENTE')
        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            lista_todos_clientes(clientes)
        elif opcao == '2':
            lista_um_cliente(clientes)
        elif opcao == '3':
            coletar_dados_cliente(clientes)
        elif opcao == '4':
            alterar_clientes(clientes)
        elif opcao == '5':
            excluir_clientes(clientes)
        elif opcao == '0':
            print('Voltano ao menu principal...')
        else:
            print('Opção inválida!')
        

# --------
# VEÍCULO
# --------
def submenu_veiculo(veiculos, testes):
    print('Em construçãp')
# ------------
# TESTE DRIVE
# ------------
def submenu_teste(testes, clientes, veículos):
    print('construçao')
# -----------
# RELATÓRIOS
# -----------
def submenu_relatorios(testes, clientes, veiculos):
    print('contrulçao')
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
            submenu_clientes(clientes, testes)
        elif opcao == "2":
            submenu_veiculo(veiculos, testes)
        elif opcao == "3":
            submenu_teste(testes, clientes, veiculos)
        elif opcao == "4":
            submenu_relatorios(testes, clientes, veiculos)
        elif opcao == "5":
            print('Encerrando o programa...')
        else:
            print('Opção inválida!')
main()

