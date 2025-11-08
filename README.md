# Sistema de Triagem Hospitalar – Python (Lista Encadeada)

Este repositório contém um sistema simples de **triagem hospitalar via linha de comando**, desenvolvido em Python, que utiliza **lista encadeada simples** para gerenciar a fila de pacientes.  
Cada paciente recebe um cartão com **cor** e **número**, e a fila respeita prioridade por cor:

- Cartões **Amarelos (A)**: prioridade maior, numeração iniciando em 201  
- Cartões **Verdes (V)**: prioridade menor, numeração iniciando em 1  

## Funcionalidades

- Cadastro de paciente informando a cor do cartão (A = Amarelo, V = Verde)
- Geração automática do número do cartão conforme a cor
- Inserção na fila respeitando prioridade:
  - Todos os **Amarelos** ficam antes dos **Verdes**
  - Mantém a ordem de chegada dentro de cada grupo de cor
- Visualização da fila de espera em ordem de atendimento
- Chamada do próximo paciente (remoção do primeiro da fila)
- Menu interativo em linha de comando

## Estrutura do Código

- `Nodo`: representa cada paciente (número, cor e ponteiro para o próximo)
- `ListaEncadeada`: gerencia a fila com operações de:
  - Inserção sem prioridade (usada para verdes)
  - Inserção com prioridade (posicionando amarelos antes dos verdes)
  - Impressão da fila de espera
  - Atendimento (remoção do primeiro da lista)
- Laço principal com menu:
  - `1` - Adicionar paciente
  - `2` - Mostrar fila
  - `3` - Chamar próximo paciente
  - `4` - Sair

## Requisitos

- Python 3.x

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPO.git
cd NOME-DO-REPO
