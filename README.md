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

// Em desenvolvimento