# Atividade Prática - Estrutura de dados

Este projeto consiste em dois programas distintos:

**Sistema de Triagem Hospitalar**: Implementação de uma lista encadeada para gerenciar a fila de atendimento em um hospital, priorizando pacientes com base na urgência indicada por cartões amarelos e verdes.

**Tabela Hash para Emplacamento de Veículos**: Implementação de uma tabela hash com endereçamento em cadeia para gerenciar a associação entre as siglas dos estados brasileiros e a posição da tabela com base em uma função hash.

## Sistema de Triagem Hospitalar
### Requisitos

- **Nodo**: Representa um cartão numerado contendo cor, número e um ponteiro para o próximo nodo.
- **Lista Encadeada**: Contém um ponteiro para a cabeça da lista (head).

### Funcionalidades
1. **Inserção Sem Prioridade**: Insere um novo nodo no final da lista.
2. **Inserção Com Prioridade**: Insere um novo nodo antes dos nodos com cartão verde.
3. **Inserir**: Solicita ao usuário a cor e o número do cartão, e insere o novo nodo na lista conforme a prioridade.
4. **Imprimir Lista de Espera**: Imprime todos os cartões na lista de espera.
5. **Atender Paciente**: Remove o primeiro paciente da fila e imprime uma mensagem chamando o paciente para atendimento.
6. **Menu de Interação**: Oferece opções para adicionar pacientes, mostrar a fila de espera, chamar o próximo paciente, e sair do programa.

## Tabela Hash para Emplacamento de Veículos

### Requisitos
- **Nodo**: Representa um estado contendo sigla, nome do estado e um ponteiro para o próximo nodo.
- **Tabela Hash**: Contém 10 posições, cada uma representando a cabeça de uma lista encadeada.

### Funcionalidades

1. **Função Hash**:
   - A entrada deve ser uma string com 2 letras, representando a sigla do estado ou distrito federal.
   - Caso a sigla seja DF, a função deve retornar 7.
   - Caso contrário, a função deve retornar a posição com base na soma dos valores ASCII das duas letras, modulo 10.
2. **Inserção na Tabela Hash**: Insere um novo nodo no início da lista encadeada correspondente à posição calculada pela função hash.
3. **Inserir Estados**: Insere todos os 26 estados e o Distrito Federal na tabela hash usando a função hash.
4. **Inserir Estado Fictício**: Insere um estado fictício com siglas formadas pela primeira letra do nome e a primeira letra do último sobrenome.
5. **Imprimir Tabela Hash**: Imprime as siglas de todos os nodos na tabela hash, separadas por posição.
