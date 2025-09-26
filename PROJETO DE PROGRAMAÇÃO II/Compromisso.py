meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

string = "/"

class Compromisso:
    def __init__(self, titulo, descricao, data):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data = data

    @property
    def ver_titulo(self):
        return f"Título: {self.__titulo}"
    
    @ver_titulo.setter
    def alterar_titulo(self, novo_titulo):
        self.__titulo = novo_titulo
        return f"Título do compromisso alterado para: {novo_titulo}"
    
    @property
    def ver_descricao(self):
        return f"Descrição do compromisso: {self.__descricao}"
    
    @ver_descricao.setter
    def alterar_descricao(self, nova_descricao):
        self.__descricao = nova_descricao
        return f"Descrição Alterada: {nova_descricao}"

    @property 
    def ver_data(self):
        return f"Data de criação do Compromisso: {self.__data}"
    
    @ver_data.setter
    def alterar_data(self, nova_data):
        if "/" in nova_data and isinstance(int(nova_data.split('/')[0]), int):
            self.__data = nova_data
            return f"Nova data do compromisso definida: {nova_data}"
        return "Data inválida, por favor verifique se não há erro de digitação."
    
    @staticmethod
    def validar_data(data):
        for mes, dia in enumerate(meses):
            if (mes in data or dia+1 in data and string in data):
                print(True)
            else:
                print("Algo está errado, confira novamente a data")    

    def mostrar_dados(self):
        print(f"""
DADOS DO COMPROMISSO
|----------------------------------------
| {self.__titulo}
|- {self.__descricao} 
|- {self.ver_data}
|----------------------------------------
""")
