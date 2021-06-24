phrase = "Bonjour tout le monde"
phrase_split = phrase.split()
 
resultat = []
 
for mot in reversed(phrase_split):
    resultat.append(mot)
 
resultat_formate = " ".join(resultat).capitalize()
print(resultat_formate)