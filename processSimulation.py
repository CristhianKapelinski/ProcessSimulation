# Os sistemas operacionais (SO) são responsáveis por gerenciar e controlar os recursos de
# hardware e software de um sistema computacional. Uma das funções mais críticas de um SO é o
# gerenciamento de processos, que envolve a criação, execução, suspensão e terminação de
# processos no sistema. Processos são instâncias de programas em execução e competem por
# recursos, como o processador, memória, e dispositivos de E/S.
# Neste trabalho, deve-se desenvolver uma simulação que reproduza o comportamento do
# gerenciamento de processos em um sistema operacional. A simulação deve incluir aspectos como
# escalonamento de processos, controle de concorrência e a troca de contexto.
# Requisitos:
# 1. Implementar uma simulação onde novos processos são criados dinamicamente.
# 2. Representar os processos em diferentes estados (Pronto, Executando, Bloqueado,
# Finalizado).
# 3. Simular diferentes algoritmos de escalonamento, como FIFO (First In, First Out),
# Round-Robin, SJF (Shortest Job First) e Prioridade.
# 4. Avaliar o impacto de diferentes algoritmos no tempo de resposta e tempo de execução dos
# processos.
# Instruções para a Simulação
# 1. Linguagem de Programação: A simulação pode ser desenvolvida em qualquer linguagem de
# programação que suporte manipulação de processos e threads, como Python, C, Java ou
# C++.
# 2. Interface do Sistema:
# ○ A simulação pode ser apresentada em uma interface gráfica simples ou por meio de
# linha de comando.
# ○ Deve exibir, de forma visual ou textual, o estado atual dos processos no sistema, o
# tempo de execução de cada um e os eventos de escalonamento.
# 3. Requisitos Funcionais:
# ○ Criar uma fila de processos que devem ser escalonados para execução.
# ○ Implementar pelo menos dois algoritmos de escalonamento.
# ○ Simular a execução concorrente de pelo menos cinco processos.
# 4. Requisitos Não Funcionais:
# ○ O código deve ser bem estruturado, com funções bem definidas e uso de boas
# práticas de programação.
# ○ A simulação deve ser clara e fácil de entender.
from random import randrange

PROCESSOS_TOTAIS = 7
PROCESSOS_INICIAIS = 5
class Processo:
    """
    Classe que representa um processo em uma simulação de SO.
    Atributos:
        id (int): O identificador único do processo.
        tempo (int): O tempo necessário para o processo ser concluído.
        estado (str): O estado atual do processo (Pronto, Executando, Finalizado).
        prioridade (int): A prioridade do processo (não utilizado no FIFO).
        cicloCriado (int): O ciclo em que o processo foi criado.
    """
    def __init__ (self, id : int, tempo : int, cicloCriado : int, prioridade = 0):
        self.id = id
        self.tempo = tempo
        self.cicloCriado = cicloCriado
        self.estado = 'pronto'
        self.prioridade = prioridade
        
    def __str__ (self):
        return f"ID: {self.id}, Ciclos totais necessarios: {self.tempo}, Estado: {self.estado}, Prioridade: {self.prioridade}, Ciclo de Criacao: {self.cicloCriado}"

    def alterar_estado(self, novo_estado : str):
        self.estado = novo_estado

