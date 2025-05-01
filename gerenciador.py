class GerenciadorDeTarefas:
    def _init_(self):
        # Dicionário que mapeia o nome do usuário para sua lista de tarefas
        self.usuarios = {}

    def adicionar_usuario(self, nome):
        # Verifica se o nome já existe
        if not isinstance(nome, str) or not nome.strip():
            print("Nome de usuário inválido.")
            return

        nome = nome.strip()

        if nome in self.usuarios:
            print(f"Usuário '{nome}' já existe.")
        else:
            self.usuarios[nome] = []
            print(f"Usuário '{nome}' adicionado com sucesso.")

    def adicionar_tarefa(self, nome, descricao):
        # Verificações básicas de entrada
        if not isinstance(descricao, str) or not descricao.strip():
            print("Descrição da tarefa inválida.")
            return

        nome = nome.strip()
        descricao = descricao.strip().capitalize()

        if nome not in self.usuarios:
            print(f"Usuário '{nome}' não encontrado.")
            return

        # Cria a tarefa como um dicionário
        nova_tarefa = {
            "descricao": descricao,
            "concluida": False
        }
        self.usuarios[nome].append(nova_tarefa)
        print(f"Tarefa adicionada para o usuário '{nome}': {descricao}")

    def concluir_tarefa(self, nome, indice):
        nome = nome.strip()

        if nome not in self.usuarios:
            print(f"Usuário '{nome}' não encontrado.")
            return

        if not isinstance(indice, int):
            print("Índice de tarefa inválido.")
            return

        try:
            self.usuarios[nome][indice]["concluida"] = True
            print(f"Tarefa {indice} do usuário '{nome}' marcada como concluída.")
        except IndexError:
            print(f"Tarefa de índice {indice} não existe para o usuário '{nome}'.")

    def listar_tarefas(self, nome, apenas_pendentes=False):
        nome = nome.strip()

        if nome not in self.usuarios:
            print(f"Usuário '{nome}' não encontrado.")
            return []

        tarefas = self.usuarios[nome]
        resultado = []

        for i, tarefa in enumerate(tarefas):
            if apenas_pendentes and tarefa["concluida"]:
                continue
            status = "✓" if tarefa["concluida"] else "✗"
            resultado.append(f"{i}. [{status}] {tarefa['descricao']}")

        return resultado