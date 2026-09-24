import re

import math



f = open("documentsTP3.tsv", "r", encoding="utf-8")

documents = {}


for l in f:
    ch = l.split()
    if len(ch) > 1:
        id_doc = ch[0]            
        phrase = " ".join(ch[1:])
        documents[id_doc] = phrase
        
def convertir_dict_text(documents):
    text=""
    for i in documents.values():
        text=text+i+"\n"
    return text

def remove_stopwords(mots_du_texte):
    stopwords = ["the", "a", "an", "is", "are", "and", "or", "in", "on", "of", "to", "for"]
    mots_filtres = []
    
    for mot in mots_du_texte:
        if mot not in stopwords:
            mots_filtres.append(mot)
            
    return " ".join(mots_filtres)

def construire_index_enrichi(documents):
    index_inverse = {}

    for id_doc, phrase in documents.items():
        mots = preprocess(phrase).split()

        for mot in mots:
            if mot not in index_inverse:
                index_inverse[mot] = {
                    "df": 0,
                    "postings": {}
                }

            if id_doc not in index_inverse[mot]["postings"]:
                index_inverse[mot]["postings"][id_doc] = {"tf": 0}
                index_inverse[mot]["df"] = index_inverse[mot]["df"] + 1

            index_inverse[mot]["postings"][id_doc]["tf"] = index_inverse[mot]["postings"][id_doc]["tf"] + 1

    return index_inverse

def tokeniser(texte): 
    return re.findall(r"\b\w+\b", texte.lower())
        
def preprocess(text):
    
    etape1et2=tokeniser(text)
    etape3=remove_stopwords(etape1et2)
    return etape3
   
def calculer_idf(terme, index_inverse, N):
    df = index_inverse[terme]["df"]
    idf = math.log10(N / df)
    return idf

def afficher_idf(index_inverse, N):
    print(" TERM DF IDF")

    for terme, information in index_inverse.items():
        df = information["df"]
        idf = calculer_idf(terme, index_inverse, N)

        print(terme, " ", df, " ", round(idf, 3))

text=convertir_dict_text(documents)
print(preprocess(text))





def trouver_extremes(index_inverse, N):
    terme_df_max = ""
    terme_df_min = ""
    terme_idf_max = ""

    df_max = 0
    df_min = N + 1
    idf_max = 0

    for terme, information in index_inverse.items():
        df = information["df"]
        idf = calculer_idf(terme, index_inverse, N)

        if df > df_max:
            df_max = df
            terme_df_max = terme

        if df < df_min:
            df_min = df
            terme_df_min = terme

        if idf > idf_max:
            idf_max = idf
            terme_idf_max = terme

    print("Terme de DF maximal :", terme_df_max)
    print("DF maximal :", df_max)

    print("Terme de DF minimal :", terme_df_min)
    print("DF minimal :", df_min)

    print("Terme de plus grand IDF :", terme_idf_max)
    print("IDF maximal :", round(idf_max, 3))

index_inverse=construire_index_enrichi(documents)

print("TERM DF POSTINGS")

for mot, information in index_inverse.items():
    postings=""

    for id_doc, info in information["postings"].items():
        postings=postings+id_doc+"(tf="+str(info["tf"])+"), "

    print(mot, " ", information["df"], " ", postings)
    
    
def poids_tfidf(terme, doc_id, index_inverse, N):
    tf = index_inverse[terme]["postings"][doc_id]["tf"]
    idf = calculer_idf(terme, index_inverse, N)

    if tf > 0:
        poids = (1 + math.log10(tf)) * idf
    else:
        poids = 0

    return poids

def afficher_tfidf(doc_id, index_inverse, N):
    resultats = []

    for terme, information in index_inverse.items():
        if doc_id in information["postings"]:
            tf = information["postings"][doc_id]["tf"]
            df = information["df"]
            idf = calculer_idf(terme, index_inverse, N)
            poids = poids_tfidf(terme, doc_id, index_inverse, N)

            resultats.append((terme, tf, df, idf, poids))

    resultats.sort(key=lambda x: x[4], reverse=True)

    print("\nDocument", doc_id)
    print("TERM\t\tTF\tDF\tIDF\tTF-IDF")

    for terme, tf, df, idf, poids in resultats:
        print(terme, "\t\t", tf, "\t", df, "\t", round(idf, 3), "\t", round(poids, 3))
        
def document_vector(doc_id, vocabulary, index_inverse, N):
    vector = []

    for terme in vocabulary:
        if terme in index_inverse and doc_id in index_inverse[terme]["postings"]:
            poids = poids_tfidf(terme, doc_id, index_inverse, N)
            vector.append(poids)
        else:
            vector.append(0)

    return vector


def afficher_vecteur(doc_id, vector):
    print("\n", doc_id, ":", vector)

    nombre_zero = 0

    for valeur in vector:
        if valeur == 0:
            nombre_zero = nombre_zero + 1

    print("Nombre de composantes nulles :", nombre_zero)
    
    
def document_vector(doc_id, vocabulary, index_inverse, N):
    vector = []

    for terme in vocabulary:
        if terme in index_inverse and doc_id in index_inverse[terme]["postings"]:
            poids = poids_tfidf(terme, doc_id, index_inverse, N)
            vector.append(poids)
        else:
            vector.append(0)

    return vector


def afficher_vecteur(doc_id, vector):
    print("\n", doc_id, ":", vector)

    nombre_zero = 0

    for valeur in vector:
        if valeur == 0:
            nombre_zero = nombre_zero + 1

    print("Nombre de composantes nulles :", nombre_zero)
    

N = len(documents)

afficher_idf(index_inverse, N)

trouver_extremes(index_inverse, N)

afficher_tfidf("D8", index_inverse, N)


vocabulary = sorted(index_inverse.keys())

vector_D1 = document_vector("D1", vocabulary, index_inverse, N)
vector_D2 = document_vector("D2", vocabulary, index_inverse, N)
vector_D3 = document_vector("D3", vocabulary, index_inverse, N)

afficher_vecteur("D1", vector_D1)
afficher_vecteur("D2", vector_D2)
afficher_vecteur("D3", vector_D3)

vocabulary = sorted(index_inverse.keys())

    
