# Sistema de triagem com Lista Encadeada Simples

class Nodo:
    def __init__(self, numero: int, cor: str):
        self.numero = numero   # número do cartão
        self.cor = cor         # "A" (amarelo) ou "V" (verde)
        self.prox = None       # ponteiro para o próximo

class ListaEncadeada:
    def __init__(self):
        self.head = None           # cabeça da lista (não circular)
        self.prox_verde = 1        # numeração V inicia em 1
        self.prox_amarelo = 201    # numeração A inicia em 201

    # [EXIGÊNCIA 2/7] inserir no fim da lista (sem considerar prioridade)
    def inserirSemPrioridade(self, nodo: Nodo):
        # anda até o último e insere após ele
        if self.head is None:
            self.head = nodo
            return
        p = self.head
        while p.prox is not None:
            p = p.prox
        p.prox = nodo

    # [EXIGÊNCIA 3/7] inserir respeitando prioridade (todos A antes de V)
    def inserirComPrioridade(self, nodo: Nodo):
        # caso lista vazia
        if self.head is None:
            self.head = nodo
            return
        # se o primeiro já é V, o novo A entra antes de todos (vira head)
        if self.head.cor == "V":
            nodo.prox = self.head
            self.head = nodo
            return
        # existe pelo menos um A: inserir após o último A
        p = self.head
        while p.prox is not None and p.prox.cor == "A":
            p = p.prox
        nodo.prox = p.prox
        p.prox = nodo

    # [EXIGÊNCIA 4/7] coleta a cor, gera número e insere conforme regra
    def inserir(self):
        while True:
            cor = input("Cor do cartão (A=Amarelo, V=Verde): ").strip().upper()
            if cor in ("A", "V"):
                break
            print("Entrada inválida. Digite apenas A ou V.")
        if cor == "V":
            numero = self.prox_verde
            self.prox_verde += 1
            novo = Nodo(numero, "V")
            if self.head is None:
                self.head = novo
            else:
                self.inserirSemPrioridade(novo)
        else:  # "A"
            numero = self.prox_amarelo
            self.prox_amarelo += 1
            novo = Nodo(numero, "A")
            if self.head is None:
                self.head = novo
            else:
                self.inserirComPrioridade(novo)
        print(f"Paciente inserido: {cor}{numero}")

    # [EXIGÊNCIA 5/7] imprime a fila da cabeça ao fim
    def imprimirListaEspera(self):
        if self.head is None:
            print("Fila vazia.")
            return
        print("Fila de espera (da esquerda para a direita):")
        p = self.head
        itens = []
        while p is not None:
            itens.append(f"{p.cor}{p.numero}")
            p = p.prox
        print(" -> ".join(itens))

    # [EXIGÊNCIA 6/7] remove o primeiro e “chama” o paciente
    def atenderPaciente(self):
        if self.head is None:
            print(" - Nenhum paciente na fila.")
            return
        atendido = self.head
        self.head = self.head.prox
        print(f" - Chamando paciente do cartão {atendido.cor}{atendido.numero} para atendimento.")


lista = ListaEncadeada()
# [EXIGÊNCIA 7/7] menu de operação
while True:
    print("\n===TRIAGEM HOSPITALAR===")
    print("1) Adicionar paciente à fila")
    print("2) Mostrar pacientes na fila")
    print("3) Chamar próximo paciente")
    print("4) Sair")

    op = input("Escolha uma opção: ").strip()
    if op == "1":
        lista.inserir()
    elif op == "2":
            lista.imprimirListaEspera()
    elif op == "3":
        lista.atenderPaciente()
    elif op == "4":
        print("Encerrando...")
        break
    else:
        print("Opção inválida. Tente novamente.")
