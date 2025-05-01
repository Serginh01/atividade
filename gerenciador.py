class GerenciadorDeTarefas:
    def __init__(self):
        # Agora o dicionário está mais claro: nome do usuário -> lista de tarefas (como dicionário ainda)
        self.usuarios = {}

    def adicionar_usuario(self, nome):
        if nome in self.usuarios:
            print(f"Usuário '{nome}' já existe.")  # Mensagem mais clara
        else:
            self.usuarios[nome] = []

    def adicionar_tarefa(self, nome, descricao):
        if nome not in self.usuarios:
            print(f"Usuário '{nome}' não encontrado.")
            return

        # A tarefa ainda é um dicionário, mas com estrutura clara
        nova_tarefa = {
            "descricao": descricao.strip().capitalize(),  # Melhor formatação da descrição
            "concluida": False
        }
        self.usuarios[nome].append(nova_tarefa)

    def concluir_tarefa(self, nome, indice):
        if nome not in self.usuarios:
            print(f"Usuário '{nome}' não encontrado.")
            return

        try:
            self.usuarios[nome][indice]["concluida"] = True
        except IndexError:
            print(f"Tarefa de índice {indice} não existe para o usuário '{nome}'.")

    def listar_tarefas(self, nome, apenas_pendentes=False):
        if nome not in self.usuarios:
            print(f"Usuário '{nome}' não encontrado.")
            return []

        tarefas = self.usuarios[nome]
        if apenas_pendentes:
            return [t for t in tarefas if not t["concluida"]]
        return tarefas
