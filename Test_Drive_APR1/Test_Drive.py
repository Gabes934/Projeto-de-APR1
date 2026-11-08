""" Gerenciamento de Testes Drive - Concessionária de Veículos """

''' 
 ---------------------------------------------------------------------
 MENUS (Funções que apenas exibem as opções na tela 'não têm lógica')
 ---------------------------------------------------------------------
 '''
def exibir_menu_principal():
    # Mostra as opções do menu principal.
    print("\n===== CONCESSIONÁRIA - TESTE DRIVE =====")
    print("1 - Clientes")
    print("2 - Veículos")
    print("3 - TesteDrives")
    print("4 - Relatórios")
    print("5 - Sair")
    print("------------------------------")


def exibir_submenu(titulo):
    # Mostra as opções do submenu.
    # Parâmetro: titulo: nome da entidade que aparece no cabeçalho (ex.: 'CLIENTE')
    # O mesmo submenu serve para Cliente, Veículo e TesteDrive

    print("\n===== SUBMENU DE " + titulo + " =====")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    print("0 - Voltar")
    print("------------------------------")


def exibir_menu_relatorios():
    # Mostra as opções de relatórios (a, b e c do enunciado).
    print("\n===== RELATÓRIOS =====")
    print("1 - Avaliações de um veículo")
    print("2 - Clientes que testaram um veículo em uma data")
    print("3 - Veículos testados entre duas datas")
    print("0 - Voltar")
    print("------------------------------")

'''
 ------------------------------------------------------------------------
 CLIENTE
   chave = CPF (texto)
   valor = [nome, data_nascimento, sexo, telefone_fixo, celular, email]
   posição:  0          1           2          3          4       5
 ------------------------------------------------------------------------
'''

def incluir_cliente(clientes):
    # Inclui um novo cliente (sem repetição de CPF)
    
    cpf = input("CPF: ")

    # Validação da chave: se o CPF já existe no dicionário, não cadastra de novo
    if cpf in clientes:
        print("Já existe um cliente cadastrado com esse CPF!")
        return

    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    sexo = input("Sexo (M/F): ")
    telefone_fixo = input("Telefone fixo: ")
    celular = input("Celular: ")
    email = input("E-mail: ")

    # Guarda no dicionário: o CPF é a chave e os demais dados vão em uma lista
    clientes[cpf] = [nome, data_nascimento, sexo, telefone_fixo, celular, email]
    print('Cliente cadastrado com sucesso!')



def exibir_cliente(cpf, dados):
    # Mostra na tela os dados de um cliente de forma organizada
    print('CPF:',cpf)
    print('Nome:', dados[0])
    print('Data de nascimento:', dados[1])
    print('Sexo:', dados[2])
    print('Telefone_fixo:', dados[3])
    print('Celular:', dados[4])
    print('E-mail:', dados[5])
    print('-'*32) # linha separadora entre um cliente e outro



def lista_todos_clientes(clientes):
    #Lista todos os clientes cadastrados

    if len(clientes) == 0: #dicionario vazio
        print('Nenhum cliente cadastrado.')
        return
    
    # O for sobre um dicionário percorre as chaves (os CPFs)
    for cpf in clientes:
        exibir_cliente(cpf, clientes[cpf])



def lista_um_cliente(clientes):
    # Busca um cliente pelo CPF e mostra seus dados
    cpf = input('CPF do cliente: ')

    # Se a chave não existe, não há o que mostrar
    if cpf not in clientes:
        print('Cliente não encontrado!')
        return

    exibir_cliente(cpf, clientes[cpf])



def alterar_cliente(clientes):
    # Altera os dados de um cliente existente.
    # O CPF é a chave e por isso NÃO pode ser alterado.

    cpf = input('CPF do cliente que deseja alterar: ')

    if cpf not in clientes:
        print('Cliente não encontrado.')
        return
    
    # Pede apenas os dados que podem mudar (tudo, menos o CPF)
    nome = input('Novo nome: ')
    data_nascimento = input('Nova data de nascimento: ')
    sexo = input('Novo sexo (M/F): ')
    telefone_fixo = input('Novo telefone fixo: ')
    celular = input('Novo celular: ')
    email = input('Novo e-mail: ')

    # Atribuir à mesma chave substitui a lista antiga pela nova
    clientes[cpf] = [nome, data_nascimento, sexo, telefone_fixo, celular, email]
    print('Cliente alterado com sucesso!')


def cliente_possui_teste(cpf, testes):
    # Verifica se um cliente possui algum teste drive cadastrado.
    # Retorna True se houver pelo menos um teste drive, False caso contrário.

    for cpf_teste, codigo_veiculo, data in testes:
        if cpf_teste == cpf:
            return True
    return False

def excluir_cliente(clientes, testes):
    # Exclui um cliente pelo CPF, após mostrar seus dados e pedir confirmação.

    cpf = input('CPF do cliente que deseja excluir: ')

    # 1. Verificar existência do cliente
    if cpf not in clientes:
        print('Cliente não encontrado!')
        return

    # 2. Bloquear a exclusão de quem já tem teste drive registrado
    if cliente_possui_teste(cpf, testes):
        print("Não é possível excluir: o cliente possui teste drive cadastrado.")
        return

    # 3. Mostra os dados para o usuário conferir antes de apagar
    print("\nDados do cliente a ser excluído:")
    exibir_cliente(cpf, clientes[cpf])

    # 4. Confirmação: upper() aceita tanto 's' quanto 'S'
    confirmacao = input("Confirma a exclusão? (S/N): ").strip().upper()

    if confirmacao == "S":
        del clientes[cpf]  # remove a chave e os dados associados a ela
        print('Cliente excluido com sucesso')
    else:
        print("Exclusão cancelada.") # Qualquer resposta diferente de S cancela a exclusão.



def submenu_clientes(clientes, testes):
    # Controla o submenu de clientes (loop até o usuário digitar 0)
    opcao = ''
    while opcao != '0':
        exibir_submenu('CLIENTE')
        opcao = input('Escolha uma opção: ').strip() # strip() tira espaços extras

        if opcao == '1':
            lista_todos_clientes(clientes)
        elif opcao == '2':
            lista_um_cliente(clientes)
        elif opcao == '3':
            incluir_cliente(clientes)
        elif opcao == '4':
            alterar_cliente(clientes)
        elif opcao == '5':
            excluir_cliente(clientes, testes)
        elif opcao == '0':
            print('Voltando ao menu principal...')
        else:
            print('Opção inválida!')
        

'''
 ---------------------------------------------
 VEÍCULO
    chave = código do veículo
    valor = [descricao, ano, modelo, valor]
 ---------------------------------------------
'''

def submenu_veiculo(veiculos, testes):
    print('Em construção...')



'''
 ---------------------------------------------
 TESTE DRIVE
    chave = tupla (cpf, codigo_veiculo, data)
    valor = avaliação do cliente
 ---------------------------------------------
'''

def submenu_teste(testes, clientes, veículos):
    print('Em construção...')



'''
 --------------
 RELATÓRIOS
 --------------
'''

def submenu_relatorios(testes, clientes, veiculos):
    print('Em construção...')



# --------------------
# PROGRAMA PRINCIPAL
# --------------------
def main():
    # Cria as estruturas de dados e controla o menu principal.

    clientes = {}
    veiculos = {}
    testes = {}
 
    opcao = ""
    while opcao != "5":
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()  # strip() remove os espaços em branco do começo e do fim do texto

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
