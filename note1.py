from enum import Enum
#criando a classe das notas musicais
class Notas(Enum): #cria uma classe notas que vai enumerar as notas musicais e seus sustenidos
    Do = "Dó"
    Do_sustenido= " Dó#"
    Re= "Ré"
    Ré_sustenido= "Ré#"
    Mi = "Mi"
    Fa = "Fá"
    Fá_sustenido= "Fá#"
    Sol= "Sol"
    Sol_sustenido="Sol#"
    Lá="Lá"
    Lá_sustenido="Lá#"
    Si= "Si"

    def remover_nota(note): #escolhe uma nota musical e escolhe uma acima dela
        nota = nota.upper() #transforma tudo em maiusculo
        procura = {
            "Dó#": Notas.Do_sustenido,
            "Ré#" : Notas.Ré_sustenido,
            "Fá#" : Notas.Fá_sustenido,
            "Sol#": Notas.Sol_sustenido,
            "Lá#": Notas.Lá_sustenido 
        }
        return procura.get(nota, Notas[nota])
    
def __str__(self):
    return self.value



