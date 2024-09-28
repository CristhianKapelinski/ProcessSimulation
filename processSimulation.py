from random import randrange
from time import sleep

class processo:
    def __init__ (self, id:int, tempo:int, cicloCriado:int, prioridade=0):
        self.id = id
        self.tempo = tempo
        self.estado = ['pronto']
        self.prioridade = prioridade
        self.cicloCriado = cicloCriado

class Escalonador:

    def __init__ (self):   
        self.ciclo = 0
        self.idGeral = 0
        self.listaProcessos = []

    def criaProcesso (self):
        self.idGeral += 1
        processoNovo = processo (self.idGeral, randrange(1, 10), self.ciclo)
        self.listaProcessos.append (processoNovo)

    def simulacaoFIFO (self):

        self.criaProcesso()
        self.criaProcesso()
        self.criaProcesso()
        self.criaProcesso()
        self.criaProcesso()

        processoAtual = processo (0, -1)

        while (1):
            try:
                input()

                if (randrange(0,20)) < 5:
                    self.criaProcesso()

                if (processoAtual.tempo <= 0 and self.listaProcessos != []):
                    processoAtual = self.listaProcessos[0]
                    self.listaProcessos.pop(0)
                    print (f"Processo atualizado: {processoAtual}")

                processoAtual.tempo -= 1
                self.ciclo += 1
            
            except(EOFError):
                print("Fim da simulacao")
                break


escalonador = Escalonador ()
escalonador.simulacaoFIFO()