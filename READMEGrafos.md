# Gerador de Escalas Maiores

Este projeto implementa uma interface gráfica para gerar e visualizar escalas maiores musicais, permitindo a seleção de qualquer nota como tônica.

## Funcionalidades

- Interface gráfica para seleção de notas musicais
- Geração de escalas maiores a partir de qualquer nota
- Suporte para todas as notas naturais e sustenidos
- Visualização clara da sequência de notas na escala

## Requisitos

- Python 3.x
- tkinter (incluído na instalação padrão do Python)
- Módulos padrão do Python (enum, collections)

## Como Executar

1. Certifique-se de ter Python 3.x instalado
2. Execute o arquivo principal da interface gráfica:
```bash
python interface_escala_maior.py
```

## Estrutura do Projeto

- `interface_escala_maior.py`: Interface gráfica principal usando tkinter
- `note1.py`: Definição das notas musicais usando Enum
- `grafico_escala_maior.py`: Lógica para geração das escalas maiores
- `requirements.txt`: Dependências do projeto

## Uso da Interface

1. Selecione uma nota musical no menu suspenso
2. Clique no botão "Mostrar Escala Maior"
3. A escala será exibida na tela, mostrando todas as notas em sequência

## Implementação

O projeto é composto por três componentes principais:

### 1. Definição das Notas (`note1.py`)
- Implementa a classe `Notas` usando Enum
- Define todas as notas naturais e sustenidos
- Inclui método para manipulação de notas

### 2. Geração de Escalas (`grafico_escala_maior.py`)
- Implementa a classe `Grafico_intervalo_maior`
- Utiliza o padrão de intervalos da escala maior (2,2,1,2,2,2,1)
- Gera escalas maiores para qualquer nota tônica

### 3. Interface Gráfica (`interface_escala_maior.py`)
- Interface amigável usando tkinter
- Menu suspenso para seleção de notas
- Exibição clara das escalas geradas

## Notas Musicais Suportadas

O sistema suporta as seguintes notas:
- Dó, Dó#
- Ré, Ré#
- Mi
- Fá, Fá#
- Sol, Sol#
- Lá, Lá#
- Si

## Padrão de Intervalos

A escala maior segue o padrão de intervalos:
- Tom (2 semitons)
- Tom (2 semitons)
- Semitom (1 semitom)
- Tom (2 semitons)
- Tom (2 semitons)
- Tom (2 semitons)
- Semitom (1 semitom) 
