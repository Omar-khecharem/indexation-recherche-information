import re 
import time 
f = open("documents.tsv", "r", encoding="utf-8")
documents = {}


for l in f:
    ch = l.split()
    if len(ch) > 1:
        id_doc = ch[0]            
        phrase = " ".join(ch[1:])
        documents[id_doc] = phrase
   
    
     
def convertir_dict_text():
    text=""
    for i in documents.values():
        text=text+i+"\n"
    return text
 
def recherche_naive(terme, documents): 
    resultats = [] 
 
    for doc_id, texte in documents.items(): 
        if terme.lower() in texte.lower(): 
            resultats.append(doc_id) 
 
    return resultats


def tokeniser(texte): 
    return re.findall(r"\b\w+\b", texte.lower())


def supprimer_stopwords(tokens):
    stopwords = { 
    "le", "la", "les", "un", "une", 
    "de", "des", "du", "et", "dans", 
    "par", "pour", "d", "l" 
    } 
    text=convertir_dict_text()
    text_tokenised=tokeniser(text)
    text_tokenised_sans_stopwords = []
    for i in text_tokenised:
        if i not in stopwords:
            text_tokenised_sans_stopwords.append(i)
            
    return text_tokenised_sans_stopwords
            
 
def preprocess(texte): 
    tokens = tokeniser(texte)
    tokens = supprimer_stopwords(tokens) 
    return tokens 
    
       
def construire_index(documents): 
    index_inverse = {} 
 
    for doc_id, texte in documents.items(): 
        termes = preprocess(texte) 
 
        for terme in set(termes): 
            if terme not in index_inverse: 
                index_inverse[terme] = [] 
 
            index_inverse[terme].append(doc_id) 
 
    return index_inverse

def rechercher(terme, index_inverse): 
    return index_inverse.get(terme.lower(), [])


def intersection(list1, list2): 
    i = 0 
    j = 0 
    resultat = [] 
 
    while i < len(list1) and j < len(list2): 
 
        if list1[i] == list2[j]: 
            resultat.append(list1[i]) 
            i += 1 
            j += 1 
 
        elif list1[i] < list2[j]: 
            i += 1 
 
        else: 
            j += 1 
 
    return resultat 

#MAIN

print("Exercice 1 :")
print("\n")
print("Le nombre des documents est ",len(documents))
print("Le contenu des documents est :",documents)

print("Exercice 2 :")
text=convertir_dict_text()
terme = input("Entrez un terme : ") 
print(recherche_naive(terme, documents))

print("Exercice 3 :")
print(tokeniser(text))
print(supprimer_stopwords(documents))

print("Exercice 4 :")

print(preprocess(text))

print("exercice 5:")
index_inverse=construire_index(documents)
print(index_inverse)

print("exercice 6:")
print(rechercher(terme,index_inverse))

print("exercice 7")
terme1 = input("Entrez le premier terme : ").lower() 
terme2 = input("Entrez le deuxième terme : ").lower() 
 
docs1 = index_inverse.get(terme1, []) 
docs2 = index_inverse.get(terme2, []) 
 
print("Intersection :", intersection(docs1, docs2))
print("exercice 8")
debut = time.perf_counter()
fin = time.perf_counter() 
print("Temps :", fin - debut)

print("Fin TP1")
