
# Árvore Binária de Busca (BST)

Este projeto implementa uma Árvore Binária de Busca (BST) em Python, com uma interface gráfica para interação.

## Funcionalidades

- Inserção de elementos na árvore
- Remoção de elementos
- Busca de elementos
- Visualização da árvore em formato texto
- Interface gráfica interativa

## Requisitos

- Python 3.x
- tkinter (incluído na instalação padrão do Python)

## Como Executar

1. Certifique-se de ter Python 3.x instalado
2. Execute o arquivo principal da interface gráfica:
```bash
python binaria_gui.py
```

## Estrutura do Projeto

- `binaria.py`: Implementação da classe BSTNode e suas funcionalidades
- `binaria_gui.py`: Interface gráfica usando tkinter
- `requirements.txt`: Dependências do projeto

## Uso da Interface

1. Digite uma chave no campo de entrada
2. Use os botões para:
   - Inserir: adiciona a chave à árvore
   - Remover: remove a chave da árvore
   - Buscar: verifica se a chave existe na árvore

A árvore é exibida em formato texto, onde:
- R--- indica um nó filho direito
- L--- indica um nó filho esquerdo
- Root: indica a raiz da árvore

## Implementação

A implementação inclui os seguintes métodos principais:
- `add(key)`: Adiciona um elemento à árvore
- `remove(key)`: Remove um elemento da árvore
- `get(key)`: Busca um elemento na árvore
- `print_tree()`: Exibe a árvore em formato texto
- `traverse()`: Percorre a árvore em diferentes ordens (pre, in, post) 
