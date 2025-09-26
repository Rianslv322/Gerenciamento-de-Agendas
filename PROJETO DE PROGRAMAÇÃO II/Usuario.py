import json
from Agenda import Agenda

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self._agendas = {}

    def criar_agenda(self, nome_agenda):
        if nome_agenda in self._agendas:
            print(f"A agenda '{nome_agenda}' já existe.")
        else:
            self._agendas[nome_agenda] = Agenda(nome_agenda)
            print(f"Agenda '{nome_agenda}' criada com sucesso.")

    def listar_agendas(self):
        if not self._agendas:
            print("Nenhuma agenda cadastrada.")
        else:
            print(f"\nAgendas de {self.nome}:")
            for nome in self._agendas:
                print("-", nome)

    def get_agenda(self, nome_agenda):
        return self._agendas.get(nome_agenda)

    def salvar_dados(self, arquivo="dados.json"):
        dados = {}
        for nome_agenda, agenda in self._agendas.items():
            dados[nome_agenda] = agenda.exportar_compromissos()
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump({"nome": self.nome, "email": self.email, "agendas": dados}, f, ensure_ascii=False, indent=4)

    @staticmethod
    def carregar_dados(arquivo="dados.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                usuario = Usuario(dados["nome"], dados["email"])
                for nome_agenda, compromissos in dados["agendas"].items():
                    usuario.criar_agenda(nome_agenda)
                    usuario.get_agenda(nome_agenda).importar_compromissos(compromissos)
                return usuario
        except (FileNotFoundError, json.JSONDecodeError):
            print("Erro ao carregar os dados. O arquivo pode estar vazio ou corrompido.")
            return None
