from random import randrange
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

PROCESSOS_TOTAIS = 7
PROCESSOS_INICIAIS = 5

class Processo:
    def __init__(self, id: int, tempo: int, cicloCriado: int, prioridade=0):
        self.id = id
        self.tempo = tempo
        self.cicloCriado = cicloCriado
        self.estado = 'pronto'
        self.prioridade = prioridade
        self.tempoEspera = 0
        self.turnaround = 0
        self.prioridadeInicial = prioridade
        self.tempoTotal = tempo

    def __str__(self):
        return f"ID: {self.id}, Ciclos totais necessarios: {self.tempo}, Estado: {self.estado}, Prioridade: {self.prioridade}, Ciclo de Criacao: {self.cicloCriado}"

    def alterar_estado(self, novo_estado: str):
        self.estado = novo_estado

class Escalonador:
    def __init__(self):   
        self.ciclo = 0
        self.idGeral = 0
        self.listaProcessos = []
        self.processosFinalizados = []

    def criaProcesso(self):
        self.idGeral += 1
        processoNovo = Processo(self.idGeral, randrange(1, 10), self.ciclo, randrange(1, 10))
        self.listaProcessos.append(processoNovo)
        console.print(Panel(f"[green]Processo criado:[/green] {processoNovo}"))

    def exibir_fila_processos(self):
        table = Table(title="Fila de Processos")
        table.add_column("ID", justify="center")
        table.add_column("Ciclos Necessários", justify="center")
        table.add_column("Estado", justify="center")
        table.add_column("Prioridade", justify="center")
        table.add_column("Ciclo de Criação", justify="center")

        for processo in self.listaProcessos:
            table.add_row(str(processo.id), str(processo.tempo), processo.estado, str(processo.prioridade), str(processo.cicloCriado))

        console.print(table)
    
    def exibir_processos_finalizados(self):
        table = Table(title="Processos Finalizados")
        table.add_column("ID", justify="center")
        table.add_column("Ciclos Necessários", justify="center")
        table.add_column("Estado", justify="center")
        table.add_column("Prioridade Final", justify="center")
        table.add_column("Prioridade Inicial", justify="center")
        table.add_column("Ciclo de Criação", justify="center")
        table.add_column("Tempo de Espera", justify="center")
        table.add_column("Turnaround", justify="center")

        tempo_espera_total = 0
        turnaround_total = 0

        for processo in self.processosFinalizados:
            table.add_row(
                str(processo.id),
                str(processo.tempoTotal),
                processo.estado,
                str(processo.prioridade),
                str(processo.prioridadeInicial),
                str(processo.cicloCriado),
                str(processo.tempoEspera),
                str(processo.turnaround)
            )
            tempo_espera_total += processo.tempoEspera
            turnaround_total += processo.turnaround

        if self.processosFinalizados:
            tempo_espera_medio = tempo_espera_total / len(self.processosFinalizados)
            turnaround_medio = turnaround_total / len(self.processosFinalizados)
        else:
            tempo_espera_medio = 0
            turnaround_medio = 0

        console.print(table)
        console.print(f"[yellow]Tempo de Espera Médio: {tempo_espera_medio:.2f}[/yellow]")
        console.print(f"[yellow]Turnaround Médio: {turnaround_medio:.2f}[/yellow]")

    def simulacaoFIFO(self):
        console.print(Panel("[cyan]Simulação FIFO[/cyan]\n"))
        for _ in range(3):
            self.criaProcesso()

        processosTotais = 3
        processoAtual = self.listaProcessos[0]
        processoAtual.alterar_estado('executando')
        console.print(f"[blue]Processo atual:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes")

        self.listaProcessos.pop(0)
        self.exibir_fila_processos()
        contador: int = 0

        while True: 
            try:
                input()
                console.print(f"\n[Ciclo: {self.ciclo}]\n")
                
                if processoAtual.tempo == contador:
                    processoAtual.alterar_estado('finalizado')
                    processoAtual.turnaround = self.ciclo - processoAtual.cicloCriado
                    processoAtual.tempoEspera = processoAtual.turnaround - processoAtual.tempoTotal
                    self.processosFinalizados.append(processoAtual)
                    console.print(f"[red]Processo {processoAtual.id} finalizado.[/red]")

                    if not self.listaProcessos:
                        console.print(Panel("[bold red]Fim da simulação[/bold red]"))
                        self.exibir_processos_finalizados()
                        break

                    processoAtual = self.listaProcessos[0]
                    self.listaProcessos.pop(0)
                    contador = 0
                    processoAtual.alterar_estado('executando')
                    console.print(f"[blue]Processo atual atualizado:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes")
                    self.exibir_fila_processos()
                else:
                    console.print(f"[yellow]Processo atual:[/yellow] ID {processoAtual.id} - Ciclos restantes: {processoAtual.tempo - contador}")

                if randrange(0, 20) < 5 and processosTotais < 8:
                    self.criaProcesso()
                    processosTotais += 1
                    console.print(f"[green]Processos na fila:[/green] {len(self.listaProcessos)}")
                
                contador += 1
                self.ciclo += 1

            except EOFError:
                console.print(Panel("[bold red]Fim da simulação[/bold red]"))
                break

    def atualizar_prioridades(self):
        for processo in self.listaProcessos:
            processo.prioridade += 1
        console.print(Panel("[yellow]Prioridades dos processos atualizadas![/yellow]"))

    def trocaContexto(self, processo: Processo, contador: int):
        processo.alterar_estado('pronto')
        processo.tempo -= contador
        self.listaProcessos.append(processo)
        console.print(Panel(f"[yellow]Troca de contexto realizada para o processo ID {processo.id}[/yellow]"))

    def simulacaoPrioridade(self):
        console.print(Panel("[cyan]Simulação Prioridade[/cyan]\n"))
        for _ in range(3):
            self.criaProcesso()

        processosTotais = 3
        self.listaProcessos.sort(key=lambda x: x.prioridade, reverse=True)
        processoAtual = self.listaProcessos[0]
        processoAtual.alterar_estado('executando')
        console.print(Panel(f"[blue]Processo atual:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes"))
        self.listaProcessos.pop(0)
        self.exibir_fila_processos()
        contador: int = 0

        while True:
            try:
                input()
                console.print(f"\n[Ciclo: {self.ciclo}]\n")

                if processoAtual.tempo == contador:
                    processoAtual.alterar_estado('finalizado')
                    processoAtual.turnaround = self.ciclo - processoAtual.cicloCriado
                    processoAtual.tempoEspera = processoAtual.turnaround - processoAtual.tempoTotal
                    self.processosFinalizados.append(processoAtual)
                    console.print(Panel(f"[red]Processo finalizado: ID {processoAtual.id}[/red]"))
                    if not self.listaProcessos:
                        console.print(Panel("[bold red]Fim da simulação[/bold red]"))
                        self.exibir_processos_finalizados()
                        break
                    self.atualizar_prioridades()
                    processoAtual = self.listaProcessos[0]
                    contador = 0
                    self.listaProcessos.pop(0)
                    processoAtual.alterar_estado('executando')
                    console.print(Panel(f"[blue]Processo atual atualizado:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes"))
                    self.exibir_fila_processos()
                else:
                   console.print(f"[yellow]Processo atual:[/yellow] ID {processoAtual.id} - Ciclos restantes: {processoAtual.tempo - contador}")

                if randrange(0, 10) < 5 and processosTotais < 8:
                    self.criaProcesso()
                    processosTotais += 1
                    self.listaProcessos.sort(key=lambda x: x.prioridade, reverse=True)

                    if self.listaProcessos[0].prioridade > processoAtual.prioridade:
                        self.trocaContexto(processoAtual, contador)
                        self.listaProcessos.sort(key=lambda x: x.prioridade, reverse=True)
                        processoAtual = self.listaProcessos[0]
                        self.listaProcessos.pop(0)
                        contador = 0
                        processoAtual.alterar_estado('executando')
                        console.print(Panel(f"[blue]Processo atual atualizado:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes"))
                    console.print(f"[green]Processos na fila: {len(self.listaProcessos)}")

                contador += 1
                self.ciclo += 1

            except EOFError:
                console.print(Panel("[bold red]Fim da simulação[/bold red]"))
                break


    def simulacaoSJF(self):
        console.print(Panel("[cyan]Simulação SJF[/cyan]\n"))
        for _ in range(3):
            self.criaProcesso()

        processosTotais = 3
        self.listaProcessos.sort(key=lambda x: x.tempo)
        processoAtual = self.listaProcessos[0]
        processoAtual.alterar_estado('executando')
        console.print(Panel(f"[blue]Processo atual:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes"))
        self.listaProcessos.pop(0)
        self.exibir_fila_processos()
        contador: int = 0

        while True:
            try:
                input()
                console.print(f"\n[Ciclo: {self.ciclo}]\n")

                if processoAtual.tempo == contador:
                    processoAtual.alterar_estado('finalizado')
                    processoAtual.turnaround = self.ciclo - processoAtual.cicloCriado
                    processoAtual.tempoEspera = processoAtual.turnaround - processoAtual.tempoTotal
                    self.processosFinalizados.append(processoAtual)
                    console.print(Panel(f"[red]Processo finalizado: ID {processoAtual.id}[/red]"))
                    if not self.listaProcessos:
                        console.print(Panel("[bold red]Fim da simulação[/bold red]"))
                        self.exibir_processos_finalizados()
                        break
                    
                    processoAtual = self.listaProcessos[0]
                    contador = 0
                    self.listaProcessos.pop(0)
                    self.listaProcessos.sort(key=lambda x: x.tempo)
                    processoAtual.alterar_estado('executando')
                    console.print(Panel(f"[blue]Processo atual atualizado:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes"))
                    self.exibir_fila_processos()
                else:
                    console.print(f"[yellow]Processo atual:[/yellow] ID {processoAtual.id} - Ciclos restantes para finalizar: {processoAtual.tempo - contador}")

                if randrange(0, 10) < 5 and processosTotais < 8:
                    self.criaProcesso()
                    processosTotais += 1
                    self.listaProcessos.sort(key=lambda x: x.tempo)
                    if self.listaProcessos[0].tempo < (processoAtual.tempo - contador):
                        self.trocaContexto(processoAtual, contador)
                        self.listaProcessos.sort(key=lambda x: x.tempo)
                        processoAtual = self.listaProcessos[0]
                        self.listaProcessos.pop(0)
                        contador = 0
                        processoAtual.alterar_estado('executando')
                        console.print(Panel(f"[blue]Processo atual atualizado:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes"))
                    console.print(f"[green]Processos na fila: {len(self.listaProcessos)}")

                contador += 1
                self.ciclo += 1

            except EOFError:
                console.print(Panel("[bold red]Fim da simulação[/bold red]"))
                break

    
    def simulacaoRoundRobin(self):
        console.print(Panel("[cyan]Simulação Round Robin[/cyan]\n"))
        for _ in range(3):
            self.criaProcesso()

        processosTotais = 3
        processoAtual = self.listaProcessos[0]
        processoAtual.alterar_estado('executando')
        console.print(Panel(f"[blue]Processo atual:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes\n"))
        self.listaProcessos.pop(0)
        self.exibir_fila_processos()
        contador: int = 0
        quantidadeCiclos = 3

        while True:
            try:
                input()
                console.print(f"[cyan]Ciclo:[/cyan] {self.ciclo}")
                if processoAtual.tempo == contador:
                    processoAtual.alterar_estado('finalizado')
                    processoAtual.turnaround = self.ciclo - processoAtual.cicloCriado
                    processoAtual.tempoEspera = processoAtual.turnaround - processoAtual.tempoTotal
                    self.processosFinalizados.append(processoAtual)
                    console.print(Panel(f"[red]Processo finalizado: ID {processoAtual.id}[/red]"))
                    if not self.listaProcessos:
                        console.print(Panel("[bold red]Fim da simulação[/bold red]"))
                        self.exibir_processos_finalizados()
                        break
                    processoAtual = self.listaProcessos[0]
                    contador = 0
                    self.listaProcessos.pop(0)
                    processoAtual.alterar_estado('executando')
                    console.print(Panel(f"[blue]Processo atual atualizado:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes"))
                    self.exibir_fila_processos()
                else:
                    console.print(f"[yellow]Processo atual:[/yellow] ID {processoAtual.id} - Ciclos restantes para finalizar: {processoAtual.tempo - contador}")

                if quantidadeCiclos == 0:
                    self.trocaContexto(processoAtual, contador)
                    processoAtual = self.listaProcessos[0]
                    self.listaProcessos.pop(0)
                    contador = 0
                    processoAtual.alterar_estado('executando')
                    console.print(Panel(f"[blue]Processo atual atualizado:[/blue] ID {processoAtual.id} com {processoAtual.tempo} ciclos restantes"))
                    quantidadeCiclos = 3

                if randrange(0, 10) < 5 and processosTotais < 8:
                    self.criaProcesso()
                    processosTotais += 1
                    console.print(f"[green]Processos na fila:[/green] {len(self.listaProcessos)}")

                contador += 1
                self.ciclo += 1
                quantidadeCiclos -= 1

            except EOFError:
                console.print(Panel("[bold red]Fim da simulação[/bold red]"))
                break


input("Pressione Enter para iniciar a simulação FIFO")
escalonadorFIFO = Escalonador ()
escalonadorFIFO.simulacaoFIFO()
input("Pressione Enter para iniciar a simulação de Prioridade")
console.clear()
escalonadorPrioridade = Escalonador()
escalonadorPrioridade.simulacaoPrioridade()
input("Pressione Enter para iniciar a simulação SJF")
console.clear()
escalonadorSJF = Escalonador()
escalonadorSJF.simulacaoSJF()
input("Pressione Enter para iniciar a simulação Round Robin")
console.clear()
escalonadorRoundRobin = Escalonador()
escalonadorRoundRobin.simulacaoRoundRobin()

