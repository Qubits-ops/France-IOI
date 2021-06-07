
import sys
nbValeurs = 0
valeurs = []
def indexDuMaximum():
   indexDuMax = 0
   for pos in range(nbValeurs):
      if valeurs[pos] > valeurs[indexDuMax]:
         indexDuMax = pos
   return indexDuMax
def extraitMaximum():
   global nbValeurs, valeurs
   indexDuMax = indexDuMaximum()
   value = valeurs[indexDuMax]
   valeurs[indexDuMax] = valeurs[nbValeurs - 1]
   nbValeurs -= 1
   return value
 
def main():
   global nbValeurs, valeurs
   nbValeurs, nbExtractions = map(int, input().split())
   valeurs = list(map(int, sys.stdin.readline().split()))
   print(" ".join(map(str, [extraitMaximum() for _ in range(nbExtractions)])))
main()
2)course automobile
import sys
def main():
   nbAutos = int(input())
   idAuto = list(map(int, sys.stdin.readline().split()))
   
   depassementsEffectues = []
   for _ in range(nbAutos):
      for rang in range(nbAutos - 1):
         if idAuto[rang] > idAuto[rang+1]:
            depassementsEffectues.append( (idAuto[rang], idAuto[rang+1]))
            idAuto[rang], idAuto[rang+1] = idAuto[rang+1], idAuto[rang]
 
   sys.stdout.write(str(len(depassementsEffectues)) + "\n")
   for (idAutoDepassee, idAutoQuiDepasse) in depassementsEffectues:
      sys.stdout.write(str(idAutoDepassee) + " " + str(idAutoQuiDepasse) + "\n")
main()
3)tri de donnee
import sys
valeurs = []
 
def indexDuMaximum(nbRestant):
   indexDuMax = 0
   for index in range(nbRestant):
      if valeurs[index] > valeurs[indexDuMax]:
         indexDuMax = index
   return indexDuMax
 
def triSelection():
   global valeurs
   for nbRestant in range(len(valeurs), 0, -1):
      indiceMax = indexDuMaximum(nbRestant)
      valeurs[indiceMax], valeurs[nbRestant-1] = valeurs[nbRestant-1], valeurs[indiceMax]
 
def main():
   global valeurs
   _ = int(input())
   valeurs = list(map(int, sys.stdin.readline().split()))
 
   triSelection()
 
   for valeur in valeurs:
      print(valeur, end = " ")
      
main()
4)matiere recyclabes
def main():
   nbMots = int(input())
   mots = [input() for _ in range(nbMots)]
   mots.sort()
   for mot in mots:
      print(mot)
main()
