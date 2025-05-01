class GerenciadorDeTarefas:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, nome):
        if nome in self.usuarios:
            print("Usuário já existe.")
        else:
            self.usuarios[nome] = []

    def adicionar_tarefa(self, nome, descricao):
        if nome in self.usuarios:
            tarefa = {"descricao": descricao, "concluida": False}
            self.usuarios[nome].append(tarefa)
        else:
            print("Usuário não encontrado.")

    def concluir_tarefa(self, nome, indice):
        if nome in self.usuarios:
            try:
                self.usuarios[nome][indice]["concluida"] = True
            except IndexError:
                print("Índice inválido.")
        else:
            print("Usuário não encontrado.")

    def listar_tarefas(self, nome, apenas_pendentes=False):
        if nome not in self.usuarios:
            print("Usuário não encontrado.")
            return []

        if apenas_pendentes:
            return [t for t in self.usuarios[nome] if not t["concluida"]]
        else:
            return self.usuarios[nome]
