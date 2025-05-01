from typing import List, Dict


# Criamos uma classe para representar tarefas, em vez de usar dicionários anônimos.
class Tarefa:
    def _init_(self, descricao: str):
        self.descricao = descricao.strip().capitalize()  # Melhor formatação automática
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def _repr_(self):
        status = "✓" if self.concluida else "✗"
        return f"[{status}] {self.descricao}"


class GerenciadorDeTarefas:
    def _init_(self):
        # Dicionário que mapeia nomes de usuários para listas de tarefas
        # Agora usamos uma tipagem explícita para facilitar leitura e debugging
        self._usuarios: Dict[str, List[Tarefa]] = {}

    def adicionar_usuario(self, nome: str) -> None:
        # Ao invés de usar 'print', usamos exceções para indicar erro — mais profissional e fácil de testar
        if nome in self._usuarios:
            raise ValueError(f"Usuário '{nome}' já existe.")
        self._usuarios[nome] = []

    def adicionar_tarefa(self, nome: str, descricao: str) -> None:
        if nome not in self._usuarios:
            raise KeyError(f"Usuário '{nome}' não encontrado.")

        # Usamos a classe Tarefa ao invés de um dicionário comum
        tarefa = Tarefa(descricao)
        self._usuarios[nome].append(tarefa)

    def concluir_tarefa(self, nome: str, indice: int) -> None:
        if nome not in self._usuarios:
            raise KeyError(f"Usuário '{nome}' não encontrado.")

        try:
            self._usuarios[nome][indice].concluir()
        except IndexError:
            raise IndexError(f"Tarefa de índice {indice} não existe para o usuário '{nome}'.")

    def listar_tarefas(self, nome: str, apenas_pendentes: bool = False) -> List[Tarefa]:
        if nome not in self._usuarios:
            raise KeyError(f"Usuário '{nome}' não encontrado.")

        tarefas = self._usuarios[nome]
        # Se apenas_pendentes for True, filtramos as tarefas não concluídas
        return [t for t in tarefas if not t.concluida] if apenas_pendentes else tarefas