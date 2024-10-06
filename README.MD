# Simulação de Gerenciamento de Processos

Este projeto é uma simulação de gerenciamento de processos que implementa diferentes algoritmos de escalonamento, incluindo FIFO, Prioridade, SJF e Round Robin. Utiliza a biblioteca `rich` para exibição formatada de informações no console.

## Funcionalidades

- Criação de processos com atributos como ID, tempo necessário e prioridade.
- Simulação de diferentes algoritmos de escalonamento:
  - **FIFO** (First In, First Out)
  - **Prioridade**
  - **SJF** (Shortest Job First)
  - **Round Robin**
- Exibição das filas de processos e dos processos finalizados.
- Cálculo de métricas como tempo de espera médio e turnaround.

## Pré-requisitos

Para executar este projeto, você precisa ter Python 3.6 ou superior instalado em sua máquina.

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/CristhianKapelinski/ProcessSimulation.git
   cd ProcessSimulation
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```

   - No Linux ou macOS:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências:**

   ```bash
   pip install rich
   ```

## Execução do Programa

Após instalar as dependências, você pode executar o programa usando o seguinte comando:

```bash
python3 processSimulation.py
```

## Estrutura do Código

O código é dividido em duas classes principais:

### 1. Classe `Processo`

Representa um processo com os seguintes atributos:

- `id`: Identificador do processo.
- `tempo`: Tempo total necessário para a execução do processo.
- `cicloCriado`: Ciclo em que o processo foi criado.
- `prioridade`: Prioridade do processo.
- `estado`: Estado atual do processo (pronto, executando, finalizado).
- `tempoEspera`: Tempo total de espera do processo.
- `turnaround`: Tempo total do processo desde a criação até a finalização.

### 2. Classe `Escalonador`

Gerencia a simulação dos processos e implementa os diferentes algoritmos de escalonamento. Os métodos principais incluem:

- `criaProcesso()`: Cria um novo processo e o adiciona à fila.
- `simulacaoFIFO()`: Executa a simulação utilizando o algoritmo FIFO.
- `simulacaoPrioridade()`: Executa a simulação utilizando o algoritmo de Prioridade.
- `simulacaoSJF()`: Executa a simulação utilizando o algoritmo SJF.
- `simulacaoRoundRobin()`: Executa a simulação utilizando o algoritmo Round Robin.

## Exemplo de Uso

Inicie a simulação e siga as instruções no console para interagir com a simulação e ver os resultados.

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar ou adicionar novas funcionalidades ao projeto, sinta-se à vontade para abrir um pull request.

## Licença

Este projeto é licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.