class Escalonador:
    """
    A class to simulate a process scheduler.
    Attributes
    ----------
    ciclo : int
        The current cycle of the scheduler.
    idGeral : int
        The general ID counter for processes.
    listaProcessos : list
        The list of processes in the scheduler.
    Methods
    -------
    __init__():
        Initializes the scheduler with default values.
    criaProcesso():
        Creates a new process and adds it to the process list.
    simulacaoFIFO():
        Simulates the FIFO (First In, First Out) scheduling algorithm.
    """
    def __init__ (self):   
        self.ciclo = 0
        self.idGeral = 0
        self.listaProcessos = []

    def criaProcesso (self):
        """
        Cria um novo processo com tempo aleatório e o adiciona à lista de processos.
        """
        self.idGeral += 1
        processoNovo = Processo (self.idGeral, randrange(1, 10), self.ciclo, randrange(1, 10))
        self.listaProcessos.append (processoNovo)
        print (f"Processo criado: {processoNovo}")

    def exibir_fila_processos(self):
        print("Fila de processos:")
        for processo in self.listaProcessos:
            print(processo)

    def atualizar_prioridades(self):
        for processo in self.listaProcessos:
            processo.prioridade += 1

    def trocaContexto(self, processo : Processo, contador : int):
        processo.alterar_estado('pronto')
        processo.tempo -= contador
        self.listaProcessos.append(processo)
        print(f"Troca de contexto: {processo}")

    def simulacaoFIFO (self):
        print("\nSimulacao FIFO\n")
        for _ in range(3):
            self.criaProcesso()

        processosTotais = 3
        processoAtual = self.listaProcessos[0]
        processoAtual.alterar_estado('executando')
        print(f"\nProcesso atual: {processoAtual}\n")
        self.listaProcessos.pop(0)
        self.exibir_fila_processos()
        contador : int = 0

        while (1): 
            try:
                input()
                print (f"Ciclo: {self.ciclo}")
                if (processoAtual.tempo == contador):
                    if(self.listaProcessos == []):
                        print("Fim da simulacao")
                        break
                    processoAtual.alterar_estado('finalizado')
                    print (f"Processo finalizado: {processoAtual}")
                    processoAtual = self.listaProcessos[0]
                    self.listaProcessos.pop(0)
                    contador = 0
                    processoAtual.alterar_estado('executando')
                    print (f"Processo atual atualizado: {processoAtual}")
                    self.exibir_fila_processos()            
                else :
                    print (f"Processo atual: {processoAtual} - Ciclos restantes para finalizar: {processoAtual.tempo - contador}")

                if (randrange(0,20)) < 5 and processosTotais < 8:
                    self.criaProcesso()
                    processosTotais += 1
                    print (f"Processos na fila: {len(self.listaProcessos)}")
                
                contador += 1
                self.ciclo += 1

            except(EOFError):
                print("Fim da simulacao")
                break

    def simulacaoPrioridade(self):
        print("\nSimulacao Prioridade\n")
        for _ in range(3):
            self.criaProcesso()

        processosTotais = 3
        self.listaProcessos.sort(key=lambda x: x.prioridade, reverse=True)
        processoAtual = self.listaProcessos[0]
        processoAtual.alterar_estado('executando')
        print(f"\nProcesso atual: {processoAtual}\n")
        self.listaProcessos.pop(0)
        self.exibir_fila_processos()
        contador : int = 0
        while (1):
            try:
                input()
                print (f"Ciclo: {self.ciclo}")
                
                if (processoAtual.tempo == contador):
                    processoAtual.alterar_estado('finalizado')
                    print (f"Processo finalizado: {processoAtual}")
                    if(self.listaProcessos == []):
                        print("Fim da simulacao")
                        break
                    self.atualizar_prioridades()
                    processoAtual = self.listaProcessos[0]
                    contador = 0
                    self.listaProcessos.pop(0)
                    processoAtual.alterar_estado('executando')  
                    print (f"Processo atual atualizado: {processoAtual}")
                    self.exibir_fila_processos()
                else :
                    print (f"Processo atual: {processoAtual} - Ciclos restantes para finalizar: {processoAtual.tempo - contador}")

                if (randrange(0,10)) < 5 and processosTotais < 8:
                    self.criaProcesso()
                    processosTotais += 1
                    self.listaProcessos.sort(key=lambda x: x.prioridade, reverse=True)
                    if(self.listaProcessos[0].prioridade > processoAtual.prioridade):
                        self.trocaContexto(processoAtual, contador)
                        self.listaProcessos.sort(key=lambda x: x.prioridade, reverse=True)
                        processoAtual = self.listaProcessos[0]
                        self.listaProcessos.pop(0)
                        contador = 0
                        processoAtual.alterar_estado('executando')
                        print(f"Processo atual atualizado: {processoAtual}")
                    print (f"Processos na fila: {len(self.listaProcessos)}")

                contador += 1
                self.ciclo += 1

            except(EOFError):
                print("Fim da simulacao")
                break

    def simulacaoSJF(self):
        print("\nSimulacao SJF\n")
        for _ in range(3):
            self.criaProcesso()

        processosTotais = 3
        self.listaProcessos.sort(key=lambda x: x.tempo)
        processoAtual = self.listaProcessos[0]
        processoAtual.alterar_estado('executando')
        print(f"\nProcesso atual: {processoAtual}\n")
        self.listaProcessos.pop(0)
        self.exibir_fila_processos()
        contador : int = 0
        while (1):
            try:
                input()
                print (f"Ciclo: {self.ciclo}")
                
                if (processoAtual.tempo == contador):
                    processoAtual.alterar_estado('finalizado')
                    print (f"Processo finalizado: {processoAtual}")
                    if(self.listaProcessos == []):
                        print("Fim da simulacao")
                        break
                    processoAtual = self.listaProcessos[0]
                    contador = 0
                    self.listaProcessos.pop(0)
                    self.listaProcessos.sort(key=lambda x: x.tempo)
                    processoAtual.alterar_estado('executando')
                    print (f"Processo atual atualizado: {processoAtual}")
                    self.exibir_fila_processos()
                else :
                    print (f"Processo atual: {processoAtual} - Ciclos restantes para finalizar: {processoAtual.tempo - contador}")

                if (randrange(0,10)) < 5 and processosTotais < 8:
                    self.criaProcesso()
                    processosTotais += 1
                    self.listaProcessos.sort(key=lambda x: x.tempo)
                    if(self.listaProcessos[0].tempo < (processoAtual.tempo - contador)):
                        self.trocaContexto(processoAtual, contador)
                        self.listaProcessos.sort(key=lambda x: x.tempo)
                        processoAtual = self.listaProcessos[0]
                        self.listaProcessos.pop(0)
                        contador = 0
                        processoAtual.alterar_estado('executando')
                        print(f"Processo atual atualizado: {processoAtual}")
                    print (f"Processos na fila: {len(self.listaProcessos)}")

                contador += 1
                self.ciclo += 1

            except(EOFError):
                print("Fim da simulacao")
                break
    
    def simulacaoRoundRobin(self):
        print("\nSimulacao Round Robin\n")
        for _ in range(3):
            self.criaProcesso()
        
        processosTotais = 3
        processoAtual = self.listaProcessos[0]
        processoAtual.alterar_estado('executando')
        print(f"\nProcesso atual: {processoAtual}\n")
        self.listaProcessos.pop(0)
        self.exibir_fila_processos()
        contador : int = 0
        quantidadeCiclos = 3
        while(1):
            try:
                input()
                print (f"Ciclo: {self.ciclo}")
                if(processoAtual.tempo == contador):
                    if(self.listaProcessos == []):
                        print("Fim da simulacao")
                        break
                    processoAtual.alterar_estado('finalizado')
                    print(f"Processo finalizado: {processoAtual}")
                    processoAtual = self.listaProcessos[0]
                    contador = 0
                    self.listaProcessos.pop(0)
                    processoAtual.alterar_estado('executando')
                    print(f"Processo atual atualizado: {processoAtual}")
                    self.exibir_fila_processos()
                else:
                    print(f"Processo atual: {processoAtual} - Ciclos restantes para finalizar: {processoAtual.tempo - contador}")
                
                if(quantidadeCiclos == 0):
                    self.trocaContexto(processoAtual, contador)
                    processoAtual = self.listaProcessos[0]
                    self.listaProcessos.pop(0)
                    contador = 0
                    processoAtual.alterar_estado('executando')
                    print(f"Processo atual atualizado: {processoAtual}")
                    quantidadeCiclos = 3

                if(randrange(0,10)) < 5 and processosTotais < 8:
                    self.criaProcesso()
                    processosTotais += 1
                    print(f"Processos na fila: {len(self.listaProcessos)}")


                contador += 1
                self.ciclo += 1
                quantidadeCiclos -= 1
            except(EOFError):
                print("Fim da simulacao")
                break

escalonadorFIFO = Escalonador ()
escalonadorFIFO.simulacaoFIFO()
escalonadorPrioridade = Escalonador()
escalonadorPrioridade.simulacaoPrioridade()
escalonadorSJF = Escalonador()
escalonadorSJF.simulacaoSJF()
escalonadorRoundRobin = Escalonador()
escalonadorRoundRobin.simulacaoRoundRobin()

