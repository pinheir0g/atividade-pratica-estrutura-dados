class ElementoDaListaSimples:
    def __init__(self, chave=None, dado=None) -> None:
        self.chave = chave
        self.dado = dado
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self) -> None:
        self.head = None

    def inserir(self, chave, dado):
        nodo = ElementoDaListaSimples(chave, dado)
        if self.head == None:
            self.head = nodo
            return 0
        else:
            nodo.proximo = self.head
            self.head = nodo
            return 0
        
    def imprimir(self):
        if self.head is None:
            print("None")
        else:
            temp = self.head
            while temp:
                print(f"{temp.chave}", end=" -> ")
                temp = temp.proximo
            print("None")
        

class TabelaHash:
    def __init__(self) -> None:
        self.tam = 10
        self.h = [ListaEncadeadaSimples() for i in range(0, self.tam)]

    def hashFunc(self, k):
        if k.upper() == 'DF':
            return 7
        k = list(k)
        return (ord(k[0]) + ord(k[1])) % self.tam
    
    def inserir(self, chave, dado):
        pos = self.hashFunc(chave)
        add = self.h[pos].inserir(chave, dado)

    def imprimir(self):
        for i in range(0, self.tam):
            print(i, end=": ")
            self.h[i].imprimir()
        
        
# Programa Principal
tabela = TabelaHash()
dados = estados_brasileiros = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins"
}
# tabela.imprimir()

for chave, dado in dados.items():
    tabela.inserir(chave, dado)

# tabela.imprimir()

tabela.inserir('GP', 'Gustavo Viana Pinheiro')
tabela.imprimir()