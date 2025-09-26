from Usuario import Usuario

usuario = Usuario.carregar_dados()

# Se não encontrar dados, pede para o usuário cadastrar novamente.
if usuario is None:
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    usuario = Usuario(nome, email)

while True:
    print(f"\n===== MENU PRINCIPAL ({usuario.nome}) =====")
    print("1 - Criar nova agenda")
    print("2 - Listar agendas")
    print("3 - Acessar uma agenda")
    print("0 - Sair")
    print("==========================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_agenda = input("Digite o nome da agenda: ")
        usuario.criar_agenda(nome_agenda)
        usuario.salvar_dados()  # Salva automaticamente no JSON

    elif opcao == "2":
        usuario.listar_agendas()

    elif opcao == "3":
        nome_agenda = input("Digite o nome da agenda que deseja acessar: ")
        agenda = usuario.get_agenda(nome_agenda)

        if agenda is None:
            print(f"A agenda {nome_agenda} não existe.")
        else:
            while True:
                print("#===== MENU =====#")
                print("""
                    [1] Adicionar Compromisso
                    [2] Listar Compromissos
                    [3] Remover Compromisso
                    [4] Acessar Compromisso
                    [0] Voltar ao menu Principal
                """)

                opcao_agenda = input("Escolha uma opção: ")

                if opcao_agenda == "1":
                    print("ADICIONAR COMPROMISSO")
                    titulo = input("Título: ")
                    descricao = input("Descrição: ")
                    data = input("Data (dd/mm/aaaa): ")
                    agenda.adicionar_Compromisso(titulo, descricao, data)
                    usuario.salvar_dados()

                elif opcao_agenda == "2":
                    print("LISTA DE COMPROMISSOS")
                    agenda.listar_compromisso

                elif opcao_agenda == "3":
                    print("REMOVER COMPROMISSO")
                    titulo_remover = input("Digite o título do compromisso a remover: ")
                    agenda.remover_compromisso(titulo_remover)
                    usuario.salvar_dados()

                elif opcao_agenda == "4":
                    titulo_acessar = input("Digite o título do compromisso que deseja acessar: ")
                    compromisso = agenda.get_compromisso(titulo_acessar)

                    if compromisso is None:
                        print("Compromisso não encontrado.")
                    else:
                        while True:
                            print("MENU DE COMPROMISSOS")
                            print("""
                                [1] Ver Título
                                [2] Alterar Título
                                [3] Ver Descrição
                                [4] Alterar Descrição
                                [5] Ver Data
                                [6] Alterar Data
                                [0] Voltar
                            """)
                            opcao_compromisso = input("Escolha uma opção: ")

                            if opcao_compromisso == "1":
                                print(compromisso.ver_titulo)

                            elif opcao_compromisso == "2":
                                novo_titulo = input("Novo Título: ")
                                agenda._Agenda__compromissos.pop(compromisso._Compromisso__titulo)
                                compromisso.alterar_titulo = novo_titulo
                                agenda._Agenda__compromissos[novo_titulo] = compromisso
                                print("Título alterado com sucesso")
                                usuario.salvar_dados()

                            elif opcao_compromisso == "3":
                                print(compromisso.ver_descricao)

                            elif opcao_compromisso == "4":
                                nova_descricao = input("Nova Descrição: ")
                                compromisso.alterar_descricao = nova_descricao
                                print("Descrição alterada com sucesso")
                                usuario.salvar_dados()

                            elif opcao_compromisso == "5":
                                print(compromisso.ver_data)

                            elif opcao_compromisso == "6":
                                nova_data = input("Nova Data (dd/mm/aaaa): ")
                                compromisso.alterar_data = nova_data
                                print("Data alterada com sucesso")
                                usuario.salvar_dados()

                            elif opcao_compromisso == "0":
                                break  # Sai do menu de compromissos

                            else:
                                print("Opção inválida.")
                
                elif opcao_agenda == "0":
                    break  # Volta ao menu principal
                
                else:
                    print("Opção inválida.")
                    
    elif opcao == "0":
        usuario.salvar_dados()  # Salva os dados antes de sair
        print("Saindo do sistema.")
        break  # Sai do programa
    
    else:
        print("Opção não encontrada")
