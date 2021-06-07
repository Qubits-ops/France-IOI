
prenoms = input().split(" ")
nombres = [0] * 2
for idPrenom in range(2):
   prenom = prenoms[idPrenom]
   nombre = 0  
   for posLettre in range(len(prenom)):
      nombre = nombre + (ord(prenom[posLettre]) - ord("A"))
   while nombre >= 10:
      sommeChiffre = 0
      while nombre > 0:
         sommeChiffre = sommeChiffre + nombre % 10
         nombre = nombre // 10
      nombre = sommeChiffre
   nombres[idPrenom] = nombre
print("{} {}".format(nombres[0], nombres[1]))
2)titre palindromique
nbLivres = int(input())
for loop in range(nbLivres):
   titre = input()
   titreMaj = titre.upper()
   estPalindrome = True
   debut = 0
   fin = len(titreMaj) - 1
   while (debut < fin):
      if titreMaj[debut] == ' ':
         debut = debut + 1
      elif titreMaj[fin] == ' ':
         fin = fin - 1
      else:
         if titreMaj[debut] != titreMaj[fin]:
            estPalindrome = False
         debut = debut + 1
         fin = fin - 1
   if estPalindrome:
      print(titre)
 3)frequence apparition
     texte = input()
nbApparitions = [0] * 26
nbLettres = 0;
for posCaractere in range(len(texte)):
   caractere = texte[posCaractere];
   if caractere.isalpha():
      nbLettres = nbLettres + 1
      caractere = caractere.upper()
      num = ord(caractere) - ord("A")
      nbApparitions[num] = nbApparitions[num] + 1
for idLettre in range(26):
   print(nbApparitions[idLettre] / nbLettres)
