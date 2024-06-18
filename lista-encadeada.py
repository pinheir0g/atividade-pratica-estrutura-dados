class Elemento:
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None

    def __repr__(self):
        return self.cor + ' ' + str(self.numero)

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
            return
        
        nodo_atual = self.head
        while nodo_atual.proximo:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo
        return
    
    def inserirComPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
            return
        
        nodo_atual = self.head
        if nodo_atual.cor == 'V':
            nodo.proximo = nodo_atual
            self.head = nodo
            return
        
        while nodo_atual.proximo and nodo_atual.proximo.cor == 'A':
            nodo_atual = nodo_atual.proximo
            
        nodo.proximo = nodo_atual.proximo
        nodo_atual.proximo = nodo


    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").upper()
        numero = input("Informe o número do cartão: ")
        nodo = Elemento(cor, numero)
        if not self.head:
            self.head = nodo
        else:    
            if cor == "V":
                self.inserirSemPrioridade(nodo)
            else:
                self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        if not self.head:
            print("A lista de espera está vazia.")
            return
        
        nodo_atual = self.head
        while nodo_atual:
            print(nodo_atual)
            nodo_atual = nodo_atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Não há pacientes na lista de espera.")
            return
        else:
            print(f"Paciente com cartão {self.head.cor} {self.head.numero} comparecer ao atendimento ")
            self.head = self.head.proximo

# PROGRAMA PRINCIPAL

listaHospital = ListaEncadeada()

while True:
    print("""
    Hospital Encadeado
    1 - Adicionar paciente a fila
    2 - Mostrar pacientes na fila
    3 - Chamar paciente
    4 - Sair
    """)

    op = int(input("Escolha uma opção: "))
    if op == 1:
        listaHospital.inserir()
    elif op == 2:
        listaHospital.imprimirListaEspera()
    elif op == 3:
        listaHospital.atenderPaciente()
    elif op == 4:
        break
