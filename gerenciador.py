class GerenciadorDeTarefas:
    def _init_(self):
        # Dicionário: nome do usuário -> lista de tarefas
        self.usuarios = {}

    def adicionar_usuario(self, nome):
        if nome in self.usuarios:
            print(f"Usuário '{nome}' já existe.")
        else:
            self.usuarios[nome] = []

    def adicionar_tarefa(self, nome, descricao):
        if nome not in self.usuarios:
            print(f"Usuário '{nome}' não encontrado.")
            return

        tarefa = {
            "descricao": descricao.strip().capitalize(),  # Descrição formatada
            "concluida": False
        }
        self.usuarios[nome].append(tarefa)

    def concluir_tarefa(self, nome, indice):
        if nome not in self.usuarios:
            print(f"Usuário '{nome}' não encontrado.")
            return

        if 0 <= indice < len(self.usuarios[nome]):
            self.usuarios[nome][indice]["concluida"] = True
        else:
            print(f"Tarefa de índice {indice} não existe para o usuário '{nome}'.")

    def listar_tarefas(self, nome, apenas_pendentes=False):
        if nome not in self.usuarios:
            print(f"Usuário '{nome}' não encontrado.")
            return []

        tarefas = self.usuarios[nome]
        if apenas_pendentes:
            return [t for t in tarefas if not t["concluida"]]
        return tarefas