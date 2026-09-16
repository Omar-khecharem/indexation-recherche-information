import math
print("exercice 1: ")
f = open("documents.tsv", "r", encoding="utf-8")

print("exercice 2: ")
index_inverse = {
    "accès": [9],
    "améliore": [7],
    "artificielle": [7],
    "besoin": [10],
    "blockchain": [4],
    "classe": [8],
    "collection": [2],
    "collections": [6],
    "distribuée": [4],
    "documents": [1, 2, 3, 6, 8],
    "expriment": [10],
    "facilite": [9],
    "grande": [2],
    "grandes": [6],
    "index": [3],
    "indexation": [5, 9],
    "indexe": [2],
    "information": [1],
    "informations": [9],
    "intelligence": [7],
    "inversé": [3],
    "manière": [4],
    "moteur": [2],
    "moteurs": [5, 7],
    "permet": [1, 3, 4],
    "pertinence": [8],
    "pertinents": [1],
    "rapide": [3, 9],
    "recherche": [1, 2, 3, 5, 6, 7, 8],
    "requête": [10],
    "retrouver": [1],
    "stocker": [4],
    "structures": [5],
    "système": [8],
    "traite": [6],
    "transactions": [4],
    "utilisateurs": [10],
    "utilisent": [5],
    "web": [6]
}


def intersection(list1, list2):
    i, j = 0, 0
    result = []
    
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
            
    return result


def intersection_skip(list1, list2):
    i, j = 0, 0
    resultat = []
    saut1 = int(math.sqrt(len(list1)))
    saut2 = int(math.sqrt(len(list2)))
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            resultat.append(list1[i])
            i+= 1
            j+= 1
        elif list1[i] < list2[j]:
            if saut1>1 and i+saut1<len(list1) and list1[i+saut1] <=list2[j]:
                i=saut1+i
            else:
                i=i+1
        else:
            if saut2>1 and j+saut2<len(list2) and list2[j + saut2]<=list1[i]:
                j = saut2+j
            else:
                j =1+j
    return resultat


print("exercice 3: ")
terme1 = input("Entrez le premier terme : ")
terme2 = input("Entrez le deuxième terme : ")
 
docs1 = index_inverse.get(terme1.lower(), [])
docs2 = index_inverse.get(terme2.lower(), [])
    
print("Postings" ,terme1 ,":" ,docs1)
print("Postings ",terme2,":" ,docs2)
    

resultat = intersection(docs1, docs2)
print("Intersection :",resultat)

print("exercice 4: ")
print("Intersection avec le skip :",intersection_skip(docs1,docs2))
