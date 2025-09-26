from Compromisso import Compromisso

class Agenda:
    def __init__(self, nome):
        self.nome = nome
        self.__compromissos = {}

    def adicionar_Compromisso(self, titulo, descricao, data):
        if titulo in self.__compromissos:
            print("O compromisso já existe.")
        else:
            novo_compromisso = Compromisso(titulo, descricao, data)
            self.__compromissos[titulo] = novo_compromisso
            print("Compromisso adicionado.")

    def remover_compromisso(self, titulo):
        if titulo in self.__compromissos:
            del self.__compromissos[titulo]
            print("Compromisso removido.")
        else:
            print("Compromisso não encontrado.")

    @property
    def listar_compromisso(self):
        for c in self.__compromissos.values():
            c.mostrar_dados()

    def get_compromisso(self, titulo):
        return self.__compromissos.get(titulo)

    def exportar_compromissos(self):
        dados = {}
        for titulo, c in self.__compromissos.items():
            dados[titulo] = {
                "descricao": c._Compromisso__descricao,
                "data": c._Compromisso__data
            }
        return dados

    def importar_compromissos(self, dados):
        for titulo, info in dados.items():
            self.adicionar_Compromisso(titulo, info["descricao"], info["data"])
