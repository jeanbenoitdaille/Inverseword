# Inverseword
Inverser les mots dans une phrase 
Le but de cet exercice était d'inverser l'ordre des mots contenus dans la variable "phrase".

Là encore, vous commencez à être habitués, nous utilisons la méthode split pour séparer les mots de la phrase en liste.

Une fois les mots séparés dans une liste, nous utilisons la fonction reversed pour inverser la liste contenue dans "phrase_split" :

    for mot in reversed(phrase_split):

Pour inverser une liste, nous pouvons également utiliser la façon de faire suivante (qui signifie en fait : "récupère tous les éléments de la liste, en partant par la fin") :

    for mot in phrase_split[::-1]:

Nous ajoutons ensuite chaque mot récupéré dans la boucle for dans la liste "resultat".

Pour finir, nous joignons tous les mots contenus dans la liste "resultat" par un espace avec la méthode join et nous utilisons la méthode capitalize pour rajouter une majuscule en début de phrase :

    resultat_formate = " ".join(resultat).capitalize()
