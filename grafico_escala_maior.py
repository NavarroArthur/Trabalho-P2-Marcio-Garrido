from collections import OrderedDict
from note1 import Notas

class Grafico_intervalo_maior:
    padrao_intervalo_maior= [ 2, 2, 1, 2, 2, 2, 1] #fórmula padrão é: tom, tom, semitom, tom, tom, tom, semitom
    
    def __init__(self):
        self.nodes = {notas_musicais:OrderedDict() for notas_musicais in Notas}
        self.init() # cria o objeto e permite o objeto interagir com a propria informação e metodos
    
    def add_valor(self,nota,value): # adiciona um novo valor usando o objeto nodes da classe de cima
        self.nodes[nota][value] = None
    
    def init(self):
        notas_musicais = list(Notas)#cria uma lista baseandose no arquivo de Notas musicais
        for i, nota_especifica in enumerate(notas_musicais): # procura na lista de notas_musicais musicais usando o indice 

            proxima_nota_padrao = i #define i(indice) com os seus valores iguais a proxima nota padrao

            for intervalo in self.padrao_intervalo_maior: # percorre o cada intervalo dos toms e semitons

                proxima_nota_padrao = ( proxima_nota_padrao+ intervalo) % len (notas_musicais) # soma o intervalo ao indice da nota que 
                                                                                    #estamos usando e encontra o indice da proxima nota na escala
             
             
                proxima_nota = notas_musicais[proxima_nota_padrao] # pega a nota do indice atual e identifica qual é a proxima nota
            
                self.add_valor(nota_especifica,proxima_nota) # chama um metodo para criar uma ligaçao entre a nota atual e a proxima nota
   
   
    def obter_escala_maior_nota(self,note): # Retorna a escala maior começando da nota dada, incluindo a tônica no final
        escala= list(self.nodes[note].keys())
        return escala   
          